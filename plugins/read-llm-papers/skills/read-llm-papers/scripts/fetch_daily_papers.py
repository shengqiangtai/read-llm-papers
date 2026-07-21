#!/usr/bin/env python3
"""Fetch and normalize Hugging Face Daily Papers metadata."""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


DEFAULT_API = "https://huggingface.co/api/daily_papers"
ARXIV_ID = re.compile(r"^\d{4}\.\d{4,5}(?:v\d+)?$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch structured Daily Papers data without parsing HTML."
    )
    parser.add_argument("--api-url", default=DEFAULT_API, help="Daily Papers JSON URL")
    parser.add_argument(
        "--input",
        type=Path,
        help="Read a saved API response instead of using the network",
    )
    parser.add_argument(
        "--format",
        choices=("json", "jsonl", "markdown"),
        default="json",
        help="Output format",
    )
    parser.add_argument(
        "--sort",
        choices=("api", "upvotes"),
        default="api",
        help="Keep API order or sort by upvotes descending",
    )
    parser.add_argument(
        "--limit",
        type=non_negative_int,
        default=0,
        help="Maximum records to emit; 0 keeps all records",
    )
    parser.add_argument("--timeout", type=positive_int, default=20)
    return parser.parse_args()


def non_negative_int(value: str) -> int:
    number = int(value)
    if number < 0:
        raise argparse.ArgumentTypeError("must be zero or greater")
    return number


def positive_int(value: str) -> int:
    number = int(value)
    if number <= 0:
        raise argparse.ArgumentTypeError("must be greater than zero")
    return number


def load_payload(args: argparse.Namespace) -> Any:
    if args.input:
        try:
            return json.loads(args.input.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise SystemExit(f"Could not read JSON input: {exc}") from exc

    request = urllib.request.Request(
        args.api_url,
        headers={
            "Accept": "application/json",
            "User-Agent": "read-llm-papers-skill/0.2",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=args.timeout) as response:
            return json.load(response)
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        raise SystemExit(f"Could not fetch Daily Papers JSON: {exc}") from exc


def first(entry: dict[str, Any], paper: dict[str, Any], key: str) -> Any:
    value = paper.get(key)
    return value if value not in (None, "") else entry.get(key)


def author_names(raw: Any) -> list[str]:
    if not isinstance(raw, list):
        return []
    names: list[str] = []
    for author in raw:
        if isinstance(author, dict) and author.get("name"):
            names.append(str(author["name"]))
        elif isinstance(author, str) and author:
            names.append(author)
    return names


def normalize(entry: Any) -> dict[str, Any]:
    if not isinstance(entry, dict):
        raise ValueError("each API record must be an object")
    paper = entry.get("paper") if isinstance(entry.get("paper"), dict) else {}
    paper_id = str(first(entry, paper, "id") or "").strip()
    if not paper_id:
        raise ValueError("paper record is missing an id")

    upvotes = first(entry, paper, "upvotes")
    try:
        upvotes = int(upvotes or 0)
    except (TypeError, ValueError):
        upvotes = 0

    return {
        "id": paper_id,
        "title": str(first(entry, paper, "title") or "").strip(),
        "authors": author_names(first(entry, paper, "authors")),
        "summary": str(first(entry, paper, "summary") or "").strip(),
        "upvotes": upvotes,
        "published_at": first(entry, paper, "publishedAt"),
        "submitted_on_daily_at": first(entry, paper, "submittedOnDailyAt"),
        "paper_url": f"https://huggingface.co/papers/{paper_id}",
        "arxiv_url": (
            f"https://arxiv.org/abs/{paper_id}" if ARXIV_ID.fullmatch(paper_id) else None
        ),
        "github_url": first(entry, paper, "githubRepo"),
        "project_url": first(entry, paper, "projectPage"),
    }


def markdown_escape(value: Any) -> str:
    return str(value or "").replace("|", "\\|").replace("\n", " ").strip()


def emit_markdown(records: list[dict[str, Any]]) -> None:
    print("| Title | Authors | Upvotes | Links |")
    print("| --- | --- | ---: | --- |")
    for record in records:
        links = [f"[HF]({record['paper_url']})"]
        for label, key in (("arXiv", "arxiv_url"), ("code", "github_url"), ("project", "project_url")):
            if record[key]:
                links.append(f"[{label}]({record[key]})")
        print(
            "| {title} | {authors} | {upvotes} | {links} |".format(
                title=markdown_escape(record["title"]),
                authors=markdown_escape(", ".join(record["authors"])),
                upvotes=record["upvotes"],
                links=" · ".join(links),
            )
        )


def main() -> None:
    args = parse_args()
    payload = load_payload(args)
    if not isinstance(payload, list):
        raise SystemExit("Daily Papers API response must be a JSON list")

    records: list[dict[str, Any]] = []
    for index, entry in enumerate(payload, start=1):
        try:
            records.append(normalize(entry))
        except ValueError as exc:
            raise SystemExit(f"Invalid record {index}: {exc}") from exc

    if args.sort == "upvotes":
        records.sort(key=lambda item: item["upvotes"], reverse=True)
    if args.limit:
        records = records[: args.limit]

    if args.format == "json":
        json.dump(records, sys.stdout, ensure_ascii=False, indent=2)
        print()
    elif args.format == "jsonl":
        for record in records:
            print(json.dumps(record, ensure_ascii=False))
    else:
        emit_markdown(records)


if __name__ == "__main__":
    main()
