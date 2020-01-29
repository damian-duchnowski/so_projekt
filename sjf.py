from parse_data import parse
from fcfs_lcfs_sjf_calculate import calculate_average_waiting_time, calculate_average_turnaround_time


def output(file_name):
    '''
    Funkcja dodajaca do pliku tekstowego wyniki danego algorytmu.
    Plik otwieram w trybie append, aby dodawac do niego kolejne wyniki roznych algorytmow.
    '''
    with open('output.txt', 'a') as f:
        f.write('SJF:' + '\n')
        f.write('---------------------------------------' + '\n')
        f.write('Sredni czas oczekiwania: ' + str(round(
            calculate_average_waiting_time(list(sorted(seq)) for seq in parse(file_name)), 2)) + '\n')
        f.write('Sredni czas cyklu przetwarzania: ' + str(round(
            calculate_average_turnaround_time(list(sorted(seq)) for seq in parse(file_name)), 2)) + '\n')
        f.write('\n')
