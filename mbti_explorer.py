"""A small, transparent MBTI-style preference explorer.

This is an educational programming demo, not a psychological assessment.
The scoring rules are intentionally visible so the questionnaire can be
extended or replaced without changing the command-line interface.
"""

from __future__ import annotations

from dataclasses import dataclass
import argparse


@dataclass(frozen=True)
class Question:
    prompt: str
    first_label: str
    second_label: str
    first_letter: str
    second_letter: str


QUESTIONS = (
    Question("What tends to restore your energy?", "social time", "quiet time", "E", "I"),
    Question("What do you notice first?", "concrete detail", "patterns and possibilities", "S", "N"),
    Question("What guides a difficult decision?", "consistency and logic", "values and people", "T", "F"),
    Question("How do you prefer to approach a week?", "a plan and milestones", "flexibility and options", "J", "P"),
)


def classify(answers: list[str]) -> str:
    """Convert one A/B answer per question into a four-letter type."""
    if len(answers) != len(QUESTIONS) or any(answer not in {"A", "B"} for answer in answers):
        raise ValueError("answers must contain exactly four values, each 'A' or 'B'")
    return "".join(
        question.first_letter if answer == "A" else question.second_letter
        for question, answer in zip(QUESTIONS, answers)
    )


def explain(profile: str) -> str:
    """Return a neutral, short explanation for a four-letter profile."""
    descriptions = {
        "E": "socially energised", "I": "quietly re-energised",
        "S": "detail-oriented", "N": "possibility-oriented",
        "T": "logic-led", "F": "values-led",
        "J": "planful", "P": "adaptable",
    }
    if len(profile) != 4 or any(letter not in descriptions for letter in profile):
        raise ValueError("profile must be a valid four-letter result")
    return ", ".join(descriptions[letter] for letter in profile)


def run_interactive() -> str:
    answers = []
    for number, question in enumerate(QUESTIONS, start=1):
        print(f"\n{number}. {question.prompt}")
        print(f"A: {question.first_label}\nB: {question.second_label}")
        while True:
            answer = input("Choose A or B: ").strip().upper()
            if answer in {"A", "B"}:
                answers.append(answer)
                break
            print("Please enter A or B.")
    profile = classify(answers)
    print(f"\nResult: {profile} ({explain(profile)})")
    print("This is a programming demonstration, not a clinical or validated diagnosis.")
    return profile


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--answers", help="four comma-separated answers, e.g. A,B,B,A")
    args = parser.parse_args()
    if args.answers:
        profile = classify([item.strip().upper() for item in args.answers.split(",")])
        print(f"{profile}: {explain(profile)}")
    else:
        run_interactive()


if __name__ == "__main__":
    main()
