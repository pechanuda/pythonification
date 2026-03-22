# Lesson 02 Lecture

## Goal

Get comfortable with a few Python syntax patterns that show up constantly in scripts: slicing, unpacking, membership, and truthiness.

These are small features, but they change how Python code reads.

## Slicing

Slicing works on sequences like strings, lists, and tuples.

Examples:

```python
name = "invoice_001.pdf"

name[:7]      # from the start up to index 7
name[8:]      # from index 8 to the end
name[-3:]     # the last three characters
```

With lists:

```python
files = ["a.txt", "b.txt", "c.txt", "d.txt"]

files[:2]     # first two items
files[1:3]    # middle slice
files[-2:]    # last two items
```

Important idea:

Slicing is usually about expressing intent clearly, not about showing off syntax.

## Unpacking

Python can assign multiple values in one step.

```python
point = (10, 20)
x, y = point
```

This is also useful with lists:

```python
first, second = ["pdf", "txt"]
```

You can also capture the rest:

```python
first, *rest = ["pdf", "txt", "docx"]
```

Use unpacking when the shape is clear and fixed enough to read naturally.

## Membership

Use `in` and `not in` directly.

```python
if ".pdf" in filename:
    print("Looks like a PDF")

if "tmp" not in folder_names:
    print("No temp folder")
```

For many everyday checks, this is cleaner than writing a more ceremonial condition.

## Truthiness

In Python, these are falsey:

- `None`
- `False`
- `0`
- empty strings
- empty collections like `[]`, `{}`, and `set()`

Examples:

```python
if files:
    print("There is at least one file")

if not errors:
    print("No errors")
```

This is a normal Python style:

```python
if results:
    ...
```

Instead of:

```python
if len(results) > 0:
    ...
```

The shorter form is usually clearer.

## Python vs Java Reflexes

As a Java developer, one common habit is to write slightly more ceremony than Python needs.

Examples:

- using `len(items) == 0` instead of `if not items:`
- reaching for indexed loops too early
- manually splitting fixed-size values when unpacking is simpler

The Pythonic direction is usually:

1. trust the built-in behavior
2. express the shape of the data directly
3. keep the code short, but not clever

## Practical Rule

If a shorter Python form makes the code easier to read, prefer it.

If it makes the code feel compressed or tricky, keep the more explicit version.
