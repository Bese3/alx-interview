#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

for i in range(10000):
    sleep(random.random())
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now(),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)
    ))
    sys.stdout.flush()
# my_list = ['202.63.250.102 - [2024-01-25 20:10:11.823681] "GET /projects/260 HTTP/1.1" 500 67',
# '58.70.209.187 - [2017-02-05 23:28:50.564010] "GET /projects/260 HTTP/1.1" 401 708',
# '125.218.201.102 - [2017-02-05 23:28:51.484960] "GET /projects/260 HTTP/1.1" 500 684',
# '93.202.122.198 - [2017-02-05 23:28:52.060026] "GET /projects/260 HTTP/1.1" 500 1002',
# '83.93.222.77 - [2017-02-05 23:28:52.920758] "GET /projects/260 HTTP/1.1" 200 551',
# '186.161.131.204 - [2017-02-05 23:28:53.006680] "GET /projects/260 HTTP/1.1" 500 665',
# '61.146.36.164 - [2017-02-05 23:28:53.792909] "GET /projects/260 HTTP/1.1" 401 299',
# '70.139.77.18 - [2017-02-05 23:28:54.747004] "GET /projects/260 HTTP/1.1" 403 543',
# '241.71.80.100 - [2017-02-05 23:28:55.573972] "GET /projects/260 HTTP/1.1" 500 222',
# '219.109.138.129 - [2017-02-05 23:28:55.755290] "GET /projects/260 HTTP/1.1" 200 186',
# '118.99.189.189 - [2017-02-05 23:28:56.091266] "GET /projects/260 HTTP/1.1" 403 278']
# for line in my_list:
#     print(line)