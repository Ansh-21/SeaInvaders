def debug(function):
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs, debug=True)
    return wrapper

def automatic(function):
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs, automatic=True)
    return wrapper