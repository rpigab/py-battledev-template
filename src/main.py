#!/usr/bin/env python3

"""
Read input from STDIN
Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
Use: sys.stderr.write() to display debugging information to STDERR"""

import sys

input = (line.rstrip('\n') for line in sys.stdin)
output = sys.stdout
debug = lambda x: sys.stderr.write(x + '\n')

my_current_pos = int(sys.stdin.readline())

for line in input:
    [nb_who_overtook_me, nb_overtook_by_me] = [int(i) for i in line.split(' ')]
    my_current_pos = my_current_pos - nb_overtook_by_me + nb_who_overtook_me

# top 100
res = ''
if my_current_pos <= 100:
    res = '1000'
elif my_current_pos <= 10000:
    res = '100'
else:
    res = 'KO'

output.write(res)
