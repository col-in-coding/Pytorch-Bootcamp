import time
import logging


def smart_decorator(decorator):

    def decorator_proxy(func=None, **kwargs):
        print(func)
        if func is not None:
            return decorator(func=func, **kwargs)

        def decorator_proxy(func):
            return decorator(func=func, **kwargs)

        return decorator_proxy

    return decorator_proxy


@smart_decorator
def log_slow_call(func, threshold=1):
    def proxy(*args, **kwargs):
        start_ts = time.time()
        result = func(*args, **kwargs)
        end_ts = time.time()

        seconds = end_ts - start_ts
        if seconds > 1:
            logging.warning('slow call: {name} in {seconds}s'.format(
                name=func.__name__,
                seconds=seconds,
            ))
        return result
    return proxy


# @log_slow_call
# def sleep_seconds(seconds):
#     time.sleep(seconds)

# smart_decorator(log_slow_call)(func=sleep_seconds)(seconds)


# @log_slow_call()
# def sleep_seconds(seconds):
#     time.sleep(seconds)

# smart_decorator(log_slow_call)(func=None)(sleep_seconds)(seconds)


@log_slow_call(threshold=2)
def sleep_seconds(seconds):
    time.sleep(seconds)

# smart_decorator(log_slow_call)(func=None, threshold=2)(sleep_seconds)(seconds)



if __name__ == "__main__":
    sleep_seconds(2)