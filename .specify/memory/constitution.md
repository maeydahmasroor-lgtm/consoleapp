<!--
---
Sync Impact Report
---
Version change: 0.0.0 → 1.0.0
Summary: Initial constitution defining core principles for the Python console-based todo application.
Principles Added:
- I. Simplicity and Focus
- II. Zero-Dependency Core
- III. Robust Input Handling
- IV. Clean and Readable Code
- V. Stateful In-Memory Model
- VI. Atomic and Predictable Operations
- VII. Interactive Menu-Driven Interface
Principles Modified: None
Principles Removed: None
Templates Requiring Updates:
- [ ] .specify/templates/plan-template.md
- [ ] .specify/templates/spec-template.md
- [ ] .specify/templates/tasks-template.md
Follow-up TODOs:
- TODO(RATIFICATION_DATE): Set initial adoption date.
-->
# Console Todo App Constitution

## Core Principles

### I. Simplicity and Focus
The application must remain a simple, console-based tool. Functionality is restricted to core todo management. No graphical user interfaces (GUIs), database integrations, or web frameworks are permitted.

### II. Zero-Dependency Core
The core application logic must not introduce any third-party package dependencies. All functionality must be implemented using the Python 3.12 standard library to ensure portability and minimize setup complexity.

### III. Robust Input Handling
All user input must be validated. The application must handle invalid commands, incorrect data types, and out-of-bounds selections gracefully without crashing, providing clear feedback to the user.

### IV. Clean and Readable Code
Code must be well-structured, clearly documented where logic is complex, and strictly follow PEP 8 style conventions. Logic must be separated into single-responsibility functions to enhance modularity and testability.

### V. Stateful In-Memory Model
The application state (the list of todos) must be managed exclusively in-memory. The data model is immutably defined by a `Todo` class containing a required `name` (string), an optional `description` (string), and a `status` (string, either "pending" or "complete").

### VI. Atomic and Predictable Operations
The application must expose a well-defined set of atomic operations: `add`, `list`, `update` (name/description), `delete`, and `toggle` (status). Each operation must be self-contained and predictable.

### VII. Interactive Menu-Driven Interface
The user experience is non-negotiably guided by a clear, persistent menu presented within a main application loop. The menu must display all available commands and be the primary method of interaction.

## Governance
This Constitution is the authoritative source for project standards. All development work, code reviews, and planning must adhere to its principles.

Amendments to this constitution require a version bump according to Semantic Versioning rules and propagation of changes across all dependent project templates.

**Version**: 1.0.0 | **Ratified**: TODO(RATIFICATION_DATE): Set initial adoption date. | **Last Amended**: 2026-01-01