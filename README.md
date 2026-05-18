# Python Learning Lab

This repository is a personal Python practice workspace. It contains small, focused scripts for learning object-oriented programming, functional programming tools, decorators, error handling, comprehensions, string handling, and simple validation exercises.

Most files are standalone examples. They are meant to be run one at a time while learning or experimenting.

## Topics Covered

- Classes, objects, attributes, instance methods, class methods, and static methods
- `self`, inheritance, `super()`, subclass checks, and Method Resolution Order
- Dunder methods such as `__str__` and `__len__`
- List, dictionary, and set comprehensions
- Lambda expressions, `map()`, `filter()`, `zip()`, and `reduce()`
- Pure functions and functional-style exercises
- Basic decorators and an authentication-style decorator
- Error handling with `try`, `except`, `else`, `finally`, and `raise`
- Simple data transformation exercises
- Caesar cipher encryption/decryption
- Input validation for a small RPG character generator

## File Guide

| File | Focus |
| --- | --- |
| `script.py` | Class basics, object attributes, class methods, static methods, and finding the oldest cat |
| `text.py` | Classes, instance methods, keyword arguments, and repeated class definitions for practice |
| `self.py` | Inheritance with `super()` and passing parent-class data into a child class |
| `inheritance.py` | Basic inheritance and `isinstance()` checks |
| `mro_algorithm.py` | Method Resolution Order examples with multiple inheritance |
| `dunder.py` | Custom `__str__` and `__len__` behavior |
| `dunder_exercise.py` | Extending the built-in `list` type and overriding `__len__` |
| `double.py` | Function that doubles each value in a list |
| `lambda_expression.py` | `lambda`, `map()`, `filter()`, and `reduce()` examples |
| `lambda_exercise.py` | Squaring values with `lambda` and manually sorting numbers from highest to lowest |
| `pure_functions.py` | `map()`, `filter()`, `zip()`, and `reduce()` with named helper functions |
| `pure_function_exercise.py` | Functional programming exercises using pet names, zipped lists, filtered scores, and `reduce()` |
| `Higher_order_func.py` | Notes placeholder for higher-order functions |
| `decorator.py` | Simple custom decorator example |
| `authenticate_decorator.py` | Decorator that only runs a function when the user dictionary has `valid: True` |
| `error_handling.py` | Interactive exception-handling practice with age input, division, custom errors, and `finally` |
| `list_comprehension.py` | List, dictionary, and set comprehension examples |
| `comprehension_exercise.py` | Finding duplicate values with comprehension syntax |
| `exercise.py` | Inheritance exercise with `Pets`, `Cat`, and several cat subclasses |
| `caesar_cipher_exercise.py` | Caesar cipher helper with `encrypt()` and `decrypt()` functions |
| `rpg_character.py` | RPG character validator for name and stat rules |
| `script1.py` | String concatenation, f-strings, slicing, and employee-code parsing |
| `texting.py` | Integer and float floor division examples |

## How To Run

Run any script directly:

```bash
python filename.py
```

On this project, the local virtual environment also has Python available:

```bash
.\.venv\Scripts\python.exe filename.py
```

Examples:

```bash
.\.venv\Scripts\python.exe inheritance.py
.\.venv\Scripts\python.exe caesar_cipher_exercise.py
```

Some files are interactive and wait for terminal input. For example:

- `error_handling.py` asks for ages with `input()`.

## Syntax Check

To check every current Python file for syntax errors with the local virtual environment:

```bash
.\.venv\Scripts\python.exe -m py_compile authenticate_decorator.py caesar_cipher_exercise.py comprehension_exercise.py decorator.py double.py dunder.py dunder_exercise.py error_handling.py exercise.py Higher_order_func.py inheritance.py lambda_exercise.py lambda_expression.py list_comprehension.py mro_algorithm.py pure_functions.py pure_function_exercise.py rpg_character.py script.py script1.py self.py text.py texting.py
```

The current files compile successfully with the command above.

## Current Review Notes

- `python` is not currently available on PATH in this shell, but `.\.venv\Scripts\python.exe` works.
- `exercise.py` currently creates cats with class objects as names, such as `Simon(Simon, 5)`. String names like `"Simon"` would make the output clearer.
- `authenticate_decorator.py` assumes the first positional argument exists and has a `"valid"` key.
- `error_handling.py` defines a custom function named `sum`, which shadows Python's built-in `sum()` function.
- `error_handling.py` intentionally raises `ValueError("hey cut it out")` in the second input loop, so that section is for exception practice rather than normal app flow.
- `rpg_character.py` appears to contain encoded display symbols for stat bars. If the terminal displays strange characters, replace them with plain ASCII or save the file as UTF-8 with the intended symbols.
- Several files print intermediate values directly. That is fine for learning scripts, but future reusable code would be easier to test if logic lived in functions and printing stayed in a small `if __name__ == "__main__":` block.

## Suggested Next Steps

1. Clean up small naming issues such as `sum`, `Capatalize_name`, and mixed capitalization.
2. Move repeated demo code under `if __name__ == "__main__":`.
3. Add short comments only where the example is teaching a specific concept.
4. Convert a few exercises into testable functions with expected inputs and outputs.

## Status

This is a work-in-progress learning repository. The goal is to keep adding small examples while improving the clarity, correctness, and organization of each script over time.
