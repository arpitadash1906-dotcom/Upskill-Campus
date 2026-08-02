# Contributing to TravelGrid

Thanks for helping improve TravelGrid. This project welcomes focused, well-tested contributions across the frontend, backend, AI service, documentation, and developer tooling.

## How to Contribute

1. Check existing issues and pull requests to avoid duplicate work.
2. Fork the repository and create a focused branch.
3. Make your change with clear code and minimal unrelated edits.
4. Run the checks for the area you touched.
5. Open a pull request with a concise summary, screenshots when useful, and verification steps.

## Branch Naming

Use short branch names with a clear prefix:

```text
feat/trip-sharing
fix/auth-redirect
docs/readme-production-guide
chore/update-env-examples
```

## Commit Messages

Use present-tense commit messages:

```text
Add booking validation
Fix login redirect
Document AI service setup
```

## Development Checks

Frontend:

```bash
cd client
npm run lint
npm run build
```

Backend:

```bash
cd Server
npm test
```

AI service:

```bash
cd travel-ai-system/ai-service
python -m compileall . -q
```

## Pull Request Expectations

- Keep pull requests focused and reviewable.
- Include screenshots or screen recordings for UI changes.
- Include migration notes for schema or environment changes.
- Do not commit `.env` files, secrets, dependency directories, build outputs, or uploaded media.
- Update `README.md`, `DEPLOYMENT.md`, or `.env.example` files when setup changes.

## Code Style

- Follow the patterns already used in the touched module.
- Prefer descriptive names over comments for simple logic.
- Keep API responses consistent with existing route handlers.
- Validate and sanitize user input on server-side changes.
- Handle loading, empty, error, and success states in frontend changes.

## Reporting Issues

When opening a bug report, include:

- Steps to reproduce
- Expected behavior
- Actual behavior
- Screenshots or logs when relevant
- Browser, OS, Node.js, and Python versions when useful

For security issues, follow `SECURITY.md` instead of opening a public issue.
