# hormiga-culona

Parent repository for the hackathon project.

## Structure

- `backend/`: git submodule pointing to [`hormiga-culona-back-end`](https://github.com/CapituloJaverianoACM/hormiga-culona-back-end).
- `frontend/`: reserved for the frontend app.
- `docs/`: project notes, decisions, setup guides, and hackathon documentation.

## Working agreement

- Keep app code inside its own folder (`backend/`, later `frontend/`).
- Prefer small commits with clear messages.
- Document decisions and setup steps in `docs/` instead of chat.
- Backend is a submodule, so after cloning run `git submodule update --init --recursive`.

## Useful commands

```bash
# clone with submodules
git clone --recurse-submodules git@github.com:CapituloJaverianoACM/hormiga-culona.git

# if already cloned
git submodule update --init --recursive

# update backend to the latest upstream main
git submodule update --remote backend
```
