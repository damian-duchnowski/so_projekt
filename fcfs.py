from parse_data import parse
from statistics import mean


def calculate_avereage_waiting_time():
    # Tablica, w ktorej zapisuje sredni czas oczekiwania procesow dla kazdego ciagu
    avg_waiting_times = []

    for seq in parse():
        waiting_times_in_current_seq = []
        for idx, process in enumerate(seq):
            waiting_times_in_current_seq.append(sum(seq[:idx]))
        avg_waiting_times.append(mean(waiting_times_in_current_seq))

    return mean(avg_waiting_times)


def calculate_average_turnaround_time():
    # Tablica, w ktorej zapisuje sredni czas cyklu przetwarzania dla kazdego ciagu
    avg_turnaround_times = []

    for seq in parse():
        turnaround_times_in_current_seq = []
        for idx, process in enumerate(seq):
            turnaround_times_in_current_seq.append(sum(seq[:idx])+process)
        avg_turnaround_times.append(mean(turnaround_times_in_current_seq))

    return mean(avg_turnaround_times)


def output():
    with open('output.txt', 'a') as f:
        f.write('FCFS:' + '\n')
        f.write('--------------------------------------' + '\n')
        f.write('Sredni czas oczekiwania: ' +
                str(round(calculate_avereage_waiting_time(), 2)) + '\n')
        f.write('Sredni czas cyklu przetwarzania: ' +
                str(round(calculate_average_turnaround_time(), 2)) + '\n')
        f.write('\n')
