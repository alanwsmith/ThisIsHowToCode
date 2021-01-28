---
title: Capturing STDOUT and STDERR with Python's subprocess
date: 1611716665
--- 

I'm not sure how I ended up on the path, but I used to jump through a bunch of hoops to capture both STDOUT and STDERR from Python's subprocess modules. As of 3.7, it's straight forward with the `capture_output`. It's as easy as:

    response = subprocess.run(['PROCESS_TO_RUN'], capture_output=True)

The values are in:

    response.stdout
    and
    response.stderr

The values are encoded and generally have a newline at the end of them. So you'll want to access them with something like:

    print(response.stdout.decode('utf-8').rstrip())
    print(response.stderr.decode('utf-8').rstrip())

Checkout the sibling scripts to see the earlier example and a test case. 

### Links

- https://docs.python.org/3/library/subprocess.html
- https://stackoverflow.com/q/31833897/102401
- https://stackoverflow.com/q/1956142/102401
- https://stackoverflow.com/q/5574702/102401
