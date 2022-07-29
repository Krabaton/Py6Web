import time


def get_current_time_milli():
    return int(round(time.time() * 1000))


def debouncer(callback, throttle_time_limit=100):
    last_millis = get_current_time_milli()

    def throttle(*args):
        nonlocal last_millis
        curr_millis = get_current_time_milli()
        if (curr_millis - last_millis) > throttle_time_limit:
            last_millis = get_current_time_milli()
            return callback(*args)
    return throttle