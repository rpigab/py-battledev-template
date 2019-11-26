#!/usr/bin/env python3

import sys


# noinspection PyUnusedLocal
def solve(
        input_stream,
        output_stream,
        debug=lambda x: sys.stderr.write(str(x) + '\n')):
    """Solves the problem,
    Reading input from input_stream and writing solution to output_stream
    Messages written to debug aren't written to output_stream
    """
    input_gen = (line.rstrip('\n') for line in input_stream)
    output = output_stream

    nb_personnes = int(input_stream.readline())
    res = ''
    longueur_p = 88888888
    for line in input_gen:
        [nom, longueur_s] = [i for i in line.split(' ')]
        longueur = int(longueur_s)
        if longueur < longueur_p:
            res = nom
            longueur_p = longueur

    output.write(res)


if __name__ == '__main__':
    if len(sys.argv) == 3 and sys.argv[1] == 'file':
        with open(sys.argv[2], 'r') as input_f:
            solve(input_f, sys.stdout)
    else:
        solve(sys.stdin, sys.stdout)
