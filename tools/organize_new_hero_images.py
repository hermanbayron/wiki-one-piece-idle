from pathlib import Path
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
IMG = ROOT / "images"


ordered_names = [
    "WhatsApp Image 2026-07-23 at 16.05.32.jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.33 (1).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.33 (2).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.33.jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.34.jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.41 (1).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.41.jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.42 (1).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.42 (2).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.42 (3).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.42 (4).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.42.jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.43 (1).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.43 (2).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.43 (3).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.43 (4).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.43.jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.44 (1).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.44 (2).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.44 (3).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.44 (4).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.44.jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.45 (1).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.45 (2).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.45 (3).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.45 (4).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.45.jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.46 (1).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.46 (2).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.46 (3).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.46.jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.47 (1).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.47 (2).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.47 (3).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.47 (4).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.47.jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.48 (1).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.48 (2).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.48 (3).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.48 (4).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.48.jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.49 (1).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.49 (2).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.49 (3).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.49.jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.50 (1).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.50 (2).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.50 (3).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.50 (4).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.50.jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.51 (1).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.51 (2).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.51 (3).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.51.jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.52 (1).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.52 (2).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.52 (3).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.52 (4).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.52.jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.53 (1).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.53 (2).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.53 (3).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.53.jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.54 (1).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.54 (2).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.54 (3).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.54 (4).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.54.jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.55 (1).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.55 (2).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.55 (3).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.55.jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.56 (1).jpeg",
    "WhatsApp Image 2026-07-23 at 16.05.56.jpeg",
]

targets = {
    1: ("aokiji", "skill-aokiji-fragility.jpeg"),
    2: ("aokiji", "skill-aokiji-ice-time.jpeg"),
    3: ("aokiji", "skill-aokiji-frost-blade.jpeg"),
    4: ("aokiji", "skill-aokiji-frigid-capsule.jpeg"),
    5: ("aokiji", "skill-aokiji-partisan.jpeg"),
    6: ("aokiji", "handbook-aokiji-comments.jpeg"),
    7: ("aokiji", "handbook-aokiji-recommendations.jpeg"),
    12: ("aokiji", "hero-aokiji-card-ur.jpeg"),
    8: ("sengoku", "skill-sengoku-powerful-shield.jpeg"),
    9: ("sengoku", "skill-sengoku-justice.jpeg"),
    10: ("sengoku", "skill-sengoku-top-command.jpeg"),
    11: ("sengoku", "skill-sengoku-deterrence-the-buddha.jpeg"),
    13: ("sengoku", "handbook-sengoku-recommendations.jpeg"),
    14: ("sengoku", "handbook-sengoku-comments.jpeg"),
    15: ("sengoku", "hero-sengoku-card-ur.jpeg"),
    17: ("sengoku", "skill-sengoku-the-buddha.jpeg"),
    16: ("caesar", "skill-caesar-candy-pill.jpeg"),
    18: ("caesar", "skill-caesar-candyman.jpeg"),
    19: ("caesar", "skill-caesar-fragile-illusion.jpeg"),
    20: ("caesar", "skill-caesar-slime-ball.jpeg"),
    21: ("caesar", "handbook-caesar-recommendations.jpeg"),
    22: ("caesar", "skill-caesar-candy-wall.jpeg"),
    23: ("caesar", "hero-caesar-card-ur.jpeg"),
    24: ("smoothie", "duplicate-smoothie-mana-slag.jpeg"),
    25: ("smoothie", "duplicate-smoothie-moisture-purify.jpeg"),
    26: ("smoothie", "duplicate-smoothie-stream-barrier.jpeg"),
    27: ("smoothie", "duplicate-smoothie-comments.jpeg"),
    28: ("smoothie", "duplicate-smoothie-moisture-sword.jpeg"),
    29: ("smoothie", "duplicate-smoothie-recommendations.jpeg"),
    30: ("smoothie", "duplicate-smoothie-comments-2.jpeg"),
    31: ("smoothie", "duplicate-smoothie-moisture-squeeze.jpeg"),
    32: ("tsuru", "skill-tsuru-traces-of-heart.jpeg"),
    33: ("tsuru", "skill-tsuru-wash-wash-fruit.jpeg"),
    34: ("tsuru", "skill-tsuru-mind-echo.jpeg"),
    35: ("tsuru", "skill-tsuru-mind-barrier.jpeg"),
    36: ("tsuru", "hero-tsuru-card-ur.jpeg"),
    37: ("tsuru", "handbook-tsuru-recommendations.jpeg"),
    38: ("tsuru", "handbook-tsuru-comments.jpeg"),
    39: ("tsuru", "hero-tsuru-alt-card-ur.jpeg"),
    40: ("tsuru", "handbook-tsuru-recommendations-2.jpeg"),
    41: ("tsuru", "skill-tsuru-mind-cleansing.jpeg"),
    42: ("tsuru", "skill-tsuru-mind-cleansing-duplicate.jpeg"),
    43: ("tsuru", "handbook-tsuru-comments-2.jpeg"),
    44: ("tsuru", "hero-tsuru-card-ur-2.jpeg"),
    45: ("shiki", "handbook-shiki-recommendations.jpeg"),
    46: ("shiki", "skill-shiki-deal-badge.jpeg"),
    47: ("shiki", "skill-shiki-gravity-blade.jpeg"),
    48: ("shiki", "skill-shiki-gravity-suppression.jpeg"),
    49: ("shiki", "skill-shiki-blood-dye.jpeg"),
    50: ("shiki", "hero-shiki-card-ur.jpeg"),
    51: ("moria", "skill-moria-shadow-clone.jpeg"),
    52: ("moria", "skill-moria-nightmare.jpeg"),
    53: ("moria", "skill-moria-doppleman.jpeg"),
    54: ("moria", "skill-moria-phantom-rock.jpeg"),
    55: ("moria", "handbook-moria-recommendations.jpeg"),
    56: ("moria", "handbook-moria-comments.jpeg"),
    57: ("moria", "hero-moria-card-ssr.jpeg"),
    58: ("law", "skill-law-dragon-rush.jpeg"),
    59: ("law", "skill-law-kage-shab.jpeg"),
    60: ("law", "skill-law-room.jpeg"),
    61: ("law", "skill-law-transplant.jpeg"),
    62: ("law", "skill-law-gamma-knife.jpeg"),
    63: ("law", "skill-law-death-shock.jpeg"),
    64: ("law", "handbook-law-comments.jpeg"),
    65: ("law", "hero-law-card-ssr.jpeg"),
    66: ("perona", "skill-perona-negative-bomb.jpeg"),
    67: ("perona", "skill-perona-negative-hollow.jpeg"),
    68: ("perona", "handbook-perona-recommendations.jpeg"),
    69: ("perona", "skill-perona-kage-ghost-claw.jpeg"),
    70: ("perona", "skill-perona-kage-ghost.jpeg"),
    71: ("perona", "handbook-perona-recommendations-2.jpeg"),
    72: ("perona", "skill-perona-ghost-ghost-boost.jpeg"),
    73: ("perona", "hero-perona-card-ssr.jpeg"),
    74: ("perona", "handbook-perona-comments.jpeg"),
}


