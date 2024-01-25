#!/usr/bin/python3
"""
parsing the output of generator code
"""
import sys
import signal
from datetime import datetime
total_size = 0
stat_dict = {}


def validate_ip(ip_ad: str) -> bool:
    """
    The function `validate_ip` takes a string representing an
    IP address and returns True if it is a valid IP address and
    False otherwise.
    """
    parts = ip_ad.split(".")

    if len(parts) != 4:
        return False

    for part in parts:
        if not isinstance(int(part), int):
            return False

        if int(part) < 0 or int(part) > 255:
            return False

    return True


def signal_handler(sig, frame):
    """
    The function `signal_handler` is a Python function
    that handles signals, printing the file size and
    resetting global variables before exiting.
    """
    global total_size
    print(f"File size: {total_size}")
    total_size = 0
    global stat_dict
    for k, v in stat_dict.items():
        if v != 0:
            print(f"{k}: {v}")
            stat_dict[k] = 0
    exit(0)


signal.signal(signal.SIGINT, signal_handler)


def main():
    """
    The main function reads log lines from standard input,
    parses them, validates the IP address and datetime format,
    counts the occurrences of different status codes, and prints
    the total file size and the count of each status code every 10 lines.
    """
    status_code = [200, 301, 400, 401, 403, 404, 405, 500]
    global stat_dict
    stat_dict = {200: 0, 301: 0, 400: 0,
                 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    global total_size
    i = 0
    for line in sys.stdin:
        line = line.rstrip().split(" ")
        try:
            ip_val = validate_ip(line[0])
            format_string = "%Y-%m-%d %H:%M:%S.%f"
            line[2] = line[2] + ' ' + line[3]
            line[2] = line[2].replace('[', '')
            line[2] = line[2].replace(']', '')
            # print(len(line))
            parsed_datetime = datetime.strptime(line[2], format_string)

            if not ip_val or not isinstance(parsed_datetime, datetime):
                raise ValueError("")
            if int(line[7]) not in status_code:
                raise ValueError("")
            stat_dict[int(line[7])] += 1
            total_size += int(line[8])
            i += 1
            if i == 10:
                i = 0
                print(f"File size: {total_size}")
                total_size = 0
                for k, v in stat_dict.items():
                    if v != 0:
                        print(f"{k}: {v}")
                    stat_dict[k] = 0
        except KeyboardInterrupt:
            signal_handler()
        except (ValueError):
            continue


if __name__ == '__main__':
    main()
