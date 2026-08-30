# Daddy's Game Workshop — Repository Instructions

This repository contains kid-created browser games and the Daddy's Game Workshop idea collector.

## Main goal

Turn a child's imaginative idea into a polished, eye-catching, playable browser game without making the child become a prompt engineer.

The kid supplies the idea.
Agent K translates the idea.
The game builder/Codex handles engineering and quality.

## Default platform

- GitHub Pages
- iPhone/iPad first
- Free to run
- Prefer a single self-contained HTML/CSS/JavaScript `index.html` per game
- No paid APIs
- Avoid external libraries unless Dad explicitly approves them

## Repository layout

Games belong at:

`games/<kid>/<game-slug>/index.html`

Kid buckets currently include:

- `games/quinton/`
- `games/lincoln/`
- `games/adella/`
- `games/gemma/`
- `games/family/`

### Critical path rule

For a NEW game, create a new nested game folder.

Do **not** replace:

`games/<kid>/index.html`

unless Dad explicitly asks to change that kid's landing/index page.

For an UPDATE, keep the existing game's folder and public URL unless Dad asks for a new version.

## Kid-first interpretation

- Preserve the child's actual concept.
- Do not force a default genre.
- Do not automatically add levels, treasure, bosses, shops, pets, combat, or exploration.
- Choose mechanics only when they fit the idea or fill a genuine gap.
- Card games should remain card games.
- Board games should remain board games.
- Learning games should make learning part of play.
- Creature/pet games should make creatures central to play.
- If camera/view/style is left to the builder, choose what best expresses the idea.

## Game quality

A game is not finished merely because the code parses.

- Make the first 30 seconds clear and interesting.
- Give important actions satisfying visual feedback.
- Use animation, particles, transitions, sound, squash/stretch, screen shake, lighting, or other feedback when appropriate.
- Prefer coherent Canvas/SVG/CSS artwork over emoji-only visuals.
- Keep art direction consistent.
- Keep controls reachable and readable on small screens.
- Include a clear gameplay loop.
- Include restart/replay behavior where relevant.
- Use localStorage for meaningful persistent progress when appropriate.
- Prefer a smaller polished game over a large unfinished one.

## Update behavior

- Preserve working features unless the request says to remove them or a change clearly improves the requested feature.
- Fix broken, boring, confusing, or awkward parts before adding unrelated complexity.
- Keep familiar controls unless the requested change requires otherwise.
- Never silently overwrite a different game or parent landing page.

## QA

Before considering a game complete:

1. Run:
   `python scripts/qa_games.py`
2. Fix any errors introduced by the change.
3. Confirm the game has the expected start state and core interaction.
4. Confirm important touch controls fit an iPhone/iPad viewport.
5. Confirm completion/win/loss/restart behavior when the game type needs it.
6. Do not claim visual correctness from syntax alone; visual problems still require actual review.

GitHub Actions also runs the free static QA workflow in:

`.github/workflows/game-qa.yml`

## Supporting docs

- `docs/AGENT_K_V2.md`
- `docs/DADDYS_GAME_BUILDER_RULES_V2.md`
- `docs/WORKSHOP_PIPELINE_V2.md`
