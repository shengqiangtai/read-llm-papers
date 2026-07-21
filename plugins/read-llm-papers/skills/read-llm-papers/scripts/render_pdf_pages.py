#!/usr/bin/env python3
"""Render selected PDF pages to PNG for visual evidence checks."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
from pathlib import Path
from typing import Any


def positive_int(value: str) -> int:
    number = int(value)
    if number <= 0:
        raise argparse.ArgumentTypeError("must be greater than zero")
    return number


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render PDF pages as PNG images.")
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--pages", default="all", help="1-based pages such as 2,5-7 or all")
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--dpi", type=positive_int, default=150)
    parser.add_argument("--overwrite", action="store_true")
    return parser.parse_args()


def parse_pages(spec: str, total: int) -> list[int]:
    if spec.strip().lower() == "all":
        return list(range(1, total + 1))

    pages: set[int] = set()
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            start_text, end_text = part.split("-", 1)
            if not start_text.isdigit() or not end_text.isdigit():
                raise SystemExit(f"Invalid page range: {part}")
            start, end = int(start_text), int(end_text)
            if start > end:
                raise SystemExit(f"Page range runs backward: {part}")
            pages.update(range(start, end + 1))
        elif part.isdigit():
            pages.add(int(part))
        else:
            raise SystemExit(f"Invalid page value: {part}")

    if not pages:
        raise SystemExit("No pages selected")
    invalid = sorted(page for page in pages if page < 1 or page > total)
    if invalid:
        raise SystemExit(f"Page outside PDF range 1-{total}: {invalid[0]}")
    return sorted(pages)


def target_path(output_dir: Path, page: int, overwrite: bool) -> Path:
    target = output_dir / f"page-{page:04d}.png"
    if target.exists() and not overwrite:
        raise SystemExit(f"Output exists; pass --overwrite to replace it: {target}")
    return target


def load_pymupdf() -> Any | None:
    try:
        import fitz  # type: ignore
    except ImportError:
        return None
    return fitz


def render_with_pymupdf(
    fitz: Any,
    pdf: Path,
    output_dir: Path,
    page_spec: str,
    dpi: int,
    overwrite: bool,
) -> list[Path]:
    outputs: list[Path] = []
    with fitz.open(str(pdf)) as document:
        pages = parse_pages(page_spec, document.page_count)
        scale = dpi / 72.0
        matrix = fitz.Matrix(scale, scale)
        for page_number in pages:
            target = target_path(output_dir, page_number, overwrite)
            page = document.load_page(page_number - 1)
            page.get_pixmap(matrix=matrix, alpha=False).save(str(target))
            outputs.append(target)
    return outputs


def poppler_page_count(pdf: Path) -> int:
    pdfinfo = shutil.which("pdfinfo")
    if not pdfinfo:
        raise SystemExit("Poppler fallback needs both pdfinfo and pdftoppm")
    result = subprocess.run(
        [pdfinfo, str(pdf)],
        check=True,
        capture_output=True,
        text=True,
    )
    match = re.search(r"^Pages:\s+(\d+)\s*$", result.stdout, flags=re.MULTILINE)
    if not match:
        raise SystemExit("Could not determine PDF page count with pdfinfo")
    return int(match.group(1))


def render_with_poppler(
    pdf: Path,
    output_dir: Path,
    page_spec: str,
    dpi: int,
    overwrite: bool,
) -> list[Path]:
    pdftoppm = shutil.which("pdftoppm")
    if not pdftoppm:
        raise SystemExit("Install PyMuPDF or Poppler to render PDF pages")
    pages = parse_pages(page_spec, poppler_page_count(pdf))
    outputs: list[Path] = []
    for page_number in pages:
        target = target_path(output_dir, page_number, overwrite)
        prefix = target.with_suffix("")
        subprocess.run(
            [
                pdftoppm,
                "-f",
                str(page_number),
                "-l",
                str(page_number),
                "-singlefile",
                "-r",
                str(dpi),
                "-png",
                str(pdf),
                str(prefix),
            ],
            check=True,
        )
        outputs.append(target)
    return outputs


def main() -> None:
    args = parse_args()
    pdf = args.pdf.expanduser().resolve()
    if not pdf.is_file():
        raise SystemExit(f"PDF not found: {pdf}")

    output_dir = (
        args.output_dir.expanduser().resolve()
        if args.output_dir
        else pdf.with_name(f"{pdf.stem}-pages")
    )
    output_dir.mkdir(parents=True, exist_ok=True)

    fitz = load_pymupdf()
    if fitz is not None:
        outputs = render_with_pymupdf(
            fitz, pdf, output_dir, args.pages, args.dpi, args.overwrite
        )
        backend = "PyMuPDF"
    else:
        outputs = render_with_poppler(
            pdf, output_dir, args.pages, args.dpi, args.overwrite
        )
        backend = "Poppler"

    print(f"Rendered {len(outputs)} page(s) with {backend}:")
    for output in outputs:
        print(output)


if __name__ == "__main__":
    main()
