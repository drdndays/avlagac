#!/usr/bin/env python3
"""
generate.py – SVG → PNG dönüştürücü
Dr.Clinic Çilek Özlü Krem Peeling tanıtım görselleri

Gereksinimler:
    pip install cairosvg pillow

Kullanım:
    python generate.py
"""

import os
import cairosvg

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FILES = [
    ("post-1080x1350.svg",  "post-1080x1350.png",  1080, 1350),
    ("story-1080x1920.svg", "story-1080x1920.png",  1080, 1920),
]

def main():
    for svg_name, png_name, width, height in FILES:
        svg_path = os.path.join(BASE_DIR, svg_name)
        png_path = os.path.join(BASE_DIR, png_name)

        print(f"Dönüştürülüyor: {svg_name} → {png_name}")
        cairosvg.svg2png(
            url=svg_path,
            write_to=png_path,
            output_width=width,
            output_height=height,
        )
        size_kb = os.path.getsize(png_path) // 1024
        print(f"  ✓ Kaydedildi: {png_path}  ({size_kb} KB)")

    print("\nTüm görseller başarıyla oluşturuldu.")

if __name__ == "__main__":
    main()
