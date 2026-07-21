# Final QA · 2026-07-21

## Content integrity

- Searchable topics: 417
- Guides: 274
- FAQs: 51
- Checklist items: 92
- Official sources: 45
- Final HTML bytes: 264,614
- Gzip bytes: 51,649
- Final SHA-256: `49780e25289d6729302b50e73e34216ebbcdec4483376557df4877106ba62fbb`
- Payload reconstruction: passed
- Per-part SHA-256 validation: passed

## Browser acceptance

Validated in Chromium at desktop and mobile viewport sizes:

- Home page rendering: passed
- Whole-site search: passed; test query `Apple Wallet` returned 19 results
- Article drawer and deep-link opening: passed
- Checklist persistence: passed; progress changed from 0/92 to 1/92
- Light/dark theme switching: passed
- Mobile navigation and responsive layout: passed
- Console errors: 0

## Release gate

GitHub Pages deployment may proceed only when `scripts/verify_payload.py` reconstructs the exact final HTML and matches the content manifest. A failed verification records `BUILD_STATUS.md` and does not replace the existing live site.
