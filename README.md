## deslopify

Deslopify is an agent-neutral skill (Agent Skills format) that rewrites AI-sounding prose into more human copy while preserving the original Markdown structure. It is compatible with any agent or tool that supports `SKILL.md` skills (e.g., Codex, Copilot, Claude).

### Use cases
- Clean up AI-written articles or blog posts.
- Make LLM drafts sound less formulaic before publishing.
- Preserve headings, lists, and formatting while improving tone.

### Example

Input (`article.md`):
```markdown
# Product Clarity

Here's the thing: building great products is hard. Let that sink in.
```

Output:
```markdown
# Product Clarity

Building great products is hard. Most teams feel it early.
```

### How it deslopifies
- Fetches the current Wikipedia "Signs of AI writing" list (with an offline fallback).
- Rewrites sentence-by-sentence to remove AI tells and formulaic patterns.
- Preserves meaning, structure, and formatting.

### Invoke the skill
- Prompt examples:
  - `deslopify article.md`
  - `deslopify this draft and keep headings as-is`

### Update the AI tells list
```bash
python3 skills/deslopify/scripts/fetch_wikipedia_ai_tells.py
```
