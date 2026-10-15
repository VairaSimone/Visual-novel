"""Generate original, deterministic audio assets for La Bambola della Porta Accanto.

Only the Python standard library is required. Run this file from any directory:
    python tools/generate_prototype_audio.py

The music cues use repeating motifs and chord movement instead of a single drone.
Ambient loops are given a short end-to-start crossfade to reduce clicks on looping.
"""
from array import array
from math import exp, pi, sin, tanh
from pathlib import Path
import sys
import wave


RATE = 22050
OUT = Path(__file__).parents[1] / "La bambola della porta accanto" / "game" / "audio"


class Noise:
    """Small deterministic PRNG so regenerated prototype assets are reproducible."""
    def __init__(self, seed=1791999556):
        self.state = seed & 0xFFFFFFFF

    def uniform(self, low=-1.0, high=1.0):
        value = self.state
        value ^= (value << 13) & 0xFFFFFFFF
        value ^= value >> 17
        value ^= (value << 5) & 0xFFFFFFFF
        self.state = value & 0xFFFFFFFF
        return low + (self.state / 4294967296.0) * (high - low)


RNG = Noise()


def clamp(value, limit=0.96):
    return max(-limit, min(limit, value))


def loop_crossfade(samples, seconds=0.45):
    """Join a loop's tail to its head without adding a silent gap."""
    frames = min(int(RATE * seconds), len(samples) // 4)
    if frames < 2:
        return samples
    head = samples[:frames]
    tail = samples[-frames:]
    blend = []
    for i, (left, right) in enumerate(zip(tail, head)):
        amount = (i + 1) / (frames + 1)
        blend.append(left * (1.0 - amount) + right * amount)
    return samples[frames:-frames] + blend


def write(name, samples, loopable=False):
    OUT.mkdir(parents=True, exist_ok=True)
    if loopable:
        samples = loop_crossfade(samples)
    # A soft limiter prevents transient peaks from clipping harshly.
    ceiling = tanh(1.15)
    pcm = array("h", (
        int(clamp(tanh(value * 1.15) / ceiling) * 32767)
        for value in samples
    ))
    if sys.byteorder != "little":
        pcm.byteswap()
    with wave.open(str(OUT / name), "wb") as file:
        file.setnchannels(1)
        file.setsampwidth(2)
        file.setframerate(RATE)
        file.writeframes(pcm.tobytes())


def edge_fade(t, duration, edge=0.025):
    return min(1.0, t / edge, max(0.0, (duration - t) / edge))


def bell(t, start, frequency, duration, amplitude, decay=3.0):
    elapsed = t - start
    if elapsed < 0.0 or elapsed >= duration:
        return 0.0
    attack = min(1.0, elapsed / 0.012)
    tail = max(0.0, 1.0 - elapsed / duration)
    envelope = attack * (tail ** 1.7) * exp(-elapsed * decay)
    fundamental = sin(2 * pi * frequency * elapsed)
    partial = 0.30 * sin(2 * pi * frequency * 2.01 * elapsed)
    air = 0.10 * sin(2 * pi * frequency * 3.97 * elapsed)
    return (fundamental + partial + air) * amplitude * envelope


def bowed_pad(t, root, strength=1.0):
    # Slow, slightly imperfect harmonics suggest bowed strings without samples.
    breathe = 0.84 + 0.16 * sin(2 * pi * 0.075 * t)
    fundamental = sin(2 * pi * root * t)
    fifth = sin(2 * pi * root * 1.498 * t + 0.3)
    octave = sin(2 * pi * root * 2.003 * t + 0.7)
    return strength * breathe * (0.62 * fundamental + 0.25 * fifth + 0.13 * octave)


def ambience_rain():
    seconds = 26
    total = RATE * seconds
    low = 0.0
    samples = []
    drops = (1.7, 4.8, 7.1, 11.9, 14.2, 18.8, 22.1, 24.5)
    for i in range(total):
        t = i / RATE
        low = low * 0.994 + RNG.uniform() * 0.006
        hiss = RNG.uniform() * 0.042
        distant = sin(2 * pi * 43 * t) * (0.014 + 0.004 * sin(2 * pi * 0.07 * t))
        drops_layer = 0.0
        for start in drops:
            elapsed = t - start
            if 0.0 <= elapsed < 0.20:
                drops_layer += (sin(2 * pi * (680 + 120 * elapsed) * elapsed)
                                * 0.035 * exp(-elapsed * 22))
        samples.append((low * 0.38 + hiss + distant + drops_layer)
                       * edge_fade(t, seconds, 0.025))
    write("ambience_rain.wav", samples, loopable=True)


def ambience_room():
    seconds = 24
    total = RATE * seconds
    samples = []
    for i in range(total):
        t = i / RATE
        hum = (sin(2 * pi * 50 * t) * 0.018
               + sin(2 * pi * 100.2 * t + 0.2) * 0.008
               + sin(2 * pi * 73 * t) * 0.004)
        air = RNG.uniform() * 0.0045
        swell = 0.7 + 0.3 * sin(2 * pi * 0.09 * t + 0.8)
        distant_creak = sin(2 * pi * (166 + 7 * sin(2 * pi * 0.16 * t)) * t) * 0.003
        samples.append((hum * swell + air + distant_creak)
                       * edge_fade(t, seconds, 0.025))
    write("ambience_room.wav", samples, loopable=True)


def menu_music():
    """A 32-second minor-key title cue: bass movement, bell motif and pulse."""
    seconds = 32
    total = RATE * seconds
    roots = (55.0, 65.406, 49.0, 58.270)
    motif = (
        (0.35, 392.00, 0.95, 0.095), (1.65, 466.16, 0.80, 0.075),
        (2.55, 523.25, 1.20, 0.090), (4.25, 392.00, 1.10, 0.075),
        (5.65, 311.13, 1.55, 0.080),
    )
    events = []
    transpositions = (1.0, 1.1892, 0.9439, 0.8909)
    for section, transpose in enumerate(transpositions):
        for start, frequency, duration, volume in motif:
            events.append((section * 8 + start, frequency * transpose, duration, volume))
    samples = []
    for i in range(total):
        t = i / RATE
        section = min(3, int(t // 8))
        local = t - section * 8
        root = roots[section]
        pad = bowed_pad(t, root, 0.042)
        pad += sin(2 * pi * root * 1.25 * t) * 0.010
        # Slow chord handover avoids an abrupt change at each eight-second bar.
        if local > 6.9:
            nxt = roots[(section + 1) % len(roots)]
            amount = (local - 6.9) / 1.1
            amount = amount * amount * (3.0 - 2.0 * amount)
            pad = pad * (1.0 - amount) + bowed_pad(t, nxt, 0.042) * amount
        pulse = sin(2 * pi * (0.25 + 0.035 * sin(2 * pi * 0.04 * t)) * t) * 0.010
        notes = sum(bell(t, start, frequency, duration, volume, 2.7)
                    for start, frequency, duration, volume in events)
        samples.append(pad + pulse + notes)
    write("music_menu.wav", samples, loopable=True)


def investigation_music():
    """Reflective, restrained underscore with a four-note recurring motif."""
    seconds = 24
    total = RATE * seconds
    roots = (65.406, 58.270, 73.416, 55.0)
    motif = ((0.55, 261.63, 1.5, 0.055), (2.15, 311.13, 1.2, 0.050),
             (3.45, 392.00, 1.6, 0.060), (5.2, 349.23, 1.3, 0.045))
    events = []
    for section, transpose in enumerate((1.0, 0.9439, 1.1225, 0.8909)):
        for start, frequency, duration, volume in motif:
            events.append((section * 6 + start, frequency * transpose, duration, volume))
    samples = []
    for i in range(total):
        t = i / RATE
        section = min(3, int(t // 6))
        local = t - section * 6
        root = roots[section]
        pad = bowed_pad(t, root, 0.032)
        pad += sin(2 * pi * root * 1.5 * t) * 0.008
        if local > 5.0:
            nxt = roots[(section + 1) % len(roots)]
            amount = (local - 5.0)
            amount = amount * amount * (3.0 - 2.0 * amount)
            pad = pad * (1.0 - amount) + bowed_pad(t, nxt, 0.032) * amount
        motif_layer = sum(bell(t, start, frequency, duration, volume, 2.3)
                          for start, frequency, duration, volume in events)
        samples.append(pad + motif_layer)
    write("music_investigation.wav", samples, loopable=True)


def tension_music():
    """Uneven low pulses, a dissonant high motif and slow harmonic pressure."""
    seconds = 20
    total = RATE * seconds
    roots = (46.25, 49.0, 43.65, 51.91)
    high_notes = ((0.8, 622.25, 1.7, 0.030), (3.2, 587.33, 1.4, 0.028),
                  (4.35, 698.46, 1.8, 0.035))
    events = []
    for section, transpose in enumerate((1.0, 1.0595, 0.9439, 1.1225)):
        for start, frequency, duration, volume in high_notes:
            events.append((section * 5 + start, frequency * transpose, duration, volume))
    beats = (0.3, 0.62, 2.1, 2.42, 4.0)
    samples = []
    for i in range(total):
        t = i / RATE
        section = min(3, int(t // 5))
        local = t - section * 5
        root = roots[section]
        pressure = 0.55 + 0.45 * sin(2 * pi * 0.055 * t)
        pad = bowed_pad(t, root, 0.050 * pressure)
        pad += sin(2 * pi * root * 1.4142 * t) * 0.009 * pressure
        if local > 4.15:
            nxt = roots[(section + 1) % len(roots)]
            amount = (local - 4.15) / 0.85
            amount = amount * amount * (3.0 - 2.0 * amount)
            pad = pad * (1.0 - amount) + bowed_pad(t, nxt, 0.050 * pressure) * amount
        pulses = 0.0
        for beat in beats:
            start = section * 5 + beat
            elapsed = t - start
            if 0 <= elapsed < 0.32:
                pulses += (sin(2 * pi * (48 - elapsed * 15) * elapsed)
                           * 0.060 * exp(-elapsed * 13))
        notes = sum(bell(t, start, frequency, duration, volume, 2.0)
                    for start, frequency, duration, volume in events)
        samples.append(pad + pulses + notes)
    write("music_tension.wav", samples, loopable=True)


def lighter():
    seconds = 0.95
    samples = []
    for i in range(int(RATE * seconds)):
        t = i / RATE
        click = RNG.uniform() * 0.27 * exp(-t * 68)
        flame = (sin(2 * pi * 142 * t) * 0.035 + RNG.uniform() * 0.018)
        flame *= exp(-max(0.0, t - 0.045) * 3.2)
        samples.append((click + flame) * edge_fade(t, seconds, 0.012))
    write("sfx_lighter.wav", samples)


def window_knock():
    seconds = 1.6
    knocks = ((0.10, 0.32, 198.0), (0.51, 0.27, 187.0), (0.83, 0.38, 205.0))
    samples = []
    for i in range(int(RATE * seconds)):
        t = i / RATE
        tone = 0.0
        for start, strength, frequency in knocks:
            elapsed = t - start
            if 0 <= elapsed < 0.34:
                impulse = (sin(2 * pi * frequency * elapsed)
                           + 0.30 * sin(2 * pi * frequency * 2.04 * elapsed))
                tone += impulse * strength * exp(-elapsed * 12)
                tone += RNG.uniform() * 0.02 * exp(-elapsed * 35) * strength
        samples.append(tone * 0.20 * edge_fade(t, seconds, 0.012))
    write("sfx_window_knock.wav", samples)


def phone():
    seconds = 1.25
    samples = []
    for i in range(int(RATE * seconds)):
        t = i / RATE
        gate = 1.0 if (t % 0.32) < 0.20 else 0.0
        tone = (sin(2 * pi * 880 * t) * 0.19
                + sin(2 * pi * 1174.66 * t) * 0.095
                + sin(2 * pi * 1760 * t) * 0.025)
        samples.append(tone * gate * exp(-t * 1.1) * edge_fade(t, seconds, 0.012))
    write("sfx_phone.wav", samples)


def heartbeat():
    seconds = 2.15
    samples = []
    for i in range(int(RATE * seconds)):
        t = i / RATE
        beat = 0.0
        for start, strength in ((0.12, 1.0), (0.38, 0.65), (1.08, 1.0), (1.34, 0.65)):
            elapsed = t - start
            if 0 <= elapsed < 0.25:
                beat += (sin(2 * pi * (56 - elapsed * 22) * elapsed)
                         * 0.32 * strength * exp(-elapsed * 15))
        samples.append(beat * edge_fade(t, seconds, 0.015))
    write("sfx_heartbeat.wav", samples)


def glass():
    seconds = 1.5
    freqs = (987.77, 1318.51, 1760.0, 2349.32, 2793.83)
    samples = []
    for i in range(int(RATE * seconds)):
        t = i / RATE
        elapsed = max(0.0, t - 0.018)
        strike = 0.0
        if t >= 0.018:
            for index, frequency in enumerate(freqs):
                strike += (sin(2 * pi * frequency * elapsed)
                           * (0.075 / (index + 1)) * exp(-elapsed * (4.0 + index)))
            strike += RNG.uniform() * 0.025 * exp(-elapsed * 30)
        samples.append(strike * edge_fade(t, seconds, 0.012))
    write("sfx_glass.wav", samples)


def door():
    seconds = 1.65
    samples = []
    for i in range(int(RATE * seconds)):
        t = i / RATE
        creak = (sin(2 * pi * (72 + 42 * t) * t)
                 + 0.35 * sin(2 * pi * (116 + 29 * t) * t))
        creak *= 0.095 * exp(-t * 1.9)
        scrape = RNG.uniform() * 0.018 * exp(-t * 2.4)
        elapsed = t - 1.03
        thud = 0.0
        if 0 <= elapsed < 0.28:
            thud = sin(2 * pi * (61 - 17 * elapsed) * elapsed) * 0.27 * exp(-elapsed * 13)
        samples.append((creak + scrape + thud) * edge_fade(t, seconds, 0.012))
    write("sfx_door.wav", samples)


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    ambience_rain()
    ambience_room()
    menu_music()
    investigation_music()
    tension_music()
    lighter()
    window_knock()
    phone()
    heartbeat()
    glass()
    door()
    print("Generated 11 deterministic WAV assets in {}".format(OUT))
