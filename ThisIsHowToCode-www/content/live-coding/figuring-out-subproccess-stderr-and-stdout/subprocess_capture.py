#!/usr/bin/env python3

import subprocess


### Pull STDOUT and STDERR into one variable 
### The order is not necessarily how it would appear
### on the command line. This is how I used to do it.

response1 = subprocess.run([
        'python.exe', 
        r'D:\ThisIsHowToCode\ThisIsHowToCode-www\content\live-coding\figuring-out-subproccess-stderr-and-stdout\send_out.py'
    ],
    stdout=subprocess.PIPE, 
    stderr=subprocess.STDOUT
    ).stdout.decode('utf-8').rstrip()

print(response1)


### This is the better way to do it. Available
### as of 3.7

response2 =  subprocess.run([
        'python.exe', 
        r'D:\ThisIsHowToCode\ThisIsHowToCode-www\content\live-coding\figuring-out-subproccess-stderr-and-stdout\send_out.py'
    ],
    capture_output=True
    )

print(response2.stdout.decode('utf-8').rstrip())
print(response2.stderr.decode('utf-8').rstrip())

