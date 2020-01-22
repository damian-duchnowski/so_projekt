from statistics import mean


def calculate_average_waiting_time(data):
    # Tablica, w ktorej zapisuje sredni czas oczekiwania procesow dla kazdego ciagu (seq)
    avg_waiting_times = []

    for seq in data:
        waiting_times_in_current_seq = []
        for idx in range(len(seq)):
            waiting_times_in_current_seq.append(sum(seq[:idx]))
        avg_waiting_times.append(mean(waiting_times_in_current_seq))

    return mean(avg_waiting_times)


def calculate_average_turnaround_time(data):
    # Tablica, w ktorej zapisuje sredni czas cyklu przetwarzania dla kazdego ciagu (seq)
    avg_turnaround_times = []

    for seq in data:
        turnaround_times_in_current_seq = []
        for idx, process in enumerate(seq):
            turnaround_times_in_current_seq.append(sum(seq[:idx])+process)
        avg_turnaround_times.append(mean(turnaround_times_in_current_seq))

    return mean(avg_turnaround_times)
