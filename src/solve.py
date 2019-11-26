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

    res = ''

    nb_mots = int(input_stream.readline())
    mots = [i for i in input_gen]
    sets = [set(i) for i in mots]

    debug(mots)

    inters = sets[0]
    for s in sets[1:]:
        inters = inters.intersection(s)

    inters = str(inters)
    debug(inters)

    mots_n = []
    min_chars = 0
    for mot in mots:
        mot_n = [c for c in mot if c in inters]
        min_chars = len(mot_n)
        mots_n.append(''.join(mot_n))

    mots_n = ''.join([m for m in mots_n if len(m) == min_chars])
    debug(mots_n)

    output.write(mots_n)


if __name__ == '__main__':
    if len(sys.argv) == 3 and sys.argv[1] == 'file':
        with open(sys.argv[2], 'r') as input_f:
            solve(input_f, sys.stdout)
    else:
        solve(sys.stdin, sys.stdout)
