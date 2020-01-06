from parse_data import parse
from fcfs_lcfs_sjf_calculate import *


def output():
    with open('output.txt', 'a') as f:
        f.write('SJF:' + '\n')
        f.write('---------------------------------------' + '\n')
        f.write('Sredni czas oczekiwania: ' +
                str(round(calculate_average_waiting_time(list(sorted(seq)) for seq in parse()), 2)) + '\n')
        f.write('Sredni czas cyklu przetwarzania: ' +
                str(round(calculate_average_turnaround_time(list(sorted(seq)) for seq in parse()), 2)) + '\n')
        f.write('\n')
