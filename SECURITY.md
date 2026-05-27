# Security Policy

## Supported Versions

Current version: 1.0.0. This is an open-source protocol and reference artifact, not a production-certified system.

## Reporting a Vulnerability

If you discover a security vulnerability in LRI, please report it by opening an issue at:

https://github.com/safal207/Living-Relational-Identity-LRI/issues

Do not open a public issue for sensitive vulnerabilities. Instead, email the repository maintainer directly (contact information in commit history).

## Scope

LRI is a protocol and reference implementation for identity-boundary reasoning. It is not currently certified for production safety, compliance, clinical, legal, or governance use. See [docs/NON_CLAIMS.md](docs/NON_CLAIMS.md) for full scope boundaries.

Security-relevant areas include:
- Cryptographic continuity of identity state chains
- Authority and access control in the reference implementation
- Audit log integrity (DMP)

## No Warranty

As specified in the MIT license, LRI is provided "as is" without warranty of any kind.
