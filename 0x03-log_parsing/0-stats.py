#!/usr/bin/python3
"""
parsing the output of generator code
"""
import sys

from datetime import datetime


if __name__ == '__main__':
    """
    The main function reads log lines from standard input,
    parses them, validates the IP address and datetime format,
    counts the occurrences of different status codes, and prints
    the total file size and the count of each status code every 10 lines.
    """

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

    def signal_handler(total_size, stat_dict):
        """
        The function `signal_handler` is a Python function
        that handles signals, printing the file size and
        resetting global variables before exiting.
        """
        print(f"File size: {total_size}")
        # total_size = 0
        for k, v in stat_dict.items():
            if v != 0:
                print(f"{k}: {v}")
                # stat_dict[k] = 0

    status_code = [200, 301, 400, 401, 403, 404, 405, 500]
    stat_dict = {k: 0 for k in status_code}
    total_size = 0
    i = 0
    try:
        for line in sys.stdin:
            line = line.rstrip().split(" ")
            try:
                ip_val = validate_ip(line[0])
                format_string = "%Y-%m-%d %H:%M:%S.%f"
                line[2] = line[2] + ' ' + line[3]
                line[2] = line[2].replace('[', '')
                line[2] = line[2].replace(']', '')
                parsed_datetime = datetime.strptime(line[2], format_string)
                if not ip_val or not isinstance(parsed_datetime, datetime):
                    raise ValueError("")
            except Exception:
                pass
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
            i += 1

            if i % 10 == 0:
                signal_handler(total_size, stat_dict)
                # signal_handler(total_size, stat_dict)
        signal_handler(total_size, stat_dict)
    except KeyboardInterrupt:
        signal_handler(total_size, stat_dict)
        raise