def crop_icon(src: Path, dest: Path) -> None:
    if not src.exists():
        return
    with Image.open(src) as im:
        w, h = im.size
        crop = im.crop((int(w * 0.18), int(h * 0.19), int(w * 0.30), int(h * 0.25)))
        crop = crop.resize((160, 160))
        dest.parent.mkdir(parents=True, exist_ok=True)
        crop.save(dest, quality=88)


def main() -> None:
    for index, name in enumerate(ordered_names, start=1):
        src = IMG / name
        if not src.exists():
            continue
        hero, new_name = targets[index]
        dest_dir = IMG / "heroes" / hero
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest = dest_dir / new_name
        if dest.exists():
            src.unlink()
        else:
            src.rename(dest)

    icon_sources = {
        "aokiji-fragility": ("aokiji", "skill-aokiji-fragility.jpeg"),
        "aokiji-ice-time": ("aokiji", "skill-aokiji-ice-time.jpeg"),
        "aokiji-frost-blade": ("aokiji", "skill-aokiji-frost-blade.jpeg"),
        "aokiji-frigid-capsule": ("aokiji", "skill-aokiji-frigid-capsule.jpeg"),
        "aokiji-partisan": ("aokiji", "skill-aokiji-partisan.jpeg"),
        "sengoku-powerful-shield": ("sengoku", "skill-sengoku-powerful-shield.jpeg"),
        "sengoku-justice": ("sengoku", "skill-sengoku-justice.jpeg"),
        "sengoku-top-command": ("sengoku", "skill-sengoku-top-command.jpeg"),
        "sengoku-deterrence-the-buddha": ("sengoku", "skill-sengoku-deterrence-the-buddha.jpeg"),
        "sengoku-the-buddha": ("sengoku", "skill-sengoku-the-buddha.jpeg"),
        "caesar-slime-ball": ("caesar", "skill-caesar-slime-ball.jpeg"),
        "caesar-fragile-illusion": ("caesar", "skill-caesar-fragile-illusion.jpeg"),
        "caesar-candy-wall": ("caesar", "skill-caesar-candy-wall.jpeg"),
        "tsuru-mind-cleansing": ("tsuru", "skill-tsuru-mind-cleansing.jpeg"),
        "tsuru-traces-of-heart": ("tsuru", "skill-tsuru-traces-of-heart.jpeg"),
        "tsuru-wash-wash-fruit": ("tsuru", "skill-tsuru-wash-wash-fruit.jpeg"),
        "shiki-blood-dye": ("shiki", "skill-shiki-blood-dye.jpeg"),
        "shiki-gravity-blade": ("shiki", "skill-shiki-gravity-blade.jpeg"),
        "moria-nightmare": ("moria", "skill-moria-nightmare.jpeg"),
        "moria-shadow-clone": ("moria", "skill-moria-shadow-clone.jpeg"),
        "law-gamma-knife": ("law", "skill-law-gamma-knife.jpeg"),
        "law-room": ("law", "skill-law-room.jpeg"),
        "perona-kage-ghost": ("perona", "skill-perona-kage-ghost.jpeg"),
        "perona-negative-bomb": ("perona", "skill-perona-negative-bomb.jpeg"),
        "perona-ghost-ghost-boost": ("perona", "skill-perona-ghost-ghost-boost.jpeg"),
    }
    for icon, (hero, file_name) in icon_sources.items():
        crop_icon(IMG / "heroes" / hero / file_name, IMG / "heroes" / "skill-icons" / f"{icon}.jpg")

    for sheet in IMG.glob("_contact-2026-07-23-*.jpg"):
        sheet.unlink()


if __name__ == "__main__":
    main()
