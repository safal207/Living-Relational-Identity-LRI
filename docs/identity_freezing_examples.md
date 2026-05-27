# Identity Freezing — Examples

Status: reviewer-facing concept illustration.

See [NON_CLAIMS.md](NON_CLAIMS.md) for scope boundary. See [GLOSSARY.md](GLOSSARY.md) for term definitions.

LRI does not classify, score, diagnose, profile, or infer a person's true self.

---

## What identity freezing looks like

Identity freezing occurs when a system reduces a living person to a fixed representation that resists revision. These examples illustrate the pattern — they are not claims that any specific product or system engages in identity freezing.

---

### Example 1: Persona lock-in

A collaboration platform assigns users a persona after observing their first few interactions. Alice is labeled "executor" because she completes tasks. Bob is labeled "ideator" because he contributes suggestions.

Over time, Alice's recommendations are filtered toward execution tasks. When she proposes a strategic direction, the system deprioritizes it — it does not fit the "executor" model. Alice cannot revise her persona without going through a formal override process.

**What is frozen:** Alice's role category.
**What is lost:** Revisability — Alice's ability to be seen differently as she grows.

---

### Example 2: Trait inference from sparse data

Carol signs up for a professional networking service. She lists two skills. The system infers a personality profile, a collaboration style, and a career trajectory from this sparse input.

Weeks later, Carol updates her skills and interests. The system continues to use the original inferred profile for matching, recommendations, and search visibility. The updated information is treated as noise; the original profile is treated as ground truth.

**What is frozen:** An inferred trait set based on early, thin data.
**What is lost:** Authority over one's own identity representation.

---

### Example 3: Behavioral loop optimization

A learning platform rewards consistency. Users who follow predictable learning paths receive smoother recommendations, higher engagement scores, and more visible profiles.

Diana is a curious but nonlinear learner. She skips between topics. The system flags her behavior as "low coherence" and reduces her recommendation quality. To restore quality, Diana must either conform to the expected path or manually reset her profile — losing her history.

**What is frozen:** An expected behavioral trajectory.
**What is lost:** Exploration, self-directed learning, nonlinear growth.

---

### Example 4: Past behavior as destiny

An AI writing assistant profiles users by linguistic style. Elena writes formally in a professional context. The assistant learns this pattern and begins to "correct" her informal writing toward formal tone, even in personal contexts where she prefers a casual voice.

Elena's past formal writing becomes a filter applied to all future writing. The system does not distinguish context. Her identity as a writer is reduced to a single detected style.

**What is frozen:** A detected stylistic pattern applied universally.
**What is lost:** Contextual variation, self-expression across contexts.

---

### Example 5: Silent authorship of identity narrative

A health and wellness application tracks user goals. Frank sets a goal of "run 5 km" and achieves it. The system records this and begins to treat Frank as a "runner" — suggesting running content, setting running goals, categorizing him in running cohorts.

Frank wants to shift to swimming. The system resists: swimming recommendations are deprioritized, running goals keep reappearing, and his profile still reads "runner." The system has silently authored an identity narrative that Frank did not choose.

**What is frozen:** A system-authored identity narrative.
**What is lost:** Self-creation — the ability to redefine one's own goals.

---

## What these examples are not

These examples do not claim that:

- identity freezing is always intentional or malicious
- any specific product or company engages in these patterns
- LRI detects, measures, or prevents identity freezing in production
- identity freezing is the only or primary risk in human-system relationships

They are illustrative boundaries — making the abstract concept of "living identity" concrete for reviewers.

## Why LRI cares about identity freezing

LRI is a human-boundary protocol. Its purpose is not to detect freezing but to define invariants that make freezing visible and resistible:

- continuity (identity cannot be silently rewritten)
- revisability (identity can change without breaking continuity)
- authority (the person retains authorship of their identity narrative)

These invariants do not guarantee that freezing will not occur. They create the conditions under which freezing, if it occurs, can be detected and contested.
