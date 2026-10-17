from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont


WIDTH = 1200
HEIGHT = 630
ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "images" / "social-card.webp"


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(f"/System/Library/Fonts/Supplemental/{name}.ttf", size)


top = (207, 235, 248)
bottom = (246, 251, 254)
image = Image.new("RGB", (WIDTH, HEIGHT))
pixels = image.load()
for y in range(HEIGHT):
    ratio = y / (HEIGHT - 1)
    color = tuple(round(top[channel] * (1 - ratio) + bottom[channel] * ratio) for channel in range(3))
    for x in range(WIDTH):
        pixels[x, y] = color

sun = Image.new("RGBA", image.size, (0, 0, 0, 0))
sun_draw = ImageDraw.Draw(sun)
sun_draw.ellipse((805, -210, 1335, 320), fill=(244, 217, 168, 220))
sun = sun.filter(ImageFilter.GaussianBlur(70))
image = Image.alpha_composite(image.convert("RGBA"), sun)

draw = ImageDraw.Draw(image)
navy = (11, 42, 74, 255)
blue = (31, 143, 192, 255)
muted = (79, 106, 131, 255)

draw.text((72, 82), "NATURAL HEALING & HEALTH OPTIMIZATION", font=font("Georgia Bold", 24), fill=blue)
draw.text((70, 145), "The Art of", font=font("Georgia", 82), fill=navy)
optimal_font = font("Georgia Italic", 100)
draw.text((70, 238), "Optimal", font=optimal_font, fill=blue)
optimal_width = draw.textbbox((70, 238), "Optimal", font=optimal_font)[2] - 70
draw.text((70 + optimal_width + 22, 238), "Living", font=font("Georgia", 100), fill=navy)
draw.text((76, 390), "Learn how to live a longer and more optimal life.", font=font("Georgia", 34), fill=muted)

draw.rounded_rectangle((72, 500, 445, 566), radius=33, fill=navy)
draw.text((111, 516), "ARTOFOPTIMALLIVING.COM", font=font("Georgia Bold", 19), fill=(255, 255, 255, 255))

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
image.convert("RGB").save(OUTPUT, "WEBP", quality=86, method=6)
print(OUTPUT)
