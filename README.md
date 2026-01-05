# mlready

**mlready** is a lightweight Python library for making tabular datasets **safe and ready for machine-learning pipelines**.

It focuses on **observation → risk detection → safe normalization**, not aggressive automation.

---

## Why mlready?

Real-world datasets fail ML pipelines because of:

* numeric values stored as strings (`"$1,200"`, `"1.2M"`)
* inconsistent booleans (`Yes / no / YES / n`)
* datetime columns stored as text
* unseen categories between train and test
* silent data leakage and ID-like columns

`mlready` helps you **detect these issues early and fix only what is safe**.

---

## Installation

```bash
pip install mlready
```

---

## Core API (3 functions)

### 1️⃣ `profile(df)`

**Purpose:** Understand the dataset (read-only).

```python
import mlready as mr

report = mr.profile(df)
```

**What it provides:**

* dataset shape, memory usage, duplicates
* per-column:

  * dtype and inferred logical type
  * missing counts and percentages
  * unique counts and percentages
  * top values
  * pattern hints (currency, boolean, datetime)

No data is modified.

---

### 2️⃣ `audit(df, target=None, reference_df=None)`

**Purpose:** Detect ML risks before training.

```python
audit_report = mr.audit(df, target="label")
```

**What it detects:**

* ID-like columns
* zero-variance columns
* high-cardinality categoricals
* numeric / boolean / datetime stored as strings
* potential target leakage
* ghost categories (train vs test mismatch)
* schema drift

Returns **structured warnings**, not guesses.

---

### 3️⃣ `apply(df, recipe=None)`

**Purpose:** Safely normalize raw data.

```python
clean_df, recipe, report = mr.apply(df)
```

**What it safely applies (v0.1):**

* currency / numeric string → numeric
  (`"$1,200"`, `"(50)"`, `"1.2M"`)
* boolean strings → boolean dtype
  (`Yes / no / YES / n`)
* unambiguous datetime parsing
* safe numeric downcasting (nullable-aware)

**What it does NOT do:**

* no column dropping
* no encoding
* no fuzzy category merging
* no feature engineering

All actions are recorded in a **reproducible recipe**.

---

## Example

```python
import pandas as pd
import mlready as mr

df = pd.DataFrame({
    "Price": ["$1,200", "1.2M"],
    "Membership": ["Yes", "no"],
})

clean, recipe, report = mr.apply(df)

print(clean)
print(report)
```

Output:

```text
       Price  Membership
0     1200.0        True
1  1200000.0       False
```

---

## Design Principles

* **Safety first** – no silent destructive actions
* **Sampling-aware** – fast on large data, reliable on small data
* **Pipeline-friendly** – deterministic behavior via recipes
* **Minimal dependencies** – pure pandas / numpy

---

## When to use mlready

Use `mlready` when:

* ingesting raw CSVs or business data
* validating train vs test consistency
* preparing data before encoding / modeling
* building reproducible ML pipelines

Not intended to replace:

* feature engineering libraries
* AutoML tools
* visualization-heavy EDA tools

---

## Project Status

* Version: **0.1.0**
* Stable core API
* Tests included
* Ready for production pipelines (safe mode)

---

## License

MIT License

---