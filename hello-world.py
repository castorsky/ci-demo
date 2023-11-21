#!env python3

import os
import time
import ntplib

client = ntplib.NTPClient()
response = client.request('pool.ntp.org')
testTime = time.strftime('%m/%d/%Y %H:%M', time.localtime(response.tx_time))
question = os.getenv("CI", "Undefined")

print("Hello, world! The time is %s" % testTime)
print(f"Hello, Slurm! It's running inside CI - {question}")
