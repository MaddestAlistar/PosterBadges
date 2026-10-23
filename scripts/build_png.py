#!/usr/bin/env python3
"""Regenerate transparent badge PNGs from badges.json (requires Pillow)."""
import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
ROOT=Path(__file__).resolve().parents[1]
items=json.loads((ROOT/'badges.json').read_text(encoding='utf-8'))['badges']

def color(value):return tuple(int(value[i:i+2],16) for i in (1,3,5))
def getfont(size,bold=True):
 for f in ('DejaVuSans-Bold.ttf' if bold else 'DejaVuSans.ttf','Arial.ttf'):
  try:return ImageFont.truetype(f,size)
  except OSError:pass
 return ImageFont.load_default()

for theme in ('dark','light'):
 dark=theme=='dark'
 out=ROOT/'assets'/theme
 out.mkdir(parents=True,exist_ok=True)
 for b in items:
  accent=color(b['color']); w,h=640,200
  base=Image.new('RGBA',(w,h),(0,0,0,0))
  halo=Image.new('RGBA',(w,h),(0,0,0,0));ha=ImageDraw.Draw(halo)
  ha.rounded_rectangle((27,21,w-27,h-21),radius=43,fill=(*accent,50))
  base.alpha_composite(halo.filter(ImageFilter.GaussianBlur(17)))
  d=ImageDraw.Draw(base)
  d.rounded_rectangle((14,12,w-14,h-12),radius=38,fill=(13,18,28,246) if dark else (249,250,253,246),outline=(*accent,255) if dark else (46,57,70,255),width=4)
  d.rounded_rectangle((23,21,w-23,h-21),radius=30,outline=(*accent,80),width=2)
  d.rounded_rectangle((36,43,48,h-43),radius=5,fill=(*accent,255))
  title=b['label'];size=82 if len(title)>9 else 100
  ft=getfont(size)
  while d.textbbox((0,0),title,font=ft)[2]>w-160 and size>25:
   size-=3;ft=getfont(size)
  box=d.textbbox((0,0),title,font=ft)
  d.text((68,51-box[1]),title,font=ft,fill=(250,252,255,255) if dark else (20,33,49,255))
  d.text((72,145),b['caption'],font=getfont(20,False),fill=(183,195,210,255) if dark else (99,115,132,255))
  d.ellipse((573,44,591,62),fill=(*accent,255))
  base.resize((320,100),Image.Resampling.LANCZOS).save(out/(b['id']+'.png'),optimize=True)
print('Built',len(items)*2,'transparent PNGs')
