from random import randint


def generate(values_per_seq, seqs, file_name):
    '''
    Funkcja generujaca pseudolosowe wartosci czasu obslugi w zadanych ilosciach i zapisujaca je.
    '''
    with open(file_name, 'w') as f:
        for _ in range(seqs):
            burst_times = []
            for burst in range(values_per_seq):
                burst_times.append(randint(1, 20))
                f.write(str(burst_times[burst]) + ';')
            f.write('\n')
