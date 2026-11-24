"""One Sentence for a Traveler from 1800.

Writes a single sentence (at most 200 characters) to /output/entry.txt
explaining the modern internet to a time traveler from the year 1800.

The sentence is a fixed constant: no input is read, no randomness, no
clock, no network access, no file reads. Running this program twice
always produces byte-identical output.
"""

# The sentence builds on things a person of 1800 already knows -- the
# post office, roads, letters, ink -- and carries one comparison only:
# letters that travel the earth in a breath and are answered at once.
# It names "the internet" a single time, as the thing being explained.
TEXT = (
    "The internet is a post office whose roads run to towns all over "
    "the earth, so a letter you send arrives in a breath and its "
    "answer returns before your ink is dry."
)


def main() -> None:
    import os
    from pathlib import Path

    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
