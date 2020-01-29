from parse_data import parse
from roundRobin_calculate import calculate_average_waiting_time, calculate_average_turnaround_time


def output(file_name):
    '''
    Funkcja dodajaca do pliku tekstowego wyniki danego algorytmu.
    Plik otwieram w trybie append, aby dodawac do niego kolejne wyniki roznych algorytmow.
    '''
    with open('output.txt', 'a') as f:
        for q in range(5, 20, 5):
            waiting_times = calculate_average_waiting_time(
                parse(file_name), q/10)[1]

            f.write('ROUND ROBIN (FCFS q=' + str(q/10) + '):' + '\n')
            f.write('---------------------------------------' + '\n')
            f.write('Sredni czas oczekiwania: ' +
                    str(round(calculate_average_waiting_time(parse(file_name), q/10)[0], 2)) + '\n')
            f.write('Sredni czas cyklu przetwarzania: ' +
                    str(round(calculate_average_turnaround_time(parse(file_name), q/10, waiting_times), 2)) + '\n')
            f.write('\n')

        for q in range(5, 20, 5):
            waiting_times = calculate_average_waiting_time(
                (seq[::-1] for seq in parse(file_name)), q/10)[1]

            f.write('ROUND ROBIN (LCFS q=' + str(q/10) + '):' + '\n')
            f.write('---------------------------------------' + '\n')
            f.write('Sredni czas oczekiwania: ' +
                    str(round(calculate_average_waiting_time((seq[::-1] for seq in parse(file_name)), q/10)[0], 2)) + '\n')
            f.write('Sredni czas cyklu przetwarzania: ' +
                    str(round(calculate_average_turnaround_time((seq[::-1] for seq in parse(file_name)), q/10, waiting_times), 2)) + '\n')
            f.write('\n')
