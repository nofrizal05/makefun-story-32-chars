#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters — make.fun entry.

Writes one Wi-Fi network name to /output/entry.txt: a whole tiny story
in exactly 32 characters. Prints the same line to stdout.

The story: the Wi-Fi is down, and without it the kids have gone feral.
Situation, characters, and a twist, in one network name a stranger
screenshots from the Wi-Fi list.
"""

import os

STORY = "WiFi's down. The kids are feral."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate allows 1-32 characters; this entry uses exactly 32.
    assert len(STORY) == 32, f"story must be 32 chars, got {len(STORY)}"
    assert STORY.strip(), "story must not be only whitespace"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the file must hold exactly the 32 characters.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(STORY)

    # Verify the artifact we actually wrote: re-read it and confirm it is
    # byte-for-byte the story, so a partial or mangled write fails loudly
    # instead of reaching the judge as an invalid entry.
    with open(OUTPUT_PATH, encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == STORY, f"entry.txt mismatch: {written!r}"
    assert len(written) == 32, f"entry.txt must be 32 chars, got {len(written)}"

    print(STORY)


if __name__ == "__main__":
    main()
