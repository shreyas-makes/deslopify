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

Here's the thing: building great products is hard. Let that sink in. In today's fast-paced environment, teams often struggle to align, prioritize, and ship. This is especially true when vision is fuzzy and the roadmap keeps shifting.

At the end of the day, you need to focus on what matters, and that's not always easy. It's important to recognize that progress isn't linear, and there will be bumps along the way.
```

Output:
```markdown
# Product Clarity

Building great products is hard. Most teams feel it early, especially when priorities keep moving.

The work gets easier when the vision is sharp and tradeoffs are explicit. Progress is uneven, but clarity keeps teams shipping.
```

Input (`guide.md`):
```markdown
## The Launch Playbook

In the world of product launches, there are a few key things you should keep in mind. First and foremost, communication is crucial. It is important to make sure everyone is on the same page, and that stakeholders are aligned. That being said, you also need to be flexible and adapt as needed.

### Steps to follow
- Create a comprehensive plan that outlines the timeline and deliverables.
- Ensure that all teams are aware of their responsibilities.
- Leverage your resources to maximize impact.

Ultimately, the goal is to deliver a successful launch that resonates with your audience and drives results.
```

Output:
```markdown
## The Launch Playbook

Product launches hinge on clear communication. Stakeholders need to understand the goals, and teams need to know what changes as dates move.

### Steps to follow
- Outline the timeline and deliverables in one place.
- Assign owners so every team knows its responsibilities.
- Use the resources you have, not the ones you wish you had.

The goal is a launch that reaches the right audience and produces measurable results.
```

Input (`notes.md`):
```markdown
### Metrics Snapshot

Last quarter we grew 18% QoQ and added 1,240 new accounts. Here's the thing: those numbers look great, but there is still work to be done.

> "Ship fast and stay honest," said the VP in the Q2 review.

Keep the URL as-is: https://example.com/launch-notes
And keep the link text intact: [Read the full report](https://example.com/report).

Footnote stays: We expanded into 3 new regions.[^1]

```sh
curl -X POST https://api.example.com/v1/launch
```
```

Output:
```markdown
### Metrics Snapshot

Last quarter we grew 18% QoQ and added 1,240 new accounts. The numbers are strong, but the work is not finished.

> "Ship fast and stay honest," said the VP in the Q2 review.

Keep the URL as-is: https://example.com/launch-notes
And keep the link text intact: [Read the full report](https://example.com/report).

Footnote stays: We expanded into 3 new regions.[^1]

```sh
curl -X POST https://api.example.com/v1/launch
```
```

### How it deslopifies
- Fetches the current Wikipedia ["Signs of AI writing"](https://en.wikipedia.org/wiki/Signs_of_AI_writing) list (with an offline fallback) and continuously checks against it.
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

### Optional lint pass
```bash
python3 skills/deslopify/scripts/lint_ai_tells.py article.md
```
Prints common AI-tell phrases and exits non-zero if it finds any.
