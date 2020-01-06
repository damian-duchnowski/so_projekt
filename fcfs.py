from parse_data import parse
from fcfs_lcfs_sjf_calculate import *


def output():
    with open('output.txt', 'a') as f:
        f.write('FCFS:' + '\n')
        f.write('---------------------------------------' + '\n')
        f.write('Sredni czas oczekiwania: ' +
                str(round(calculate_avereage_waiting_time(parse()), 2)) + '\n')
        f.write('Sredni czas cyklu przetwarzania: ' +
                str(round(calculate_average_turnaround_time(parse()), 2)) + '\n')
        f.write('\n')
