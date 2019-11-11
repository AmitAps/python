import functools

def uppercase(func):
    @functools.wraps(func)
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

@uppercase
def greet():
    """Return a friendly greeting."""
    return 'Hello, Amit'
