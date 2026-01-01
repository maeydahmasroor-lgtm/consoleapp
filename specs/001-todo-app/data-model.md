# Data Model

This document defines the data model for the Todo application, based on the entities identified in the feature specification.

## Entities

### Todo

Represents a single task.

**Attributes**:

| Name        | Type   | Constraints                  | Description                                      |
|-------------|--------|------------------------------|--------------------------------------------------|
| `name`      | string | Mandatory, non-empty         | The title of the task.                           |
| `description`| string | Optional                     | More details about the task.                     |
| `status`    | string | Must be "pending" or "complete" | The completion status of the task. Defaults to "pending". |

**State Transitions**:

- The `status` attribute can transition from "pending" to "complete" and from "complete" to "pending".
