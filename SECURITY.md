# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability in Th1nkN3st, please report it to us at:
- **Email**: devsecopstips@gmail.com
- **Subject Line**: [SECURITY] Brief description

We will respond within 48 hours.

## Scope

This is a static Jekyll site hosted on GitHub Pages. Security concerns include:
- XSS vulnerabilities in user-submitted content
- Malicious links or affiliate URL manipulation
- Social engineering via comments or external links
- Privacy concerns with tracking/analytics

## Out of Scope

- Server-side vulnerabilities (no server-side code)
- Database issues (no database)
- Issues with third-party services (GitHub, DNS providers)

## Security Best Practices

We follow these security practices:
1. No user authentication or data collection
2. All external links use `rel="noopener noreferrer"`
3. Content Security Policy headers configured
4. Regular dependency updates
5. Public repository for transparency

## Disclosure Policy

- We will acknowledge receipt within 48 hours
- We will provide a fix timeline within 7 days
- We will credit reporters (unless they prefer anonymity)
- We will publish security advisories for confirmed vulnerabilities

Thank you for helping keep Th1nkN3st secure!
