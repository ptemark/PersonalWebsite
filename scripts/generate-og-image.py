#!/usr/bin/env python3
"""
Generate the Open Graph social preview image for petermark.dev.
Output: img/og-image.png (1200x630)
Palette matches site dark theme: bg #0f0f0f, accent #A78BFA, muted #888888, text #e5e5e5
"""

import os
from PIL import Image, ImageDraw, ImageFont

# --- Palette (mirrors CSS custom properties) ---
BG       = (15, 15, 15)        # #0f0f0f
SURFACE  = (26, 26, 26)        # #1a1a1a
ACCENT   = (167, 139, 250)     # #A78BFA
TEXT     = (229, 229, 229)     # #e5e5e5
MUTED    = (136, 136, 136)     # #888888
BORDER   = (42, 42, 42)        # #2a2a2a

W, H = 1200, 630

# --- Font paths ---
FONT_BOLD   = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_REGULAR = "/System/Library/Fonts/Supplemental/Arial.ttf"

def load_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except (IOError, OSError):
        return ImageFont.load_default()

def main():
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    # --- Accent bar: left vertical stripe ---
    bar_w = 8
    bar_margin = 80
    bar_top = 80
    bar_bottom = H - 80
    draw.rectangle([(bar_margin, bar_top), (bar_margin + bar_w, bar_bottom)], fill=ACCENT)

    # --- Accent dot cluster (top-right decorative) ---
    dot_r = 5
    dot_gap = 22
    dot_origin_x = W - 100
    dot_origin_y = 100
    for row in range(4):
        for col in range(4):
            cx = dot_origin_x + col * dot_gap
            cy = dot_origin_y + row * dot_gap
            alpha = 180 - (row + col) * 18
            dot_color = (ACCENT[0], ACCENT[1], ACCENT[2])
            draw.ellipse([(cx - dot_r, cy - dot_r), (cx + dot_r, cy + dot_r)], fill=dot_color)

    # --- Text layout (left-aligned, inset from accent bar) ---
    text_x = bar_margin + bar_w + 48  # 48px gap after bar

    # Greeting
    font_greeting = load_font(FONT_REGULAR, 26)
    draw.text((text_x, 160), "Hi, I'm", font=font_greeting, fill=MUTED)

    # Name
    font_name = load_font(FONT_BOLD, 96)
    draw.text((text_x, 200), "Peter Mark", font=font_name, fill=ACCENT)

    # Title
    font_title = load_font(FONT_REGULAR, 40)
    draw.text((text_x, 318), "Senior Software Engineer", font=font_title, fill=TEXT)

    # Tagline
    font_tag = load_font(FONT_REGULAR, 28)
    draw.text((text_x, 384), "7+ years · Java · AWS · Microservices", font=font_tag, fill=MUTED)

    # URL (bottom-right)
    font_url = load_font(FONT_REGULAR, 26)
    url = "petermark.dev"
    bbox = draw.textbbox((0, 0), url, font=font_url)
    url_w = bbox[2] - bbox[0]
    draw.text((W - url_w - 80, H - 72), url, font=font_url, fill=MUTED)

    # --- Output ---
    out_dir = os.path.join(os.path.dirname(__file__), "..", "img")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "og-image.png")
    img.save(out_path, "PNG", optimize=True)
    print(f"Saved: {os.path.abspath(out_path)}  ({W}x{H})")

if __name__ == "__main__":
    main()
