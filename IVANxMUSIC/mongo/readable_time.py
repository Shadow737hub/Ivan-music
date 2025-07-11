# readable_time.py
# Helper to convert seconds to human-readable time

def get_readable_time(seconds: int) -> str:
    """
    Convert seconds to a string like: 1d 3h 25m 17s
    """
    count = 0
    time_list = []
    time_suffix_list = ["s", "m", "h", "d"]

    while count < 4 and seconds > 0:
        if count == 0:
            remainder, result = divmod(seconds, 60)
        elif count == 1:
            remainder, result = divmod(seconds, 60)
        elif count == 2:
            remainder, result = divmod(seconds, 24)
        else:
            remainder, result = 0, seconds

        if result > 0:
            time_list.append(f"{int(result)}{time_suffix_list[count]}")
        seconds = remainder
        count += 1

    return " ".join(time_list[::-1]) if time_list else "0s"
