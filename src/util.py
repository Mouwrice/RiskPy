import time


def print_verbose(string: str, verbose: bool = True, verbose_duration: float = 1):
    if verbose:
        print(string)
        time.sleep(verbose_duration)
