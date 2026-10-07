---
this_file: prompts/index.md
---

# Prompts

Not every tool installs skills. These prompts carry the same rules into any
chat: copy one, paste it, then add the brief, the evidence and any draft.

Each page has two variants. The short one carries the operating rules and a
checklist in a few dozen lines. The long one is the complete skill, generated
from it: instructions, checklist, house rules and worked cases. Both work alone.

| Prompt | Use it for | Skill |
|---|---|---|
| [Neutral text](neutral.md) | Release notes, announcements, introductions, mail to existing customers | `fontlab-neutral` |
| [Write marketing copy](write-marketing.md) | New landing pages, product pages, campaigns, taglines | `fontlab-marketing` |
| [Edit marketing copy](edit-marketing.md) | Revising existing marketing copy | `fontlab-marketing` |
| [Write technical text](write-technical.md) | New procedures, reference pages, help articles | `fontlab-technical` |
| [Edit technical text](edit-technical.md) | Revising existing technical text | `fontlab-technical` |
| [Write balanced text](write-balanced.md) | New pieces that join appeal to precise explanation | `fontlab-write` |
| [Edit balanced text](edit-balanced.md) | Revising mixed drafts passage by passage | `fontlab-rewrite` |
| [Condense into a TLDR](tldr.md) | A literary summary at about 20% that keeps the source’s voice | `fontlab-tldr` |
| [Review a draft](review.md) | A second reader in a fresh chat: failures with locations, no rewrite | all of the above |

## Ask for the check, not only the rules

A long list of rules asks the model to remember all of them while it writes,
and models drop instructions as the list grows. So every prompt ends its rules
with a checklist and asks for a loop: after each portion, check each item on
its own against the text and the evidence, repair only what fails, recheck the
repairs and stop after three rounds. What still fails is marked, not declared
finished.

A writer reviewing their own draft reads what they meant. For anything that
matters, paste the draft and its evidence into a new chat with the
[review prompt](review.md), without the conversation that produced the draft,
and take its findings back to the writing session.

The writing guide explains the method in
[For agents](https://fontlab.dev/vexy-fontlab-writing-styleguide/fl1992mk/guide/for-agents/)
and the [checklists](https://fontlab.dev/vexy-fontlab-writing-styleguide/fl1992mk/guide/checklists/).
