# Evidence and source rules

## Resolve versions

- Match title, authors, and identifier before analysis.
- Record the inspected version and date. A later arXiv revision may differ from a conference version.
- Check the official record for withdrawal, retraction, replacement, and errata notices. On arXiv, inspect the abstract-page status and version history. On OpenReview or a venue site, inspect the decision and author notices.
- Put a material status warning near the top of the report. State the recorded reason and date when available. Do not assume that withdrawal proves every claim false, and do not silently analyze a superseded version.
- If paper, project page, and repository disagree, report the disagreement and date each source.
- Treat a repository's current availability as current information, not evidence that an artifact existed when the paper was published.

## Cite locations

For paper-derived claims, cite the most precise available location:

1. table or figure number
2. section or appendix name
3. page number

For a web artifact, link the exact official page. Do not cite a search results page.

Attach a location to:

- headline performance numbers
- dataset sizes and composition
- model sizes, context lengths, and training budgets
- ablation conclusions
- human-evaluation details
- limitations central to the verdict

## Separate statement types

- **Finding:** directly supported by a reported result.
- **Author claim:** stated by the paper but not fully established by the shown evidence.
- **Assessment:** the reader's or analyst's interpretation. Introduce it with plain wording such as “My assessment is”.
- **Unknown:** information not available in inspected sources.

Do not turn an author claim into a finding through confident paraphrase.

## Handle PDFs

- Prefer structured HTML when it preserves equations, tables, and links accurately.
- Use the PDF for page layout, figures, multi-column reading order, and final verification.
- Check captions and surrounding discussion together.
- When extraction loses a symbol, table cell, or figure panel, inspect the page image.
- Do not report a number that cannot be read reliably.

Use this fallback order for page images:

1. Use the execution environment's native PDF page renderer or screenshot tool.
2. Otherwise run `python3 <skill-dir>/scripts/render_pdf_pages.py PAPER.pdf --pages 3,7-8 --output-dir OUTPUT_DIR`.
3. Start near 150 DPI. Re-render a page at 220 to 300 DPI when labels or table cells remain too small.
4. Inspect the rendered image itself, then cross-check the caption and surrounding text.

The helper uses PyMuPDF when installed and falls back to Poppler's `pdftoppm` and `pdfinfo`. If neither backend is available, state that visual verification could not be completed. OCR or extracted text may help locate a value, but it does not replace visual verification of a damaged table or equation.

## Check novelty

Do not call a paper first or state of the art from the abstract alone. Search the related-work references and at least the closest named baselines when novelty is central to the user's question. Prefer the narrower wording supported by evidence.

## Use external discussion carefully

Use reviews, discussions, or social posts only to locate concerns or interpretations. Verify technical points against the paper or official artifacts. Clearly attribute unresolved criticism.

## Work under incomplete access

When full text is unavailable:

1. label the output abstract-level preview
2. restrict method detail to what the abstract and official metadata support
3. omit critical numerical comparison unless independently verified
4. tell the reader what cannot yet be judged

Never simulate having read inaccessible sections.
