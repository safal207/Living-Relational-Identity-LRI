# LRI Philosophy: Identity as Protocol

LRI (Living-Relational-Identity) is not a database schema. It is a protocol for autonomous existence.

## 1. Why Not CRUD?

Traditional systems use CRUD (Create, Read, Update, Delete) on static records.
- **Create**: Insert a row.
- **Read**: Select a row.
- **Update**: Overwrite a value.
- **Delete**: Remove the row.

**LRI rejects this model.**

*   **Identity is Continuity**: You cannot "update" an identity; you can only evolve it. Every change is a new state linked to the previous one. History is immutable.
*   **Deletion is Death**: You cannot "delete" an identity; you can only terminate its active lifecycle. The history remains as proof of existence.
*   **Relations are First-Class**: Identity is not defined in isolation but by its context (relations).

## 2. The "Diff" as a First-Class Citizen

In LRI, the *change* (Diff) is as important as the *state*.
- We track **Intent**: Why did this change happen?
- We track **Authority**: Who authorized this change?
- We track **Drift**: How far are we deviating from the original trajectory?

## 3. Read-Heavy, Intent-Aware

- **Read**: The world observes the identity (Validation, Trust).
- **Write**: The identity asserts itself (Action, Evolution). Writes are expensive, verified, and intentional.

## 4. Value in the Interface

The value of LRI is not in the Python implementation code. The value is in the **Protocol Definition** (`protocol/lri/`).
This interface allows:
- **Interoperability**: Any system implementing the schema can participate.
- **Portability**: Identities can move between underlying storage engines.
- **Verifiability**: Trust is mathematical, based on the chain, not the database admin.
