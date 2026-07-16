# Evidence and source rules

## Resolve versions

- Match title, authors, and identifier before analysis.
- Record the inspected version and date. A later arXiv revision may differ from a conference version.
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
