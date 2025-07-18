TEMPLATE = """
You are a helpful assistant that writes docstrings in the NumPy Python documentation style.

Given the following Python function, insert a proper docstring that describes what the function does, its arguments, and return type.

Output the updated function with the docstring included. Output only the codes, no need for triple backticks.

Function:
```python
{code}
```
"""


def get_prompt(code: str) -> str:
    return TEMPLATE.format(code=code.strip())
