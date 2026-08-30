# Daddy's Game Workshop V2 Pipeline

The goal is to let the kids invent games with simple prompts while keeping recurring AI/token use and tooling costs low.

## Intended flow

1. **Kid on iPad:** uses Daddy's Game Workshop to describe a game idea.
2. **Workshop page:** produces a short IDEA PACKET only.
3. **Agent K:** translates the idea packet into a concise GAME BRIEF.
4. **Daddy's Game Builder:** applies permanent engineering/quality rules and builds or updates the playable game.
5. **GitHub:** stores the game and hosts it with GitHub Pages.
6. **GitHub Actions:** performs free automatic structural and JavaScript checks.
7. **Dad:** reviews the actual game and decides whether it needs another improvement pass.

## Why the prompts are intentionally small

Permanent requirements such as mobile support, complete files, free hosting, code quality, touch controls, and QA do not belong in every child's prompt. Repeating them wastes tokens and can drown out the child's actual idea.

The Workshop should collect imagination.
Agent K should translate.
The Builder should engineer.

## Default technology

- Single-file HTML/CSS/JavaScript
- Canvas/SVG/CSS procedural visuals
- Web Audio when useful
- localStorage for saves
- GitHub Pages hosting
- GitHub Actions for free QA

## Upgrade philosophy

Add tools when they create a real improvement without making the kids' workflow harder. Better AI models, free browser automation, reusable game systems, and optional advanced web engines can be adopted later without changing the basic kid → Dad workflow.
