import time


def run_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        middle = float(end * 1000 - start * 1000)
        print(f"Time taken: {round(middle, 4)} seconds, result:", end=" ")
        return result

    return wrapper
