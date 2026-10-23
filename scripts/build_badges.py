#!/usr/bin/env python3
"""Regenerate LiangYou PosterBadges v1. Requires Pillow>=10.
Brand names describe media features; artwork is not an official certification badge.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BADGES = [
    ("4k", "4K", "ULTRA HD", "#EAC46C"),
    ("1080p", "1080P", "FULL HD", "#A7CAFF"),
    ("hdr10", "HDR10", "HIGH DYNAMIC RANGE", "#FFB76B"),
    ("hdr10-plus", "HDR10+", "DYNAMIC HDR", "#F6AF6A"),
    ("dolby-vision", "DOLBY VISION", "HDR VIDEO", "#B49AFF"),
    ("atmos", "ATMOS", "IMMERSIVE AUDIO", "#76C7FF"),
    ("truehd", "TRUEHD", "LOSSLESS AUDIO", "#E6BB7B"),
    ("dts-hd-ma", "DTS-HD MA", "MASTER AUDIO", "#78D8D5"),
    ("hevc", "HEVC", "H.265 VIDEO", "#94CBEA"),
    ("remux", "REMUX", "DISC SOURCE", "#F0D58B"),
    ("web-dl", "WEB-DL", "STREAM SOURCE", "#B7BED1"),
    ("10bit", "10BIT", "COLOR DEPTH", "#B3DE90"),
]
W, H, S = 540, 164, 3
ROOT = Path(__file__).resolve().parents[1]
FONT_CANDIDATES = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/opentype/inter/InterDisplay-Bold.otf",
]
MEDIUM_CANDIDATES = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/opentype/inter/InterDisplay-Regular.otf",
]

def font(px, bold=True):
    for path in FONT_CANDIDATES if bold else MEDIUM_CANDIDATES:
        try:
            return ImageFont.truetype(path, px)
        except OSError:
            continue
    return ImageFont.truetype("DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf", px)

def rgb(h):
    return tuple(int(h[i:i+2], 16) for i in (1, 3, 5))

def make_png(stem, label, sub, accent, theme):
    w, h = W * S, H * S
    c = rgb(accent)
    base = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    halo = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    hd = ImageDraw.Draw(halo)
    hd.rounded_rectangle((27*S, 25*S, (W-27)*S, (H-25)*S),
                         radius=48*S, fill=(*c, 60))
    halo = halo.filter(ImageFilter.GaussianBlur(19*S))
    base.alpha_composite(halo)
    d = ImageDraw.Draw(base)
    bg = (13, 18, 28, 238) if theme == "dark" else (248, 249, 252, 244)
    frame = c + (255,) if theme == "dark" else (35, 46, 60, 255)
    d.rounded_rectangle((13*S, 12*S, (W-13)*S, (H-12)*S),
                        radius=31*S, fill=bg, outline=frame, width=3*S)
    d.rounded_rectangle((21*S, 20*S, (W-21)*S, (H-20)*S),
                        radius=25*S,
                        outline=(*c, 58 if theme == "dark" else 45),
                        width=2*S)
    d.rounded_rectangle((31*S, 37*S, 39*S, (H-37)*S),
                        radius=4*S, fill=c + (255,))
    d.ellipse(((W-67)*S, 34*S, (W-53)*S, 48*S), fill=c + (235,))
    d.ellipse(((W-47)*S, 34*S, (W-40)*S, 41*S),
              fill=(255,255,255,166) if theme == "dark" else (60,70,85,155))
    size = 68 if len(label) < 9 else 52
    label_font = font(size*S)
    while d.textbbox((0, 0), label, font=label_font)[2] > (W-102)*S and size > 20:
        size -= 2
        label_font = font(size*S)
    text_color = (249,251,255,255) if theme == "dark" else (18,28,40,255)
    bb = d.textbbox((0, 0), label, font=label_font)
    x, y = 55*S, (43 if len(label) >= 9 else 38)*S
    d.text((x, y-bb[1]), label, font=label_font, fill=text_color)
    f2 = font(13*S, False)
    sub_color = (177,190,207,255) if theme == "dark" else (96,108,128,255)
    d.text((59*S, 124*S), sub, font=f2, fill=sub_color)
    return base.resize((W, H), Image.Resampling.LANCZOS)

def make_svg(stem, label, sub, accent, theme):
    from html import escape
    bg = "#0D121C" if theme == "dark" else "#F8F9FC"
    fg = "#F8FBFF" if theme == "dark" else "#121C28"
    frame = accent if theme == "dark" else "#232E3C"
    muted = "#B1BECF" if theme == "dark" else "#606C80"
    font_size = 60 if len(label) < 9 else 44
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="540" height="164" viewBox="0 0 540 164" role="img" aria-label="{escape(label)}">
  <defs><filter id="glow"><feGaussianBlur stdDeviation="7"/></filter></defs>
  <rect x="29" y="27" width="482" height="110" rx="31" fill="{accent}" opacity=".16" filter="url(#glow)"/>
  <rect x="13" y="12" width="514" height="140" rx="31" fill="{bg}" stroke="{frame}" stroke-width="3"/>
  <rect x="21" y="20" width="498" height="124" rx="25" fill="none" stroke="{accent}" stroke-opacity=".22" stroke-width="2"/>
  <rect x="31" y="37" width="8" height="90" rx="4" fill="{accent}"/>
  <circle cx="480" cy="40" r="7" fill="{accent}"/><circle cx="496" cy="37" r="3.5" fill="{fg}" opacity=".65"/>
  <text x="55" y="100" font-size="{font_size}" letter-spacing="-1.5" font-family="DejaVu Sans,Arial,sans-serif" font-weight="800" fill="{fg}">{escape(label)}</text>
  <text x="59" y="137" font-size="13" letter-spacing="1" font-family="Arial,sans-serif" fill="{muted}">{escape(sub)}</text>
</svg>
'''

def main():
    for theme in ("dark", "light"):
        folder = ROOT / "assets" / theme
        folder.mkdir(parents=True, exist_ok=True)
        for stem, label, sub, accent in BADGES:
            img = make_png(stem, label, sub, accent, theme)
            img.save(folder / (stem + ".png"), "PNG", optimize=True)
            (folder / (stem + ".svg")).write_text(
                make_svg(stem, label, sub, accent, theme), encoding="utf-8")
    print(f"Regenerated {len(BADGES) * 2} transparent PNG and {len(BADGES) * 2} SVG")

if __name__ == "__main__":
    main()
