# hormiga-culona

Parent repository for the hackathon project.

## Structure

- `backend/`: imported from [`hormiga-culona-back-end`](https://github.com/CapituloJaverianoACM/hormiga-culona-back-end) with full commit history preserved.
- `frontend/`: reserved for the frontend app.
- `docs/`: project notes, decisions, setup guides, and hackathon documentation.

## Working agreement

- Keep app code inside its own folder (`backend/`, later `frontend/`).
- Prefer small commits with clear messages.
- Document decisions and setup steps in `docs/` instead of chat.
- If we need to sync backend changes from the original repo again, use git subtree so history stays intact.

## Useful commands

```bash
# add/update backend from upstream
git remote add backend-upstream https://github.com/CapituloJaverianoACM/hormiga-culona-back-end.git
git fetch backend-upstream
git subtree pull --prefix=backend backend-upstream main
```
