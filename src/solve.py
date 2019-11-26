#!/usr/bin/env python3

import itertools
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

    if not inters or len(inters) == 0:
        output.write('KO')
        exit()

    mots = [''.join([c for c in m if c in inters]) for m in mots]
    debug(mots)

    possible_words = set()

    for mot in mots:
        res = [mot[x:y] for x, y in itertools.combinations(
            range(len(mot) + 1), r=2)]
        possible_words.update(res)

    debug('possible_words: ' + str(possible_words))

    possible_words2 = []

    for idx, m in enumerate(mots):
        possible_words2.append(set())
        for p in possible_words:
            p_i = 0
            m_t = ''
            for m_c in m:
                if p_i >= len(p):
                    continue
                if p[p_i] == m_c:
                    m_t += m_c
                p_i += 1
            # debug('m_t: {}'.format(m_t))
            possible_words2[idx].add(m_t)
            # debug('p: {}, m: {}'.format(p, m))
    debug(possible_words2)

    inters = possible_words2[0]
    for t in possible_words2[1:]:
        inters = inters.intersection(t)
    debug(inters)

    # maximum = max([len(m) for m in possible_words2])
    # debug(maximum)
    # possible_words2 = [m for m in possible_words2 if len(m) == maximum]
    # debug(possible_words2)
    output.write('KO')


if __name__ == '__main__':
    if len(sys.argv) == 3 and sys.argv[1] == 'file':
        with open(sys.argv[2], 'r') as input_f:
            solve(input_f, sys.stdout)
    else:
        solve(sys.stdin, sys.stdout)
