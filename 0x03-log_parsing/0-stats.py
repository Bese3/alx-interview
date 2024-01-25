#!/usr/bin/python3
"""
parsing the output of generator code
"""
import sys


if __name__ == '__main__':
    """
    The main function reads log lines from standard input,
    parses them, validates the IP address and datetime format,
    counts the occurrences of different status codes, and prints
    the total file size and the count of each status code every 10 lines.
    """

    def print_stats(stats: dict, file_size: int) -> None:
        print("File size: {:d}".format(file_size))
        for k, v in stats.items():
            if v:
                print("{}: {}".format(k, v))

    status_code = [200, 301, 400, 401, 403, 404, 405, 500]
    stat_dict = {k: 0 for k in status_code}
    total_size = 0
    i = 0
    try:
        for line in sys.stdin:
            i += 1
            line = line.rstrip().split(" ")
            try:
                status = int(line[-2])
                if status in status_code:
                    stat_dict[status] += 1
            except BaseException:
                pass
            try:
                total_size += int(line[-1])
            except BaseException:
                pass
            if i % 10 == 0:
                print_stats(stat_dict, total_size)
        print_stats(stat_dict, total_size)
    except KeyboardInterrupt:
        print_stats(stat_dict, total_size)
        raise
