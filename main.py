#!/usr/bin/env python3
"""One Word for Your Wi-Fi.

Writes a single word describing home Wi-Fi to /output/entry.txt.
Deterministic: the same word on every run, no network, no randomness.

The word is "Gaslighting": the router insists it is connected, full bars,
while nothing loads. It says the connection is fine; your eyes, your video
call and your download all disagree. Funny at once, painfully true of home
Wi-Fi, a fresh angle nobody reaches for first, and it works as a Wi-Fi
network name with no context needed. 11 characters, inside the gate's
1-20 character limit.
"""

import os

WORD = "Gaslighting"


def main() -> None:
    # Gate check, same rule the sealed scorer applies: UTF-8 text of
    # 1 to 20 characters, not only white space.
    assert 1 <= len(WORD) <= 20 and WORD.strip(), "word fails the gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
