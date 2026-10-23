#!/usr/bin/env python3
"""Check manifest, PNG alpha, dimensions, and SVG XML syntax."""
import json
import xml.etree.ElementTree as ET
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
info = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
assert info["schema"] == "liangyou-poster-badges/v1"
assert len(info["assets"]) == 12
total = 0
for badge in info["assets"]:
    for theme, paths in badge["files"].items():
        assert theme in ("dark", "light")
        png = ROOT / paths["png"]
        svg = ROOT / paths["svg"]
        assert png.is_file(), str(png)
        assert svg.is_file(), str(svg)
        with Image.open(png) as image:
            assert image.mode == "RGBA", (png, image.mode)
            assert image.size == (540, 164), (png, image.size)
            assert image.getpixel((0, 0))[3] == 0, (png, "corner should be transparent")
            assert image.getpixel((270, 75))[3] > 0, (png, "missing visible badge")
        e = ET.parse(svg).getroot()
        assert e.tag.endswith("svg") and e.attrib.get("viewBox") == "0 0 540 164"
        total += 1
assert (ROOT / "preview" / "index.html").is_file()
print(f"PASS: {total} PNG badges and {total} valid SVG sources")
