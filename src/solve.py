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
    cables = [None for i in range(nb_cables)]

    for line in input_gen:
        [debut_requete, fin_requete] = [int(i) for i in line.split(' ')]
        cable_courant = 0
        used = False
        while cable_courant <= nb_cables:
            # Si le cable n'est pas encore utilisé
            # ou qu'il n'est utilisé que jusqu'à un instant inférieur au début de la requête
            if not cables[cable_courant] or debut_requete >= cables[cable_courant]:
                # Utiliser ce cable
                # On stocke dans le, tableau d'utilisation des cables la date de fin
                # Pour savoir à quel moment il sera à nouveau disponible
                cables[cable_courant] = fin_requete
                res.append(cable_courant + 1)
                used = True
                break
            else:
                # Avancer l'indice pour tester le cable suivant au prochain passage de la boucle while
                cable_courant += 1
                if cable_courant >= nb_cables:
                    cable_courant = 0
        # Si aucun des N cables n'est disponible pour cette requête, indiquer que c'est impossible
        if not used:
            output.write('pas possible')
            exit()

    debug(cables)

    # Écrire la solution
    output.write(' '.join([str(i) for i in res]) + '\n')


if __name__ == '__main__':
    if len(sys.argv) == 3 and sys.argv[1] == 'file':
        with open(sys.argv[2], 'r') as input_f:
            solve(input_f, sys.stdout)
    else:
        solve(sys.stdin, sys.stdout)
