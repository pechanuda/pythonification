# Pythonification High-Level Plan

## Goal

Learn Python efficiently as a software engineer coming from Java, with emphasis on:

- writing idiomatic Python instead of Java-shaped Python
- building maintainable CLI and backend-style applications
- handling files, text, JSON, and document-processing workflows
- using professional tooling and testing practices

This track is intentionally not focused on data science. It is aimed at application development around unstructured data and document-processing systems.

## Working Assumptions

- Available study time: 3-5 hours per week
- Learning style: mix of structured curriculum and mentor-style iteration
- Existing strengths: core programming basics, OOP, terminal usage, Java experience
- Platforms: macOS and Windows via WSL

## Study Method

Each week should usually have:

- one core topic
- one hands-on exercise set
- one review and refactor pass
- occasional mini-project milestones

Recommended weekly rhythm:

- 45-60 minutes to learn the concepts
- 60-90 minutes to solve exercises
- 30-45 minutes to review, refactor, and discuss tradeoffs
- optional extra time to extend or test the solution

## Principles

- Skip beginner programming basics you already know
- Focus on Python idioms, not just syntax
- Prefer small hands-on tasks over passive reading
- Use tooling early so the workflow feels real
- Build toward document and text processing use cases
- Refactor often to improve readability and design judgment

## 10-Week Roadmap

### Week 1: Python Mindset and Core Collections

Focus:

- `list`, `dict`, `set`, tuples
- slicing and unpacking
- comprehensions
- truthiness and membership
- reading simple Python expressions comfortably

Outcome:

You should be able to read and write small Python scripts that transform data cleanly.

### Week 2: Functions, Exceptions, and Type Hints

Focus:

- function design
- default parameters
- return values
- exception basics
- practical type hints

Outcome:

You should be able to write small reusable functions with readable signatures and controlled error handling.

### Week 3: Files, Paths, and Text Processing

Focus:

- `pathlib`
- reading and writing files
- encodings
- line-by-line processing
- simple regex usage

Outcome:

You should be able to safely process folders and text files in a cross-platform way.

### Week 4: Project Structure and Tooling

Focus:

- modules and imports
- `venv`
- dependency installation
- `pyproject.toml`
- `ruff`
- `pytest`

Outcome:

You should understand how a real Python repository is structured and why these tools are used.

### Week 5: Classes, Dataclasses, and Pythonic Design

Focus:

- when to use classes
- when functions are enough
- `dataclass`
- simple object modeling

Outcome:

You should be able to model domain data without overengineering.

### Week 6: CLI Applications

Focus:

- `argparse`
- entrypoints
- parsing input
- printing useful output
- exit codes and errors

Outcome:

You should be able to build small command-line tools that behave like real software.

### Week 7: JSON, CSV, and Document Metadata Workflows

Focus:

- JSON and CSV handling
- data normalization
- metadata extraction
- shaping intermediate representations

Outcome:

You should be able to build the core data plumbing used by document-processing systems.

### Week 8: Testing Properly with Pytest

Focus:

- test structure
- assertions
- fixtures
- testing file-related code
- temporary directories

Outcome:

You should be able to protect logic with readable tests and refactor with more confidence.

### Week 9: Refactoring and Application Architecture

Focus:

- separating domain logic from I/O
- keeping scripts maintainable
- avoiding tightly coupled designs
- organizing modules clearly

Outcome:

You should be able to evolve a script into a maintainable small application.

### Week 10: Mini Capstone

Focus:

- combine parsing, validation, reporting, and CLI structure
- build a small document intake/reporting tool

Outcome:

You should finish with a realistic project that reflects the kind of work you want to do.

## Why These Tools Matter

### `venv`

Purpose:

Isolate dependencies per project.

Why it matters:

Different projects need different package versions. Using `venv` keeps your environment predictable and avoids machine-wide dependency conflicts.

### `pytest`

Purpose:

Run tests with concise syntax and good ergonomics.

Why it matters:

It is easier to read and write than the built-in `unittest` in many real-world teams, especially when testing small units of logic and file workflows.

### `ruff`

Purpose:

Lint and format code quickly.

Why it matters:

It keeps style consistent, catches common mistakes, and is fast enough that it does not get in the way of your workflow.

## First Mini-Projects

These are better starting projects than a game because they map directly to your target domain:

1. File inventory CLI
2. Text report analyzer
3. Document intake pipeline
4. Rule-based document classifier

## Mentor Workflow

For each lesson:

1. Learn a focused Python topic
2. Solve one or more small exercises
3. Get a code review
4. Refactor based on feedback
5. Periodically combine lessons into mini-projects

The main goal is not just to get code working. It is to learn how Python code should look and how to design it cleanly.
