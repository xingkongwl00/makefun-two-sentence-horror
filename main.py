from pathlib import Path

"""Two-sentence horror story for a make.fun bounty."""

JOKE = "Draft: two-sentence horror story pending final review."

OUTPUT_DIR = Path("/output")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
(OUTPUT_DIR / "entry.txt").write_text(JOKE, encoding="utf-8")
