# LRI vs Privacy, Consent, and Data Minimization

Status: reviewer-facing concept comparison.

See [NON_CLAIMS.md](NON_CLAIMS.md) for scope boundary. See [GLOSSARY.md](GLOSSARY.md) for term definitions.

LRI does not replace, implement, or certify privacy, consent, or data minimization practices.

---

## Purpose of this comparison

LRI operates in a space adjacent to privacy, consent, and data minimization. This document clarifies the relationships and boundaries — what LRI shares, what it does not claim, and where it contributes something distinct.

---

## LRI vs Privacy

### What they share

Both care about:

- the person's control over their own information
- preventing unauthorized use of personal data
- transparency about how data is used

### Where they differ

| Dimension | Privacy frameworks (e.g. GDPR, PIPL) | LRI |
|---|---|---|
| Primary concern | Data protection, lawful processing, disclosure control | Identity continuity, revisability, relational context |
| Unit of analysis | Personal data, consent records, processing purposes | Identity state, relational context, authority attributions |
| Temporal scope | Collection-to-deletion lifecycle | Continuous identity chain across context changes |
| Harm model | Data breach, unauthorized disclosure, unlawful processing | Identity freezing, silent authorship, relational drift |
| Mechanism | Access controls, consent forms, DPO, audit | Protocol invariants, continuity hashes, authority checks |

### Boundary

LRI does not implement privacy controls. It does not encrypt data, manage consent records, or enforce data retention policies. Those remain the responsibility of privacy frameworks.

LRI highlights a gap that privacy frameworks do not fully address: identity harm that occurs without data breach or consent violation.

---

## LRI vs Consent

### What they share

Both recognize that:

- consent is foundational to legitimate human-system relationships
- consent can lose meaning over time
- the person should remain the decision-maker

### Where they differ

| Dimension | Consent frameworks | LRI |
|---|---|---|
| Moment | Consent is given at a point in time | Identity is continuous across time |
| Change | Re-consent is a discrete event | Context drift is continuous |
| Scope | What data is collected and used | Who the person is and is becoming |
| Failure mode | Consent not obtained or exceeded | Consent still valid but meaning has drifted |

### Boundary

LRI does not replace consent. It does not provide consent forms, consent records, or consent management APIs. Consent processes remain necessary and separate.

LRI makes visible a risk that consent processes cannot address alone: consent that is technically valid but contextually obsolete.

---

## LRI vs Data Minimization

### What they share

Both resist:

- collecting data without purpose
- retaining data longer than needed
- using data for purposes beyond the original scope

### Where they differ

| Dimension | Data minimization | LRI |
|---|---|---|
| Question | What data is necessary? | What identity context is preserved? |
| Strategy | Limit collection, retain less, delete faster | Track continuity, make drift visible, preserve revisability |
| Harm | Privacy risk from data hoarding | Identity risk from context erasure |

### Boundary

LRI does not minimize data. It does not specify what to collect or how long to keep it. Data minimization and LRI address different risks:

- data minimization: too much data in the system
- LRI: too little context preserved for identity continuity

Both are necessary. Neither replaces the other.

---

## Summary

| | Privacy | Consent | Data minimization | LRI |
|---|---|---|---|---|
| Protects | Data from misuse | Authorized processing | Proportional collection | Identity continuity |
| Mechanism | Access control, encryption | Forms, records, withdrawal | Limit, retain, delete | Protocol invariants |
| Blind spot | Identity harm without breach | Context drift | Identity erasure | — |
| LRI complements | Yes — different harm model | Yes — drift visibility | Yes — context preservation | — |

---

## Correct framing for reviewers

LRI is not a privacy protocol, a consent framework, or a data minimization strategy. It is a **human-boundary protocol** that defines invariants for protecting identity continuity, revisability, and relational context.

Privacy, consent, and data minimization remain necessary. LRI addresses something adjacent that they do not fully cover: identity-level harm in long-term human-system relationships.
