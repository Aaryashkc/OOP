# Python OOP and Advanced Python Lab

This repository is my personal learning space for getting better at Python beyond the basics.

I am using it to practice **object-oriented programming**, **dunder methods**, **inheritance**, **method resolution order**, **lambda expressions**, **pure functions**, **decorators**, **error handling**, **list comprehensions**, and other advanced Python ideas through small focused examples.

## What I Am Learning

- Object-oriented programming with classes and objects
- The role of `self` in instance methods
- Inheritance and code reuse
- Method Resolution Order (MRO)
- Dunder methods like `__str__`, `__repr__`, and operator-style behavior
- Lambda expressions and functional-style patterns
- Pure functions and cleaner program design
- Higher-order functions and decorators
- Basic authentication-style decorators
- Error handling with `try`, `except`, and `else`
- List, dictionary, and set comprehensions
- Finding duplicate values with comprehension logic
- Writing small exercises to make concepts stick

## Project Files

| File | Focus |
| --- | --- |
| `script.py` | Class basics, attributes, class methods, and static methods |
| `text.py` | Practice with classes, methods, and keyword arguments |
| `self.py` | Understanding `self` and object state |
| `inheritance.py` | Basic inheritance examples |
| `mro_algorithm.py` | Method Resolution Order practice |
| `dunder.py` | Dunder method experiments |
| `dunder_exercise.py` | Practice with special methods |
| `double.py` | Doubling list values with a function |
| `lambda_expression.py` | Lambda expression examples |
| `lambda_exercise.py` | Lambda practice area |
| `pure_functions.py` | Pure function examples |
| `pure_function_exercise.py` | Functional programming practice |
| `Higher_order_func.py` | Higher-order function basics |
| `decorator.py` | Simple decorator example |
| `authenticate_decorator.py` | Decorator exercise that checks whether a user is valid |
| `error_handling.py` | Exception handling practice with `ValueError`, `ZeroDivisionError`, and `TypeError` |
| `list_comprehension.py` | List, dictionary, and set comprehension examples |
| `comprehension_exercise.py` | Finding duplicate values using comprehension syntax |
| `exercise.py` | General Python exercises |

## Goal

The goal is simple: build a strong foundation in Python OOP and advanced Python concepts by writing code, breaking things, fixing them, and understanding why they work.

## How To Run

Run any file directly with Python:

```bash
python filename.py
```

Example:

```bash
python inheritance.py
```

To check all files for syntax errors:

```bash
python -m compileall -q .
```

## Current Review Notes

The code currently compiles successfully, but a few practice files still need cleanup:

- `error_handling.py`: converting a caught `TypeError` to text should use an f-string or comma-based `print`, not string concatenation with the exception object.
- `error_handling.py`: the custom `sum` function works, but it shadows Python's built-in `sum()` function.
- `exercise.py`: the cat instances should use string names like `'Simon'`, `'Sally'`, and `'Chilli'` instead of passing the class objects as names.
- `authenticate_decorator.py`: the decorator works for the current example, but it assumes the first argument exists and contains a `"valid"` key.

## Status

This is a work in progress. I will keep adding examples and exercises as I learn more.
