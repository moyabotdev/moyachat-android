#!/usr/bin/env python3
"""Faerbt das Material-3-Theme des Forks auf die MoyaVPN-Marke um.
Ersetzt nur die primary/secondary/tertiary-Familien (Marken-Akzent) mit
einer blau/gruenen Tonleiter; Neutral-, Surface- und Fehlerfarben bleiben.
Aufruf: python3 rebrand_colors.py <pfad/colors-themed.xml>
"""
import colorsys
import re
import sys

# Seed-Hues aus MoyaVPN: Blau #2C6BED, Gruen #3DDC97
FAMILIES = {
    "primary":   (0.606, 0.85),   # H,S fuer Blau
    "secondary": (0.606, 0.45),   # gedaempftes Blau
    "tertiary":  (0.44, 0.70),    # Gruen
}

# M3 Tone-Zuordnung je Rolle (light, dark)
TONES = {
    "light": {"": 40, "on": 100, "container": 90, "oncontainer": 10},
    "dark":  {"": 80, "on": 20, "container": 30, "oncontainer": 90},
}


def tone_hex(h, s, tone):
    light = tone / 100.0
    s2 = s * (0.35 + 0.65 * (1 - abs(light - 0.5) * 2))  # weniger Sat an den Enden
    r, g, b = colorsys.hls_to_rgb(h, light, s2)
    return "#%02x%02x%02x" % (round(r * 255), round(g * 255), round(b * 255))


def role_for(token):
    # token z.B. md_theme_light_onPrimaryContainer
    m = re.match(r"md_theme_(light|dark)_(on)?([A-Za-z]+?)(Container)?$", token)
    if not m:
        return None
    mode, on, fam, cont = m.group(1), m.group(2), m.group(3).lower(), m.group(4)
    if fam not in FAMILIES:
        return None
    if on and cont:
        role = "oncontainer"
    elif on:
        role = "on"
    elif cont:
        role = "container"
    else:
        role = ""
    return mode, fam, role


def main(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()

    def repl(m):
        name, val = m.group(1), m.group(2)
        r = role_for(name)
        if not r:
            return m.group(0)
        mode, fam, role = r
        h, s = FAMILIES[fam]
        hexc = tone_hex(h, s, TONES[mode][role])
        return '<color name="%s">%s</color>' % (name, hexc)

    new = re.sub(r'<color name="([a-zA-Z_]+)">(#[0-9a-fA-F]+)</color>', repl, text)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new)
    print("umgefaerbt:", path)


if __name__ == "__main__":
    main(sys.argv[1])
