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

    nb_cartons = int(input_stream.readline())

    poids_sur_montecharge = 0
    nb_allers_retours = 0

    for poids_carton in (int(i) for i in input_gen):
        total = poids_carton + poids_sur_montecharge
        if total > 100:
            # on envoie avec juste les cartons en cours, le courant sera seul sur le MC apres coup
            nb_allers_retours += 1
            poids_sur_montecharge = poids_carton
        else:
            # on rajoute le carton courant en plus sur le MC, on envoie pas
            poids_sur_montecharge = total
        debug('MC: {}, allers-retours: {}'.format(poids_sur_montecharge, nb_allers_retours))

    # un petit dernier pour la route
    nb_allers_retours += 1

    output.write(str(nb_allers_retours))


if __name__ == '__main__':
    if len(sys.argv) == 3 and sys.argv[1] == 'file':
        with open(sys.argv[2], 'r') as input_f:
            solve(input_f, sys.stdout)
    else:
        solve(sys.stdin, sys.stdout)
