# Lesson 04 Lecture

## Goal

Combine the Week 1 concepts into one practical exercise that feels closer to real scripting work.

At this point, the challenge is less about isolated syntax and more about making small design choices well.

## The Main Questions to Ask

When you look at a small Python task, ask:

1. What is the shape of the data?
2. What output do I need?
3. Which built-in collection fits that output naturally?
4. Would a loop or a comprehension be clearer here?

These questions matter more than memorizing syntax.

## Choosing Collection Types

Use:

- `list` when order matters or you want all matching items
- `set` when uniqueness or fast membership is the point
- `dict` when you need lookup, counting, or named fields

For record-like data, a `dict` is still fine at this stage.

## Keep Script Logic Honest

A common early mistake is to add structure before the code earns it.

That can look like:

- creating classes for a four-line exercise
- splitting simple logic into too many helper functions
- over-commenting obvious code

Right now, favor:

- direct transformations
- descriptive variable names
- one level of abstraction at a time

## Review Questions

After you solve the exercise, review your code with these questions:

- Is any loop longer than it needs to be?
- Is any comprehension harder to read than the loop version?
- Did I choose the right data structure?
- Did I write anything because of Java habit rather than Python need?

This review habit is part of becoming productive, not an optional cleanup step.
