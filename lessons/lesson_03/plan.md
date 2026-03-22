# Lesson 03 Plan

## Theme

Comprehensions and transformation patterns.

This lesson turns the ideas from Lesson 01 into more repetition. The point is not just to know the syntax, but to develop judgment about when comprehensions help.

## Objectives

By the end of this lesson, you should be able to:

- read list, set, and dict comprehensions comfortably
- translate a small loop into a comprehension when it improves clarity
- recognize filter, map, and grouping-like transformation patterns
- avoid writing a comprehension that is harder to read than the original loop

## Time Budget

Target total: about 45-60 minutes.

Suggested split:

- 15 minutes reading the lecture
- 25-35 minutes solving the exercise
- 10 minutes reviewing and rewriting one or two parts

## Workflow

1. Read [lecture.md](/Users/michael.linka/Udemy/pythonification/lessons/lesson_03/lecture.md)
2. Work in [exercise.py](/Users/michael.linka/Udemy/pythonification/lessons/lesson_03/exercise.py)
3. Solve with loops first where useful
4. Refactor at least half the sections into comprehensions
5. Bring back both your first pass and your cleaner pass if you want detailed review

## What Success Looks Like

Success means:

- you can read a comprehension without mentally reformatting it into Java
- you know when a normal loop is still the better choice
- your transformed results are correct and your code still feels readable

## Common Mistakes to Avoid

- forcing every loop into a comprehension
- putting too much logic inside a single expression
- using nested comprehensions before the simple case feels natural
- forgetting that clarity matters more than density
