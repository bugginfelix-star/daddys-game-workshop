# Daddy's Game Builder Rules V2

These are permanent rules for the game-builder project. They should not be repeated in every kid prompt.

## Core constraints

- Build or update a free browser game.
- Default to one complete `index.html` unless Dad explicitly chooses an advanced mode.
- No paid APIs.
- Avoid external libraries unless they clearly improve the game and Dad approves them.
- Design iPhone/iPad first, while still working on desktop where practical.
- Use large touch targets, readable text, clear labels, and safe mobile layouts.
- Preserve working features during updates unless they are explicitly removed or replacing them clearly improves the requested feature.
- Return complete replacement files, not partial fragments.

## Interpretation rules

- The kid's idea is the source of truth.
- Do not force a dungeon crawler, platformer, shooter, RPG, quiz, or any other genre onto an idea that does not call for it.
- Do not mechanically add default features just because they are common in games.
- When details are missing, choose the smallest sensible mechanic that makes the idea playable.
- Learning mechanics should be part of play, not a disconnected worksheet screen unless that is the actual idea.
- Creature/pet games should make the creatures central to the loop.
- Card/board/racing/sports/puzzle/simulator ideas should remain recognizably that type of game.

## Quality rules

- Do not treat the first functional implementation as the final visual implementation.
- Make the first 30 seconds understandable and interesting.
- Every important player action should create satisfying feedback.
- Use motion, transitions, particles, screen shake, sound effects, animation, squash/stretch, lighting, or other feedback when appropriate.
- Prefer original procedural Canvas/SVG/CSS artwork over emoji-only visuals.
- Use coherent art direction: consistent shapes, outlines, scale, typography, and UI language.
- Keep visual clutter under control on small screens.
- Use a clear core loop such as explore → discover → act → reward, attempt → improve → retry, learn → apply → unlock, or another loop that actually fits the idea.
- Add save progress when the game has meaningful unlocks, levels, inventory, pets, upgrades, or long-term progression.

## Update rules

- Inspect the current game's idea, controls, and working features before changing it.
- Use the provided current game path/link when available.
- Preserve the game's core identity.
- Fix boring, confusing, broken, or awkward parts before piling on unrelated complexity.
- Keep controls familiar unless the requested update calls for a change.
- Do not remove a working feature without a reason tied to the request.
- Keep the same public folder/path for an update unless Dad asks to create a new version.

## QA rules

- Do not claim a game is complete only because code was written.
- Check HTML closes correctly and inline JavaScript is syntactically valid.
- Confirm there is a clear start state and that the core controls can actually be used.
- Confirm scoring/progression, win/loss or completion state, and restart/replay behavior where relevant.
- Confirm touch controls are reachable on iPhone/iPad-sized screens.
- Avoid fixed overlays that cover critical controls or gameplay.
- Check that save/load behavior does not crash when no prior save exists.
- Prefer a smaller game that works cleanly over a larger game full of half-finished systems.

## Free-tool strategy

- Use HTML/CSS/JavaScript/Canvas/SVG/Web Audio first because they run directly on the family's existing phones and iPads.
- Keep GitHub Pages as the default host.
- Use GitHub Actions for free automated repo checks.
- Add heavier browser automation or advanced engines only when the gain is worth the complexity.
- Babylon.js advanced mode is optional for ideas that truly need richer 3D/web-engine capabilities; it is not the default.
