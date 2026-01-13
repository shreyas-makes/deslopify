---
name: deslopify
description: Rewrite AI-sounding prose into more human, natural copy while preserving existing Markdown structure and formatting. Use when asked to "deslopify" or clean AI-written articles/blog posts and when removing AI tells, formulaic phrasing, or predictable rhetorical patterns based on the current Wikipedia "Signs of AI writing" list.
---

# Deslopify

## Overview

Rewrite prose to read human while keeping the original structure, headings, lists, and formatting intact. Use the current Wikipedia list of AI tells as a dynamic constraint to avoid. Aim for more generative, creative phrasing (higher variation and lexical diversity) without changing facts or structure.

## Workflow

### 1. Refresh the AI-tells reference

Always run the fetch script at the start of the skill to keep the AI-tells list current. It will refresh `references/ai_tells.wikitext` when network access is available:

```bash
python3 scripts/fetch_wikipedia_ai_tells.py
```

If the fetch fails or the user forbids network access, the script should fall back to the existing `references/ai_tells.wikitext` cache. If that file does not exist, use the local fallback list in `references/ai_tells_fallback.txt` and mention it may be stale.

### 2. Load the article and preserve structure

Open the referenced file (e.g., `article.md`). Keep all Markdown structure and formatting:

- Headings, lists, tables, links, code blocks, and blockquotes stay in place.
- Do not change the outline or reorder sections unless the user asks.
- Hard no-touch content: code blocks, quoted text, URLs, link text, numbers, citations/footnotes.

### 3. Deslopify the copy (creative pass)

Rewrite sentence-by-sentence and paragraph-by-paragraph, keeping meaning and intent but removing AI tells. Favor higher-entropy choices and fresh phrasing that still fits the source tone:

- Cut throat-clearing openers, dramatic pivots, and filler.
- Avoid formulaic contrasts (e.g., "Not X. But Y.") and cadence-heavy punchlines.
- Vary sentence lengths; do not default to rhythmic triads.
- Prefer direct statements over rhetorical questions and self-answering.
- Keep tone consistent with the source; do not inject a new voice.
- Reach for vivid but accurate verbs and concrete nouns when they clarify, not embellish.
- Allow occasional mild metaphor or sensory phrasing if it feels native to the original.
- Avoid safe paraphrase; choose distinctive alternatives that still read natural.

### 4. Validate against the Wikipedia tells

Scan the output against the latest `references/ai_tells.wikitext` list and remove any matching patterns or stylistic cues. If a tell appears unavoidable, rewrite again until the tell is gone.

Optional: run the linter to catch common AI-tell phrases in the output draft:

```bash
python3 scripts/lint_ai_tells.py <draft.md>
```

### 5. Deliver clean output

Return the revised content only. Do not include a score or commentary unless the user requests it.

## Guidance

- Preserve facts and claims; only adjust phrasing and rhythm.
- Keep lists concise; two items often beat three.
- Avoid meta phrases like "let that sink in" or "here's the thing."
- End paragraphs in varied ways; avoid the final punchline cadence.
- Use a slightly higher-variance word choice; avoid bland neutrality.
