#!/usr/bin/env python3
"""
Generate a screenshot-style placeholder for the personal-website project card.
Output: img/projects/personal-website.png (640x360)
Renders a simplified dark-theme preview: navbar, hero text, section labels.
Palette matches site dark theme: bg #0f0f0f, accent #A78BFA, muted #888888, text #e5e5e5
"""

import os
from PIL import Image, ImageDraw, ImageFont

# --- Palette (mirrors CSS custom properties) ---
BG      = (15, 15, 15)         # #0f0f0f
SURFACE = (26, 26, 26)         # #1a1a1a
ACCENT  = (167, 139, 250)      # #A78BFA
TEXT    = (229, 229, 229)      # #e5e5e5
MUTED   = (136, 136, 136)      # #888888
BORDER  = (42, 42, 42)         # #2a2a2a
BTN_OUTLINE = (80, 60, 120)    # outline button border (accent-tinted)

W, H = 640, 360

# --- Font paths ---
FONT_BOLD    = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_REGULAR = "/System/Library/Fonts/Supplemental/Arial.ttf"


def load_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except (IOError, OSError):
        return ImageFont.load_default()


def draw_rounded_rect(draw, xy, radius, fill=None, outline=None, outline_width=1):
    """Draw a rectangle with rounded corners."""
    x0, y0, x1, y1 = xy
    draw.rounded_rectangle([x0, y0, x1, y1], radius=radius, fill=fill,
                           outline=outline, width=outline_width)


def main():
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    # -------------------------------------------------------------------------
    # NAV BAR (height 32px)
    # -------------------------------------------------------------------------
    nav_h = 32
    draw.rectangle([(0, 0), (W, nav_h)], fill=SURFACE)
    # Bottom border on nav
    draw.line([(0, nav_h), (W, nav_h)], fill=BORDER, width=1)

    font_nav_brand = load_font(FONT_BOLD, 12)
    font_nav_link  = load_font(FONT_REGULAR, 10)

    px = 20  # horizontal page padding (scaled)

    # Wordmark "Peter Mark" in accent
    draw.text((px, 9), "Peter Mark", font=font_nav_brand, fill=ACCENT)

    # Nav links right-aligned
    nav_links = "Experience   Projects"
    bbox = draw.textbbox((0, 0), nav_links, font=font_nav_link)
    link_w = bbox[2] - bbox[0]
    draw.text((W - link_w - px - 18, 11), nav_links, font=font_nav_link, fill=MUTED)

    # Theme toggle dot (sun icon suggestion)
    toggle_cx = W - px - 8
    toggle_cy = nav_h // 2
    draw.ellipse(
        [(toggle_cx - 5, toggle_cy - 5), (toggle_cx + 5, toggle_cy + 5)],
        outline=MUTED, width=1
    )
    # tiny rays
    for dx, dy in [(0, -8), (0, 8), (-8, 0), (8, 0)]:
        draw.line(
            [(toggle_cx + dx // 2, toggle_cy + dy // 2),
             (toggle_cx + dx * 3 // 4, toggle_cy + dy * 3 // 4)],
            fill=MUTED, width=1
        )

    # -------------------------------------------------------------------------
    # HERO SECTION
    # -------------------------------------------------------------------------
    hero_top = nav_h + 22
    font_greeting  = load_font(FONT_REGULAR, 11)
    font_name      = load_font(FONT_BOLD, 36)
    font_title     = load_font(FONT_REGULAR, 14)
    font_tagline   = load_font(FONT_REGULAR, 11)
    font_btn       = load_font(FONT_BOLD, 10)

    # "Hi, I'm"
    draw.text((px, hero_top), "Hi, I'm", font=font_greeting, fill=MUTED)

    # "Peter Mark" — large accent name
    name_y = hero_top + 16
    draw.text((px, name_y), "Peter Mark", font=font_name, fill=ACCENT)

    # "Senior Software Engineer"
    title_y = name_y + 44
    draw.text((px, title_y), "Senior Software Engineer", font=font_title, fill=TEXT)

    # Tagline
    tagline_y = title_y + 20
    draw.text((px, tagline_y), "7+ years · Java · AWS · Microservices",
              font=font_tagline, fill=MUTED)

    # CTA Buttons
    btn_y = tagline_y + 20
    btn_h = 22
    btn_radius = 6

    # Primary button — filled accent
    btn1_text = "View My Work"
    bbox1 = draw.textbbox((0, 0), btn1_text, font=font_btn)
    btn1_w = bbox1[2] - bbox1[0] + 20
    draw_rounded_rect(draw, (px, btn_y, px + btn1_w, btn_y + btn_h),
                      radius=btn_radius, fill=ACCENT)
    draw.text((px + 10, btn_y + 6), btn1_text, font=font_btn, fill=BG)

    # Secondary button — outlined
    btn2_x = px + btn1_w + 10
    btn2_text = "Get In Touch"
    bbox2 = draw.textbbox((0, 0), btn2_text, font=font_btn)
    btn2_w = bbox2[2] - bbox2[0] + 20
    draw_rounded_rect(draw, (btn2_x, btn_y, btn2_x + btn2_w, btn_y + btn_h),
                      radius=btn_radius, fill=None, outline=ACCENT, outline_width=1)
    draw.text((btn2_x + 10, btn_y + 6), btn2_text, font=font_btn, fill=ACCENT)

    # Social icon dots (GitHub, LinkedIn, Email) — simplified circles
    social_y = btn_y + btn_h + 14
    for i in range(3):
        cx = px + i * 22 + 6
        draw.ellipse([(cx - 5, social_y - 5), (cx + 5, social_y + 5)],
                     outline=MUTED, width=1)

    # -------------------------------------------------------------------------
    # SECTION DIVIDER & EXPERIENCE LABEL (peeks in at bottom)
    # -------------------------------------------------------------------------
    divider_y = H - 58
    draw.line([(0, divider_y), (W, divider_y)], fill=BORDER, width=1)

    font_section_label = load_font(FONT_BOLD, 14)
    draw.text((px, divider_y + 12), "Experience", font=font_section_label, fill=TEXT)

    # Timeline left accent bar (experience section preview)
    tl_x = px
    tl_top = divider_y + 34
    tl_bot = H - 4
    draw.rectangle([(tl_x, tl_top), (tl_x + 2, tl_bot)], fill=ACCENT)

    # Timeline entry stub
    font_tl = load_font(FONT_REGULAR, 10)
    draw.text((tl_x + 10, tl_top + 2), "Senior Software Engineer — FIS",
              font=font_tl, fill=TEXT)
    draw.text((tl_x + 10, tl_top + 15), "June 2025 – July 2025",
              font=font_tl, fill=MUTED)

    # Gradient-style fade at very bottom to suggest more content
    for i in range(20):
        alpha = int(255 * (i / 20))
        y = H - 20 + i
        if 0 <= y < H:
            draw.line([(0, y), (W, y)], fill=(BG[0], BG[1], BG[2]))

    # -------------------------------------------------------------------------
    # Output
    # -------------------------------------------------------------------------
    out_dir = os.path.join(os.path.dirname(__file__), "..", "img", "projects")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "personal-website.png")
    img.save(out_path, "PNG", optimize=True)
    print(f"Saved: {os.path.abspath(out_path)}  ({W}x{H})")


if __name__ == "__main__":
    main()
