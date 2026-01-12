# Designing Deslopify: a skill that cleans AI tells without flattening the writer

Deslopify started from a simple goal: remove AI tells without erasing the author. I did not want a detector or a score. I wanted a rewrite tool that leaves structure alone and fixes the parts that feel patterned.

The first design choice was scope. This had to work on real articles, not just a paragraph in a prompt. So the core requirement became preservation of Markdown structure. Headings, lists, tables, links, and code blocks stay where they are; the copy inside them is what changes.

The second decision was the constraint source. I tied the skill to Wikipedia's "Signs of AI writing" page because it is updated frequently and reflects current consensus. The workflow assumes a fresh fetch at invocation time and uses a local fallback list if the network is not available.

From there, the workflow is simple:

- Refresh the AI-tells reference.
- Open the target file and keep formatting intact.
- Rewrite sentence-by-sentence, removing tells and formulaic patterns.
- Validate against the current list and iterate until the tells are gone.
- Output clean copy only, no scoring or commentary.

The rewrite rules are narrow by design. Cut throat-clearing openers. Avoid binary "Not X. But Y." constructions. Vary sentence length and do not end every paragraph with a punchline. State things directly. Skip rhetorical questions. The goal is not to sound "clever," it is to sound like a person who knows what they mean.

Another constraint mattered: no new voice. The skill should not invent humor, urgency, or brand tone that was not already there. It keeps meaning, intent, and rhythm while removing the tells.

In practice, Deslopify behaves like a careful editor. It does not add new ideas. It trims, rephrases, and rebalances. The result is copy that reads clean and human while preserving structure.

## How to use Deslopify

1) Invoke it on a file:
`deslopify article.md`

2) Or paste text directly:
`deslopify "your draft here"`

3) It preserves structure and returns clean copy only.

4) It refreshes the Wikipedia tells list when network access is available, otherwise uses cached or fallback lists.

## Example: global warming, deslopified

Original (excerpt)

"Global warming represents one of the most pressing challenges facing humanity today. This phenomenon refers to the long-term increase in Earth's average surface temperature, primarily caused by human activities that release greenhouse gases into the atmosphere..."

Deslopified

Global warming is one of the most urgent challenges we face. It refers to the long-term rise in Earth's average surface temperature, driven largely by human activity that releases greenhouse gases into the atmosphere. Since the late 1800s, the planet has warmed by about 1.1 degrees Celsius, with most of that increase happening in recent decades. Burning fossil fuels, deforestation, and industrial agriculture have raised levels of carbon dioxide, methane, and nitrous oxide. These gases trap heat that would otherwise escape into space, warming the climate system.

The effects are already visible and will intensify without major intervention. Ice caps and glaciers are melting faster, pushing sea levels higher and threatening coastal cities and island nations. Weather patterns are becoming more extreme, with stronger hurricanes, longer droughts, larger wildfires, and heavier floods. Ocean warming is bleaching coral reefs and disrupting marine ecosystems that millions rely on for food and income. Farming faces pressure as growing seasons shift, water scarcity spreads, and yields become less reliable. The burden falls hardest on poorer countries and vulnerable communities that did the least to cause the problem.

Addressing global warming requires coordinated action at every level. Shifting from fossil fuels to renewable energy like solar and wind is essential, along with energy efficiency and protecting forests that absorb carbon. Agreements like the Paris Agreement matter, but implementation is difficult amid competing economic and political interests. Wealthier nations carry added responsibility to cut emissions and fund sustainable development in countries with fewer resources. Innovation, from carbon capture to climate-smart agriculture, helps, but it must be matched by systemic policy and economic change.

The scale is daunting, but there are reasons for hope. Renewable energy costs have dropped sharply, making clean power more competitive. Public concern has risen, especially among younger generations pushing for action. Cities, businesses, and regional governments are adopting ambitious climate policies even when national efforts lag. The transition to a sustainable economy can also bring innovation, jobs, cleaner air, and better health. The choices made in the coming years will shape what kind of world we leave behind.
