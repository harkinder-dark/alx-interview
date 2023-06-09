#!/usr/bin/python3
"""
Write a script that reads stdin line by line
and computes metrics
"""
import sys


if __name__ == '__main__':

    def printer(size: int, code: dict) -> None:
        """
        printer function
        """
        print("File size: {:d}".format(size))
        for key, val in sorted(code.items()):
            if val:
                print("{}: {}".format(key, val))

    size = 0
    i = 0
    status = ["200", "301", "400", "401", "403", "404", "405", "500"]
    code = {key: 0 for key in status}
    try:
        for url in sys.stdin:
            line = url.split()
            i += 1
            try:
                size += int(line[-1])
            except Exception:
                pass
            try:
                stat = line[-2]
                if stat in code:
                    code[stat] += 1
            except Exception:
                pass
            if i % 10 == 0:
                printer(size, code)
        printer(size, code)
    except KeyboardInterrupt:
        printer(size, code)
        raise
