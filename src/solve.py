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

    taille_grille = int(input_stream.readline())

    multiplicateurs = []
    coins = []

    current_pos = (0,0)
    chemin = ''

    # trouver les bonus
    for y, line in enumerate(input_stream):
        for x, c in enumerate(line):
            if c == '*':
                multiplicateurs.append((x,y))
            elif c == 'o':
                coins.append((x,y))

    # les parcourir
    for elt in coins + multiplicateurs:
        if current_pos[0] < elt[0]:
            # go right
            chemin += '>' * (elt[0] - current_pos[0])
        elif current_pos[0] > elt[0]:
            # go left
            chemin += '<' * (current_pos[0] - elt[0])
        if current_pos[1] < elt[1]:
            # go down
            chemin += 'v' * (elt[1] - current_pos[1])
        elif current_pos[1] > elt[1]:
            # go up
            chemin += '^' * (current_pos[1] - elt[1])
        # assume we're at dest
        current_pos = elt
        # pickup
        chemin += 'x'

    output.write(chemin)


if __name__ == '__main__':
    if len(sys.argv) == 3 and sys.argv[1] == 'file':
        with open(sys.argv[2], 'r') as input_f:
            solve(input_f, sys.stdout)
    else:
        solve(sys.stdin, sys.stdout)
