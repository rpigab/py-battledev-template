#!/usr/bin/env python3

import sys
import itertools

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

    """
    Entrée

    Ligne 1 : 3 entiers séparés par des espaces : N le nombre de pierres précieuses, M le nombre de types de poudres,
    C la quantité (en gramme) de pierres ou poudre que peux contenir la lampe, chacun compris entre 1 et 100.
    Lignes 2 à N + 1 : 2 entiers séparés par des espaces, respectivement la valeur (en pièces d'or)
    et le poids (en grammes) de chaque pierre précieuse, compris respectivement entre 1 et 1000 et 1 et C
    Lignes N + 2 à N + M + 2 : 2 entiers séparés par des espaces,
    respectivement le prix au poids (en pièces d'or par gramme)
    et la quantité disponible (en grammes) de chaque type de poudre, compris respectivement entre 1 et 100 et 1 et C.
    
    Sortie
    
    La valeur maximale que peux contenir la lampe en pierres précieuses et poudres !
    """

    [nb_pierres_precieuses, nb_types_poudres, qte_contenance] = [int(i) for i in input_stream.readline().split(' ')]

    for line in itertools.islice(input_gen, nb_pierres_precieuses):
        [valeur, poids] = [int(i) for i in line.split(' ')]
    for line in itertools.islice(input_gen, nb_types_poudres):
        [valeur, poids] = [int(i) for i in line.split(' ')]

    output.write('')


if __name__ == '__main__':
    if len(sys.argv) == 3 and sys.argv[1] == 'file':
        with open(sys.argv[2], 'r') as input_f:
            solve(input_f, sys.stdout)
    else:
        solve(sys.stdin, sys.stdout)
