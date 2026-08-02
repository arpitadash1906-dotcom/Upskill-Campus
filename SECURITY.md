# Security Policy

## Supported Versions

The `main` branch receives security fixes.

## Reporting a Vulnerability

Please do not open public GitHub issues for sensitive reports.

Report vulnerabilities privately to the repository owner or maintainer. Include:

- A clear description of the issue
- Steps to reproduce
- Potential impact
- Affected files, routes, or services
- Suggested mitigation, if known

## Security Expectations

- Never commit `.env` files or production secrets.
- Rotate credentials immediately if they are exposed.
- Use strong values for `JWT_SECRET` and provider API keys.
- Restrict CORS origins in production.
- Validate and sanitize user-controlled input.
- Avoid logging sensitive tokens, cookies, passwords, or connection strings.
- Store uploads and generated media outside the repository.
