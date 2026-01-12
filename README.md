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

### Install the skill

#### Codex
1. Copy the skill folder into your Codex skills directory:
   ```bash
   mkdir -p ~/.codex/skills
   cp -R skills/deslopify ~/.codex/skills/deslopify
   ```
2. Restart Codex so it picks up the new skill.

#### Claude
1. Copy the skill folder into the skills directory that Claude is configured to read.
2. If your Claude setup supports `.skill` bundles, you can copy `deslopify.skill` into that same directory instead.
3. Restart Claude to load the skill.

#### GitHub Copilot
1. Copy the skill folder into the skills directory that Copilot is configured to read.
2. If your Copilot setup supports `.skill` bundles, you can copy `deslopify.skill` instead.
3. Restart Copilot so it detects the new skill.

### Invoke the skill
- Prompt examples:
  - `deslopify article.md`
  - `deslopify this draft and keep headings as-is`

### Update the AI tells list
```bash
python3 skills/deslopify/scripts/fetch_wikipedia_ai_tells.py
```
If the fetch fails (offline or blocked), it falls back to the cached `skills/deslopify/references/ai_tells.wikitext`. If the cache is missing, it uses `skills/deslopify/references/ai_tells_fallback.txt`.
