#!/usr/bin/python3
for i in range(97, 123):
    if chr(i) not in 'eq':
        print("".format(chr(i)), end="")
