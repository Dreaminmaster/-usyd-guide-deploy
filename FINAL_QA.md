# Final QA · Source-labelled redesign · 2026-07-21

## Content integrity

- Edition: source-labelled-redesign-2026
- Searchable topics: 423
- Guides: 280
- FAQs: 51
- Checklist items: 92
- Original first-party / authority sources: 50
- Base knowledge HTML: 333,135 bytes
- Published HTML: 333,239 bytes
- Published HTML SHA-256: `5cdacc4e0193b85ee7e8f809000bb3791b681e3dd5dfcbff8886fbabbe140b31`
- Provenance CSS: 3,220 bytes, independently hashed
- Provenance JavaScript: 15,994 bytes, independently hashed

## Source behaviour acceptance

- Full answer remains inside the website article: passed
- External source links are optional and collapsed at the bottom: passed
- Visible labels for official fact, official system path, student experience and editorial synthesis: passed
- Student-experience content only renders when a concrete item is present: passed
- Official rules and eligibility remain distinguishable from practical advice: passed
- Personal Offer, email, Sydney Student, Canvas and visa records are described as higher priority: passed

## Apple Wallet acceptance

The in-page guide includes:

- enrolment, UniKey, Okta and photo prerequisites;
- Transact eAccounts installation and University of Sydney selection;
- iPhone Apple Wallet flow;
- Apple Watch flow;
- building, library, printing and concession synchronisation waits;
- actual card uses;
- lost-device deactivation through Card Management or SydPay;
- reactivation after recovery;
- exam and physical-card limitations;
- troubleshooting and separately labelled editorial advice.

## Static and build acceptance

- Provenance JavaScript syntax (`node --check`): passed
- Base payload per-part SHA-256 validation: required by release gate
- Base HTML bytes and SHA-256 validation: required by release gate
- CSS and JavaScript bytes and SHA-256 validation: required by release gate
- Final injected HTML bytes and SHA-256 validation: required by release gate
- Public HTML, CSS and JavaScript online hashes: required by online QA

## Release gate

GitHub Pages may publish only when `scripts/verify_payload.py` reconstructs the exact base page, verifies both readable provenance assets, injects them, and matches the final manifest. Online QA must then independently download and hash all three public files before the release is accepted.
