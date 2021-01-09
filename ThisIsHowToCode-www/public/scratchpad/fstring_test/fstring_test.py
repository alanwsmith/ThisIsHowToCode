#!/usr/bin/env python3

my_line_1 = "Hello, World"
print(my_line_1)
# outputs: Hello, World

my_line_2 = "Hello, {}".format("Universe")
print(my_line_2)
# outputs: Hello, Universe

my_line_3 = "Hello, {}"
print(my_line_3.format("Moon"))
# output: Hello, Moon


my_f_string = "Hello, {name}"
print(f"{my_f_string}")
# outputs: Hello, {name}

# Doesn't look like there's a way to pass
# variables in to the f-string to be
# replaced







