"""Generate original, royalty-free WAV ambience and effects for the game."""

from array import array
from math import exp, pi, sin
from pathlib import Path
from random import Random
import wave


RATE = 22050
OUT = Path(__file__).parents[1] / "La bambola della porta accanto" / "game" / "audio"
RNG = Random(1791999556)


def clamp(value):
    return max(-1.0, min(1.0, value))


def write(name, samples):
    OUT.mkdir(parents=True, exist_ok=True)
    data = array("h", (int(clamp(value) * 32767) for value in samples))
    with wave.open(str(OUT / name), "wb") as file:
        file.setnchannels(1)
        file.setsampwidth(2)
        file.setframerate(RATE)
        file.writeframes(data.tobytes())


def fade(index, total, edge=0.04):
    edge_samples = int(total * edge)
    if index < edge_samples:
        return index / max(1, edge_samples)
    if index > total - edge_samples:
        return (total - index) / max(1, edge_samples)
    return 1.0


def ambience_rain():
    seconds = 26
    total = RATE * seconds
    low = 0.0
    samples = []
    for i in range(total):
        low = low * 0.992 + RNG.uniform(-1.0, 1.0) * 0.008
        rain = RNG.uniform(-1.0, 1.0) * 0.075
        distant = sin(2 * pi * 47 * i / RATE) * 0.018
        samples.append((low * 0.6 + rain + distant) * fade(i, total, 0.08))
    write("ambience_rain.wav", samples)


def ambience_room():
    seconds = 24
    total = RATE * seconds
    samples = []
    for i in range(total):
        t = i / RATE
        hum = sin(2 * pi * 53 * t) * 0.025 + sin(2 * pi * 106 * t) * 0.012
        air = sin(2 * pi * 0.11 * t) * 0.01 + RNG.uniform(-1, 1) * 0.006
        samples.append((hum + air) * fade(i, total, 0.08))
    write("ambience_room.wav", samples)


def menu_music():
    seconds = 30
    total = RATE * seconds
    samples = []
    for i in range(total):
        t = i / RATE
        drone = sin(2 * pi * 55 * t) * 0.10 + sin(2 * pi * 82.41 * t) * 0.045
        pulse = sin(2 * pi * 0.085 * t) * 0.018
        shimmer = sin(2 * pi * 220 * t) * 0.006 * (0.5 + 0.5 * sin(2 * pi * 0.17 * t))
        samples.append((drone + pulse + shimmer) * fade(i, total, 0.07))
    write("music_menu.wav", samples)


def lighter():
    total = int(RATE * 1.1)
    samples = []
    for i in range(total):
        t = i / RATE
        click = RNG.uniform(-1, 1) * 0.55 * exp(-t * 52)
        flame = (sin(2 * pi * 148 * t) * 0.055 + RNG.uniform(-1, 1) * 0.03) * exp(-max(0, t - 0.05) * 2.2)
        samples.append((click + flame) * fade(i, total))
    write("sfx_lighter.wav", samples)


def window_knock():
    total = int(RATE * 1.45)
    samples = []
    for i in range(total):
        t = i / RATE
        tone = 0.0
        for offset in (0.10, 0.48, 0.72):
            elapsed = t - offset
            if elapsed >= 0:
                tone += sin(2 * pi * 198 * elapsed) * 0.48 * exp(-elapsed * 13)
                tone += sin(2 * pi * 94 * elapsed) * 0.22 * exp(-elapsed * 10)
        samples.append(tone * fade(i, total))
    write("sfx_window_knock.wav", samples)


def phone():
    total = int(RATE * 1.35)
    samples = []
    for i in range(total):
        t = i / RATE
        envelope = exp(-t * 3.6)
        tone = (sin(2 * pi * 880 * t) + sin(2 * pi * 1174.66 * t) * 0.55) * 0.20 * envelope
        samples.append(tone * fade(i, total))
    write("sfx_phone.wav", samples)


def heartbeat():
    total = int(RATE * 2.1)
    samples = []
    for i in range(total):
        t = i / RATE
        beat = 0.0
        for offset, strength in ((0.15, 1.0), (0.43, 0.78), (1.13, 1.0), (1.41, 0.78)):
            elapsed = t - offset
            if elapsed >= 0:
                beat += sin(2 * pi * 54 * elapsed) * 0.38 * strength * exp(-elapsed * 16)
        samples.append(beat * fade(i, total))
    write("sfx_heartbeat.wav", samples)


def glass():
    total = int(RATE * 1.6)
    freqs = (987.77, 1318.51, 1760, 2349.32)
    samples = []
    for i in range(total):
        t = i / RATE
        tone = sum(sin(2 * pi * frequency * t) * 0.12 * exp(-t * (3.5 + index)) for index, frequency in enumerate(freqs))
        samples.append(tone * fade(i, total))
    write("sfx_glass.wav", samples)


def door():
    total = int(RATE * 1.4)
    samples = []
    for i in range(total):
        t = i / RATE
        creak = sin(2 * pi * (78 + 55 * t) * t) * 0.16 * exp(-t * 1.7)
        thud = sin(2 * pi * 63 * max(0, t - 0.93)) * 0.42 * exp(-max(0, t - 0.93) * 12)
        samples.append((creak + thud) * fade(i, total))
    write("sfx_door.wav", samples)


if __name__ == "__main__":
    ambience_rain()
    ambience_room()
    menu_music()
    lighter()
    window_knock()
    phone()
    heartbeat()
    glass()
    door()
    print(f"Created prototype audio in {OUT}")
