import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PATTERNS = [
    re.compile(r"""(?:src|href)\s*=\s*["']([^"']+\.(?:jpeg|jpg|png|webp|css|js))["']"""),
    re.compile(r"""(?:image|portrait|icon):\s*["'](images/[^"']+\.(?:jpeg|jpg|png|webp))["']"""),
]


def main() -> int:
    missing = []
    for page in ROOT.glob("*.html"):
        text = page.read_text(encoding="utf-8")
        for pattern in PATTERNS:
            for match in pattern.finditer(text):
                ref = match.group(1)
                if ref.startswith(("http", "#", "mailto:")):
                    continue
                if not (ROOT / ref).exists():
                    missing.append((page.name, ref))

    if missing:
        for page, ref in missing:
            print(f"{page}: missing {ref}")
        return 1

    print("asset refs ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
