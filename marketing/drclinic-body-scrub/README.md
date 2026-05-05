# Dr.Clinic Çilek Özlü Krem Peeling – Tanıtım Görselleri

Bu dizin, **Dr.Clinic Çilek Özlü Krem Peeling 300 ml** ürünü için hazırlanan sosyal medya tanıtım (promo) görsellerini ve kaynak dosyalarını içermektedir.

---

## Dosya Listesi

| Dosya | Boyut | Açıklama |
|---|---|---|
| `post-1080x1350.svg` | — | Instagram post kaynağı (düzenlenebilir SVG) |
| `post-1080x1350.png` | 1080 × 1350 px | Instagram post çıktısı (PNG) |
| `story-1080x1920.svg` | — | Instagram story kaynağı (düzenlenebilir SVG) |
| `story-1080x1920.png` | 1080 × 1920 px | Instagram story çıktısı (PNG) |
| `generate.py` | — | SVG → PNG dönüştürme betiği |

---

## Tasarım Bilgileri

### Boyutlar
| Format | Boyut | Oran | Kullanım |
|---|---|---|---|
| Instagram Post | 1080 × 1350 px | 4:5 | Feed paylaşımı |
| Instagram Story | 1080 × 1920 px | 9:16 | Hikaye / Reels kapak |

### Renk Paleti

| Renk Adı | HEX Kodu | Kullanım Yeri |
|---|---|---|
| Koyu Pembe (Ana) | `#C2185B` | Başlık çubuğu, CTA butonu, ikonlar |
| Koyu Vişne | `#880E4F` | Ürün ismi, kart başlıkları |
| Açık Pembe (Orta) | `#FF8FAB` | Dekoratif daireler, vurgular |
| Pastel Pembe | `#FFB3CA` | Arka plan blob'ları |
| Krem Zemin | `#FFF5F5` → `#FADDE6` | Arka plan gradyanı |
| Beyaz | `#FFFFFF` | Fayda kartları, jar görseli |
| Gri Metin | `#555555` / `#888888` | Açıklamalar, uyarı metni |

### Font Önerileri
Mevcut tasarımda sisteme bağımlı fontlar kullanılmaktadır. Premium bir çıktı için şu Google Fonts tercih edilebilir:

| Kullanım | Önerilen Font | Ağırlık |
|---|---|---|
| Marka adı / Başlıklar | **Playfair Display** (serif) | 700 Bold |
| Ürün ismi / Slogan | **Cormorant Garamond** (serif) | 600 SemiBold / Italic |
| Fayda kartları / CTA | **Montserrat** (sans-serif) | 700 Bold / 400 Regular |
| Uyarı metni | **Montserrat** (sans-serif) | 400 Regular, küçük punto |

Alternatif olarak sisteme dahil **Georgia** (serif) ve **Arial** (sans-serif) fontları mevcut SVG'de kullanılmaktadır.

### Metin İçerikleri (Düzeltilmiş Türkçe)

#### Başlık
```
ÇİLEK ÖZLÜ KREM PEELİNG
```

#### Slogan
```
Pürüzsüz & Canlı Cilt
```

#### Faydalar
1. **Kayısı Çekirdeği Tozu** – Ölü hücrelerden arındırır, pürüzsüz görünüm
2. **Panax Ginseng Kök Özü** – Antioksidan; cilde canlı görünüm kazandırır
3. **Gliserin + Hyaluronik Asit** – Yoğun nemlendirme, yumuşak ve esnek cilt
4. **Hoş Koku** – Cilt bakımını keyifli bir deneyime dönüştürür

#### Kullanım (Story'de yer alır)
```
Temiz ve nemli cilde dairesel hareketlerle uygulayın ve bol suyla durulayın.
```

#### CTA (Call to Action)
```
HAFTADA 2–3 KEZ KULLANIN
```

#### Uyarı Metni (küçük punto)
```
Harici kullanım içindir. Göz temasından kaçının.
Temas halinde bol su ile yıkayın.
Çocukların ulaşamayacağı ve serin yerde saklayın.
```

> **Not:** Orijinal metindeki yazım hataları düzeltildi:
> - "tızü" → "tozu"
> - "uygulayınve" → "uygulayın ve"

---

## Görselleri Yeniden Üretme

### Gereksinimler
```bash
pip install cairosvg pillow
```

### Çalıştırma
```bash
cd marketing/drclinic-body-scrub
python generate.py
```

Bu komut `post-1080x1350.svg` ve `story-1080x1920.svg` dosyalarını aynı dizinde **PNG** olarak dışa aktarır.

### Inkscape ile (alternatif)
```bash
inkscape --export-type=png --export-dpi=96 \
         --export-filename=post-1080x1350.png post-1080x1350.svg

inkscape --export-type=png --export-dpi=96 \
         --export-filename=story-1080x1920.png story-1080x1920.svg
```

---

## SVG'yi Düzenleme

`post-1080x1350.svg` ve `story-1080x1920.svg` dosyaları herhangi bir vektör düzenleyiciyle açılabilir:

- **Inkscape** (ücretsiz, önerilen): `inkscape post-1080x1350.svg`
- **Adobe Illustrator**: Dosyayı doğrudan sürükle-bırak ile açın
- **Figma**: "Import" menüsünden SVG dosyasını içe aktarın

Metin düzenlemek için `<text>` etiketlerini, renkler için `fill` özelliklerini, boyutlar için `width`/`height`/`viewBox` değerlerini değiştirin.

---

## Ürün Bilgisi

**Dr.Clinic Çilek Özlü Krem Peeling**
- Hacim: 300 ml
- Kategori: Vücut Peeling
- URL: https://www.drclinic.com.tr/urun/vucut-bakim/vucut-peeling/drclinic-cilek-ozlu-krem-peeling-300-ml
