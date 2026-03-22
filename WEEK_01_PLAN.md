# Week 1 Plan

## Theme

Python mindset and core collections.

This week is about becoming comfortable reading and writing small pieces of idiomatic Python without treating it like compressed Java.

## Week 1 Objectives

By the end of this week, you should be able to:

- choose between `list`, `dict`, and `set` confidently
- read and write list, dict, and set comprehensions
- use slicing and unpacking without hesitation
- transform small datasets in a Pythonic way
- understand simple scripts that process filenames and document metadata

## Time Budget

Target total: about 3-4 hours

This is split into four short sessions so it fits your weekly rhythm.

## Session 1: Core Collections and Reading Python

Target time: 45-60 minutes

### Concepts

- `list`: ordered collection
- `dict`: key-value mapping
- `set`: unique values and fast membership checks
- tuple unpacking
- truthiness

### Read and Notice

Focus on recognizing these patterns quickly:

```python
names = ["invoice.pdf", "notes.txt", "report.pdf"]

pdfs = [name for name in names if name.endswith(".pdf")]
extensions = {name.split(".")[-1] for name in names}
lengths = {name: len(name) for name in names}
```

Questions to ask yourself while reading:

- Why is a `set` useful here?
- Why is a `dict` better than parallel lists?
- What is being filtered vs transformed?

### Exercise

Create a file called `scripts/lesson1.py`.

Use this input:

```python
files = [
    "invoice_001.pdf",
    "invoice_002.pdf",
    "notes.txt",
    "report_final.docx",
    "image.png",
    "invoice_003.pdf",
    "todo.txt",
]
```

Write code that prints:

- all PDF files
- all filenames without extension
- a set of unique extensions
- a dictionary mapping filename to extension

### Constraint

First solve it with normal loops. Then rewrite at least part of it with comprehensions.

## Session 2: Counting, Membership, and Data Transformation

Target time: 45-60 minutes

### Concepts

- counting values with dictionaries
- membership checks with `in`
- choosing `set` vs `list`
- direct transformations instead of verbose loops

### Exercise

Use this input:

```python
words = ["doc", "scan", "doc", "report", "scan", "pdf", "report", "report"]
```

Build:

- a set of unique words
- a dictionary of word counts

Then write this function:

```python
def summarize_extensions(files: list[str]) -> dict[str, int]:
    ...
```

Expected shape:

```python
{"pdf": 3, "txt": 2, "docx": 1, "png": 1}
```

### Reflection

After solving it, ask:

- Did I make this more complicated than necessary?
- Did I create variables that are not pulling their weight?
- Would another developer understand this in one pass?

## Session 3: Working with Structured Records

Target time: 45-60 minutes

### Concepts

- lists of dictionaries
- filtering records
- projecting fields
- summing values
- mapping entities to attributes

### Exercise

Use this input:

```python
documents = [
    {"name": "invoice_001.pdf", "pages": 3, "processed": True},
    {"name": "notes.txt", "pages": 1, "processed": False},
    {"name": "report.pdf", "pages": 12, "processed": True},
    {"name": "draft.docx", "pages": 5, "processed": False},
]
```

Produce:

- names of processed documents
- names of documents with more than 2 pages
- total number of pages
- a dictionary mapping document name to page count

### Stretch

Rewrite at least two results using comprehensions or generator expressions.

## Session 4: Review, Cleanup, and Discussion

Target time: 30-45 minutes

### Tasks

- reread your own `lesson1.py`
- remove clumsy or repetitive parts
- rename unclear variables
- separate unrelated pieces with blank lines
- add one or two small helper functions only if they improve clarity

### What to Submit for Review

At the end of Week 1, bring:

- your `scripts/lesson1.py`
- any questions about syntax that still feel awkward
- any parts that feel too magical or hard to read

## What Success Looks Like

You do not need to memorize every syntax feature.

Success for Week 1 means:

- you can read basic Python without freezing
- you can solve small collection-based tasks comfortably
- you start recognizing when comprehensions help and when they hurt readability

## Common Java-to-Python Mistakes to Avoid

- overusing classes for small problems
- writing overly verbose loops when a direct expression is clearer
- naming things too ceremonially
- trying to force Java stream habits onto every transformation
- overcomplicating simple scripts with too much structure

## Optional Extra Practice

If you still have time this week, do one extra task:

Create a list of fake document filenames and produce a summary report with:

- total file count
- counts by extension
- longest filename
- files grouped into text-like vs non-text-like categories

No classes needed. Keep it simple and readable.
