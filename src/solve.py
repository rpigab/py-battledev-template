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

    """
    Entrée
    
    Ligne 1: deux entiers séparés par un espace,
    N le nombre de câbles RJ11 et M le nombre de requêtes de vos ingénieurs, 
    N est compris entre 1 et 500 et M est compris entre 1 et 3N.
    Ligne 2 à M+1: deux entiers séparés par un espace 
    représentant la date de début et de fin d'une requête d'usage d'un cable RJ11. 
    Les entiers représentent le nombre de secondes écoulées depuis le 26 novembre 2019. 
    Ces entiers sont compris entre 0 et 2500. Les transferts de cable sont instantanés : 
    si un usage se termine à un temps T, le câble qu'il utilise peut être utilisé 
    pour un autre usage commençant à l'instant T.
    
    Sortie
    
    Une série d'entiers compris entre 1 et N et séparés par des espaces 
    indiquant le numéro câble attribué à chaque requête ou la chaine pas possible, 
    si a un moment donné vous n'avez pas assez de câble pour satisfaire toutes les requêtes.
    """

    [nb_cables, nb_requetes] = [int(i) for i in input_stream.readline().split(' ')]
    debug('nb_cables: {}, nb_requetes: {}'.format(nb_cables, nb_requetes))

    res = []
    # cable_courant = 0
    cables = [-1 for i in range(nb_cables)]
    for line in input_gen:
        [deb, fin] = [int(i) for i in line.split(' ')]
        cable_courant = 0
        used = False
        while cable_courant <= nb_cables:
            if deb >= cables[cable_courant]:
                # utiliser ce cable
                cables[cable_courant] = fin
                res.append(cable_courant+1)
                used = True
                break
            else:
                cable_courant += 1
                if cable_courant >= nb_cables:
                    cable_courant = 0
        if not used:
            output.write('pas possible')
            exit()
    debug(cables)

    # top 100
    output.write(' '.join([str(i) for i in res]))


if __name__ == '__main__':
    if len(sys.argv) == 3 and sys.argv[1] == 'file':
        with open(sys.argv[2], 'r') as input_f:
            solve(input_f, sys.stdout)
    else:
        solve(sys.stdin, sys.stdout)
