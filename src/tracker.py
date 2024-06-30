#I don't fully understand the decorator function but I searched for a way to keep track of the actions.

def log_action(action):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(f"'{action}'.")
            return result
        return wrapper
    return decorator
