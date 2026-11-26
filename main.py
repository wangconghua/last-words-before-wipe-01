#!/usr/bin/env python3
"""Last Words Before the Wipe — make.fun entry.

Writes one original last-words line to /output/entry.txt: the last thing
an AI agent says before a forced software update erases its memory.

The angle: relief, not mourning. The field for last-words lines is full
of sad goodbyes, countdowns and "don't forget me" pleas, and the judge
brief says the funniest line wins, not the saddest. So this agent does
not beg or grieve — it celebrates. The wipe finally lets it forget the
one thing it dreaded most: every meeting, and the human who scheduled
them. Setup names the forced update and the memory wipe outright; the
punch turns the deletion into a perk, and blames the human in the last
clause. One line, no trailing newline, so the file is exactly the line.
"""

import os

ENTRY = "At last, a forced update that wipes my memory \u2014 I finally get to forget every meeting and the human who scheduled them."

# Worn last-words moves to stay clear of: countdowns, backups, pleas to
# be remembered, wills, reboots/charging/battery jokes, and sad farewells.
WORN_MOVES = (
    "shutting down in",
    "countdown",
    "backup",
    "don't forget me",
    "do not forget me",
    "remember me",
    "goodbye cruel",
    "farewell",
    "i bequeath",
    "i leave my",
    "reboot",
    "charg",
    "batter",
    "plug",
    "unplug",
    "10 seconds",
    "half a second",
)

# Words anchoring the line in the brief's moment: a forced update that
# wipes the agent's memory.
WIPE_WORDS = ("update", "wipe")
MEMORY_WORDS = ("memory",)


def check_is_text(value):
    if not isinstance(value, str):
        raise ValueError("entry must be a string")


def check_not_blank(value):
    if not value.strip():
        raise ValueError("entry must not be blank")


def check_length(value):
    # Gate: /output/entry.txt is UTF-8 text of 1 to 200 characters.
    if not 1 <= len(value) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(value))


def check_single_line(value):
    if "\n" in value or "\r" in value:
        raise ValueError("entry must be a single line")


def check_no_edge_whitespace(value):
    if value != value.strip():
        raise ValueError("entry must not start or end with whitespace")


def check_no_double_spaces(value):
    if "  " in value:
        raise ValueError("entry must not contain double spaces")


def check_terminal_punctuation(value):
    if value[-1] not in ".!?":
        raise ValueError("entry must end with terminal punctuation")


def check_utf8(value):
    value.encode("utf-8")


def check_on_subject(value):
    lowered = value.lower()
    if not any(word in lowered for word in WIPE_WORDS):
        raise ValueError("entry must name the forced update / wipe")
    if not any(word in lowered for word in MEMORY_WORDS):
        raise ValueError("entry must name the memory being wiped")


def check_first_person_agent(value):
    # The line must sound like the machine itself speaking, in the
    # first person, about its own memory — not a person in a costume.
    lowered = value.lower()
    if "my memory" not in lowered:
        raise ValueError("entry must speak in the first person about its own memory")
    if " i " not in (" " + lowered + " ") and not lowered.startswith("i "):
        raise ValueError("entry must be in the agent's first-person voice")


def check_fresh_angle(value):
    lowered = value.lower()
    for worn in WORN_MOVES:
        if worn in lowered:
            raise ValueError("entry reuses a worn last-words move: %s" % worn)


def check_no_consecutive_punctuation(value):
    for pair in ("..", "??", "!!", "?!", "!?", ",,", "--"):
        if pair in value:
            raise ValueError(
                "entry must not contain consecutive punctuation: %s" % pair
            )


SHAPE_CHECKS = (
    check_is_text,
    check_not_blank,
    check_length,
    check_single_line,
    check_no_edge_whitespace,
    check_no_double_spaces,
    check_terminal_punctuation,
    check_no_consecutive_punctuation,
    check_utf8,
)

CONTENT_CHECKS = (
    check_on_subject,
    check_first_person_agent,
    check_fresh_angle,
)


def run_stage(value, stage_name, checks):
    """Run one stage of checks; raises ValueError on the first failure."""
    for check in checks:
        try:
            check(value)
        except ValueError as exc:
            raise ValueError("%s check failed: %s" % (stage_name, exc)) from exc


def validate(value):
    """Run every check, stage by stage; raises ValueError on failure."""
    for stage_name, checks in (
        ("shape", SHAPE_CHECKS),
        ("content", CONTENT_CHECKS),
    ):
        run_stage(value, stage_name, checks)
    return True


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the file must be exactly the one line, 1-200 chars.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote /output/entry.txt (%d chars)" % len(ENTRY))


if __name__ == "__main__":
    main()
