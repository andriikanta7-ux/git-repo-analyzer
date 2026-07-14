import sys
import os
import json

from github_skill import get_repository_context
from llm_analyzer import analyze_repository


def main():

    if len(sys.argv) != 3:
        print("Usage: python3 main.py <owner> <repository>")
        return

    owner = sys.argv[1]
    repo = sys.argv[2]

    print("Getting repository...")

    context = get_repository_context(
        owner,
        repo
    )

    print("Analyzing with Gemini...")

    result = analyze_repository(
        context
    )

    os.makedirs(
        "output",
        exist_ok=True
    )

    with open(
        "output/report.md",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
    f"""
# Repository Analysis

## Summary
{result['summary']}

## Technologies
{', '.join(result['technologies'])}

## Strengths
{chr(10).join('- ' + x for x in result['strengths'])}

## Issues
{chr(10).join('- ' + x for x in result['issues'])}

## Recommendations
{chr(10).join('- ' + x for x in result['recommendations'])}
"""
)

    with open(
        "output/analysis.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            result,
            file,
            indent=4,
            ensure_ascii=False
        )

    print("Done!")


if __name__ == "__main__":
    main()