#!/usr/bin/env python3

import sys


# noinspection PyUnusedLocal
def solve(
        input_stream,
        output_stream,
        debug=lambda x: sys.stderr.write(x + '\n')):
    """Solves the problem,
    Reading input from input_stream and writing solution to output_stream
    Messages written to debug aren't written to output_stream
    """
    input_gen = (line.rstrip('\n') for line in input_stream)
    output = output_stream

    my_current_pos = int(input_stream.readline())

    for line in input_gen:
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


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        with open(sys.argv[1], 'r') as input_f:
            solve(input_f, sys.stdout)
    else:
        solve(sys.stdin, sys.stdout)
