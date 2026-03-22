# Lesson 02 Plan

## Theme

Slicing, unpacking, membership, and truthiness.

This lesson is still part of Week 1. The goal is to make short Python expressions feel readable instead of cryptic.

## Objectives

By the end of this lesson, you should be able to:

- read common slicing expressions on lists and strings
- use unpacking for small fixed-shape values
- use `in` and `not in` naturally
- rely on truthiness for simple control flow
- avoid overly defensive Java-style checks when Python already gives a clear idiom

## Time Budget

Target total: about 45-60 minutes.

Suggested split:

- 15 minutes reading the lecture
- 25-35 minutes solving the exercise
- 10 minutes reviewing and simplifying your code

## Workflow

1. Read [lecture.md](/Users/michael.linka/Udemy/pythonification/lessons/lesson_02/lecture.md)
2. Work in [exercise.py](/Users/michael.linka/Udemy/pythonification/lessons/lesson_02/exercise.py)
3. Solve with direct, readable code first
4. Refactor anything that feels too ceremonial
5. Bring the result back for review

## What Success Looks Like

Success means:

- you can read `items[:3]`, `items[-1]`, and `head, *tail = items` without hesitation
- you stop writing `len(items) > 0` when `if items:` is clearer
- membership checks start to feel like normal Python, not a special trick

## Common Mistakes to Avoid

- treating slicing syntax as something to memorize mechanically
- unpacking values when it makes the code less obvious
- replacing every explicit check with truthiness even when the meaning gets vague
- writing clever one-liners before the data shape is clear
