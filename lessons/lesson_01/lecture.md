# Lesson 01 Lecture

## Goal

Build a basic mental map of Python collections and syntax so you can start solving exercises without stopping to google every line.

This lecture is intentionally short. It gives you just enough context to work.

## The Main Built-In Collection Types

### `list`

Ordered and mutable.

Use it when:

- order matters
- duplicates are allowed
- you want to append, remove, or update items

Examples:

```python
files = ["invoice.pdf", "notes.txt", "report.pdf"]
numbers = [1, 2, 3]
```

Access:

```python
files[0]
files[-1]
```

### tuple

Ordered and usually used as a fixed-size grouping of values.

Use it when:

- the position of values matters
- you want a small record-like structure
- you want unpacking

Examples:

```python
point = (10, 20)
name_age = ("Alice", 30)
```

Unpacking:

```python
name, age = ("Alice", 30)
```

You do not need tuples everywhere. They are just one more useful tool.

### `dict`

Key-value mapping.

Use it when:

- you want to look up a value by key
- you want to count things
- you want to represent a small structured record

Examples:

```python
extension_by_file = {
    "invoice.pdf": "pdf",
    "notes.txt": "txt",
}

document = {
    "name": "invoice.pdf",
    "pages": 3,
    "processed": True,
}
```

Access:

```python
document["name"]
document["pages"]
```

### `set`

Unordered collection of unique values.

Use it when:

- duplicates should disappear
- you only care whether a value exists
- membership checks should be fast

Examples:

```python
extensions = {"pdf", "txt", "docx"}
```

Or built from a list:

```python
unique_words = set(["doc", "scan", "doc"])
```

## Basic Python Syntax Patterns

### Truthiness

In Python, empty collections are falsey.

```python
files = []

if files:
    print("There are files")
```

If `files` is empty, that condition is false.

### Membership

Use `in`.

```python
if "pdf" in extensions:
    print("PDFs exist")
```

### Slicing

Useful for lists and strings.

```python
name = "invoice.pdf"

name[:7]
name[-3:]
```

You do not need to master every slicing form today. Just recognize the syntax.

## Comprehensions

This is one of the most important Python features for everyday code.

### List comprehension

Pattern:

```python
[result for item in items if condition]
```

Example:

```python
files = ["invoice.pdf", "notes.txt", "report.pdf"]
pdfs = [name for name in files if name.endswith(".pdf")]
```

Read it as:

"Build a list of `name` for each `name` in `files`, but only if it ends with `.pdf`."

### Dict comprehension

Pattern:

```python
{key_expr: value_expr for item in items}
```

Example:

```python
extension_map = {name: name.split(".")[-1] for name in files}
```

### Set comprehension

Pattern:

```python
{expr for item in items if condition}
```

Example:

```python
extensions = {name.split(".")[-1] for name in files}
```

## Loop First, Then Refactor

At your stage, this is the right approach:

1. solve it with a normal loop
2. make sure you understand the logic
3. refactor into a comprehension if it becomes clearer

That matters because comprehensions should improve readability, not become a magic trick.

## Common Patterns You Will Use Today

### Filter a list

```python
pdfs = []
for name in files:
    if name.endswith(".pdf"):
        pdfs.append(name)
```

Refactor:

```python
pdfs = [name for name in files if name.endswith(".pdf")]
```

### Build a mapping

```python
extension_map = {}
for name in files:
    extension_map[name] = name.split(".")[-1]
```

Refactor:

```python
extension_map = {name: name.split(".")[-1] for name in files}
```

### Count values

```python
counts = {}
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
```

This is a very common Python pattern.

## Java-to-Python Mindset Shift

Do not aim for:

- lots of boilerplate
- classes for everything
- explicit ceremony around simple data
- overly abstract code too early

Do aim for:

- short readable transformations
- direct use of built-in types
- clear variable names
- simple functions

These skills apply broadly across scripts, CLIs, backend services, and automation tasks.

## What You Need to Remember for This Lesson

If you only keep a few things in your head, keep these:

- `list` for ordered items
- `dict` for key-value lookups and counts
- `set` for uniqueness and membership
- tuple for fixed grouped values and unpacking
- start with loops, then rewrite with comprehensions

## Next Step

Open [exercise.py](/Users/michael.linka/Udemy/pythonification/lessons/lesson_01/exercise.py) and solve the tasks.
