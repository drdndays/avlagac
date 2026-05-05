# Dr.Clinic Body Cream Scrub – Social Media Promo Visuals

Promotional assets for **Dr.Clinic Çilek Özlü Krem Peeling (Body Cream Scrub) 300 ml**.  
Covers Instagram Post and Story formats.

---

## Directory Structure

```
marketing/drclinic-body-cream-scrub/
├── post.png        # Instagram Post  – 1080 × 1350 px (exported PNG)
├── story.png       # Instagram Story – 1080 × 1920 px (exported PNG)
├── post.html       # Editable HTML/CSS source for the Post
├── story.html      # Editable HTML/CSS source for the Story
├── post.svg        # Standalone SVG source for the Post
├── story.svg       # Standalone SVG source for the Story
└── README.md       # This file
```

---

## Canvas Sizes

| Format          | Width | Height | Aspect Ratio |
|-----------------|-------|--------|-------------|
| Instagram Post  | 1080  | 1350   | 4:5         |
| Instagram Story | 1080  | 1920   | 9:16        |

---

## Colors

| Role                  | Hex       | Usage                                      |
|-----------------------|-----------|--------------------------------------------|
| Brand red (dark)      | `#c0112b` | Brand bar, CTA gradient start, headings    |
| Brand red (light)     | `#e8174a` | CTA gradient end, accent elements          |
| Strawberry pink       | `#ff6b8a` | Gradient accents, decorative elements      |
| Background pink       | `#fff0f3` | Page background / light half               |
| Background warm white | `#fff8f8` | Post background start                      |
| Dark maroon           | `#2a0a14` | Bottom bar, body text headings             |
| Dark maroon (mid)     | `#6b1a28` | Bottom bar gradient end                    |
| Muted rose            | `#7a3040` | Subheadings, secondary text                |
| Jar body pink         | `#ffb8cb` | Product jar illustration                   |

---

## Typography

| Role           | Font Family                          | Weight | Size (post) |
|----------------|--------------------------------------|--------|-------------|
| Brand name     | Poppins (fallback: Arial)            | 700    | 38 px       |
| Product title  | Playfair Display / Georgia (serif)   | 700    | 72 px       |
| Subtitle       | Poppins                              | 300    | 26 px       |
| Benefit heading| Poppins                              | 600    | 20 px       |
| Benefit body   | Poppins                              | 300    | 17 px       |
| Usage text     | Poppins                              | 300–700| 16 px       |
| CTA button     | Poppins                              | 700    | 22 px       |

Google Fonts URL used in HTML templates:
```
https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;1,400&family=Poppins:wght@300;400;600;700&display=swap
```

The SVG files use system-safe fallback fonts (`Poppins, 'Segoe UI', Arial, sans-serif`).

---

## Turkish Copy

### Product Name
- **Çilek Özlü Krem Peeling** (Body Cream Scrub)

### Benefits (3 key bullets)
1. Kayısı çekirdeği tozu ile cildi ölü hücrelerden arındırır; pürüzsüz ve yumuşak görünüm.
2. Panax ginseng kök özü antioksidan özelliği ile cilde canlı görünüm kazandırmaya yardımcı olur.
3. Gliserin ve hyaluronik asit ile nemlendirir. Hoş kokusuyla bakım keyifli.

### Usage Instructions
> Temiz ve nemli cilde dairesel hareketlerle masaj yaparak uygulayın ve bol suyla durulayın. **Haftada 2–3 kez.**

### Warning (short)
> Harici kullanım içindir. Göz ile temasından kaçının.

### CTA
> **Şimdi Keşfet**

---

## How to Regenerate PNGs

The PNGs are rendered from the HTML source files using headless Chromium.

### Requirements
- Google Chrome or Chromium installed

### Commands

**Instagram Post (1080×1350):**
```bash
google-chrome \
  --headless=new \
  --no-sandbox \
  --disable-gpu \
  --window-size=1080,1350 \
  --screenshot="post.png" \
  --hide-scrollbars \
  "file://$(pwd)/post.html"
```

**Instagram Story (1080×1920):**
```bash
google-chrome \
  --headless=new \
  --no-sandbox \
  --disable-gpu \
  --window-size=1080,1920 \
  --screenshot="story.png" \
  --hide-scrollbars \
  "file://$(pwd)/story.html"
```

Run both commands from the `marketing/drclinic-body-cream-scrub/` directory.

> **Note:** If using Docker or a headless environment, add `--disable-dev-shm-usage` to the flags.

---

## How to Edit

### HTML/CSS sources (`post.html`, `story.html`)
Open in any text editor or browser DevTools. Each file is self-contained:
- All styles are in the `<style>` block at the top.
- Text content is directly in the HTML body.
- Colors are defined as CSS variables/properties — search for `#c0112b` or `#e8174a` to update brand colors globally.

### SVG sources (`post.svg`, `story.svg`)
Open in:
- **Inkscape** (free, recommended) – full vector editing
- **Adobe Illustrator** – commercial
- **Figma** – import via File → Import
- Any text editor for direct markup changes

Key SVG elements to modify:
- `<text>` nodes → change copy directly
- `linearGradient` defs → update stop colors to change the palette
- `<rect>` / `<circle>` elements → adjust layout

---

## Design Notes

- **Layout:** Light pink/warm-white background for the post; split red-top / pink-bottom for the story.
- **Product illustration:** SVG jar with strawberry icon on the label (replace with actual product photo by swapping the `<g filter>` jar group with an `<image href="product.jpg" .../>` tag in the SVG, or an `<img>` tag in HTML).
- **Accents:** Strawberry emoji (🍓) used as decorative watermarks at low opacity.
- **Red brand bar:** Present at top (and bottom) of both formats.
- **Three benefits:** Always shown as icon + heading + body text.
- **Responsive:** The HTML templates are fixed-pixel (not responsive) to ensure pixel-perfect export.

### Replacing the product illustration with a real photo

**In HTML:**
```html
<!-- Replace the <div class="product-wrap">…</div> SVG with: -->
<div class="product-wrap">
  <img src="product.png" alt="Dr.Clinic Body Cream Scrub" style="width:440px;height:auto;object-fit:contain;">
</div>
```

**In SVG:**
```xml
<!-- Replace the jar <g> group with: -->
<image href="product.png" x="300" y="375" width="480" height="520"
       preserveAspectRatio="xMidYMid meet"/>
```
