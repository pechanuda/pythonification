# Lesson 03 Lecture

## Goal

Make comprehensions feel like a normal tool instead of a Python party trick.

You already saw the syntax in Lesson 01. This lesson is about using it with better judgment.

## The Three Main Shapes

### List comprehension

```python
[expr for item in items if condition]
```

Use it when you want a new list.

Example:

```python
pdf_files = [name for name in files if name.endswith(".pdf")]
```

### Set comprehension

```python
{expr for item in items if condition}
```

Use it when you want unique values.

Example:

```python
extensions = {name.split(".")[-1] for name in files}
```

### Dict comprehension

```python
{key_expr: value_expr for item in items if condition}
```

Use it when you want a mapping.

Example:

```python
pages_by_name = {doc["name"]: doc["pages"] for doc in documents}
```

## When Comprehensions Help

Comprehensions are strong when the logic is:

- one pass over the input
- one main expression
- maybe one simple filter

That usually covers a lot of practical scripting work.

## When a Loop Is Better

Prefer a normal loop when:

- you need multiple branches
- you are updating several outputs
- the logic needs comments to stay understandable
- the expression stops being readable in one glance

Pythonic code is not "short at all costs."

## Common Transformation Patterns

### Filter

```python
large_docs = [doc for doc in documents if doc["pages"] > 10]
```

### Map

```python
names = [doc["name"] for doc in documents]
```

### Filter and map together

```python
processed_names = [doc["name"] for doc in documents if doc["processed"]]
```

### Build a lookup

```python
status_by_name = {doc["name"]: doc["processed"] for doc in documents}
```

## Java Comparison

If you know Java streams, the rough idea can feel familiar. But do not force a stream mental model onto Python.

Comprehensions are more direct and less abstract:

- no chained method calls
- no lambda noise for simple cases
- often easier to read once the syntax clicks

The goal is not to imitate streams. The goal is to express simple transformations clearly.

## Practical Rule

Write the obvious loop first if needed.

Then ask:

"Would a comprehension make this easier to read in one scan?"

If yes, use it. If not, keep the loop.
