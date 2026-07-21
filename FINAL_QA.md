# Final QA · Official-first redesign · 2026-07-21

## Content integrity

- Edition: official-first-redesign-2026
- Searchable topics: 423
- Guides: 280
- FAQs: 51
- Checklist items: 92
- Official / authority sources: 50
- Final HTML bytes: 333,135
- Gzip bytes: 61,973
- Final SHA-256: `870213a38ef91c0c882e37d76ec78fc5d0d5669de35c836e5591fd5b684ecdbf`
- Payload reconstruction: passed locally
- Per-part SHA-256 validation: passed locally

## Source and detail acceptance

- First-party source metadata and checked dates: passed
- Apple Wallet walkthrough contains prerequisites, exact flow, activation waits, Card Management and three official links: passed
- Detailed enrolment, unit selection, international arrival update, digital setup and timetable walkthroughs: passed
- Warnings and troubleshooting are searchable: passed

## Browser acceptance

Validated in Chromium at desktop and mobile viewport sizes:

- School-style home page rendering: passed
- Natural-language instant search: passed
- Query `Apple Wallet`: 8 suggestions; correct guide ranked first
- Detailed article drawer and deep-link opening: passed
- Apple Wallet article: 7 sections, 3 source links and Card Management troubleshooting
- Checklist persistence: passed; progress changed from 0/92 to 1/92
- Light/dark theme switching: passed
- Mobile navigation and responsive layout: passed
- Console/page errors: 0

## Release gate

GitHub Pages deployment may proceed only when `scripts/verify_payload.py` reconstructs the exact final HTML and matches the content manifest. Public Pages must then return exactly 333,135 bytes with the expected SHA-256 before the release is accepted.
