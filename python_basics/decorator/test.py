import time
import logging


def log_slow_call(func=None, threshold=1):
    def decorator(func):
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
    if func is None:
        return decorator
    else:
        return decorator(func)


@log_slow_call()
def sleep_seconds(seconds):
    time.sleep(seconds)


if __name__ == "__main__":
    sleep_seconds(1)
