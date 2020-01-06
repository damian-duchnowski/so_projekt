from statistics import mean
from parse_data import parse  # USUN TO!


def calculate_average_waiting_time(data, q):
    # Tablica, w ktorej zapisuje sredni czas oczekiwania procesow dla kazdego ciagu (seq)
    avg_waiting_times = []

    # TODO: Sprawdzaj czy jakis element jest zerowy przed zrobieniem kolejnej iteracji petli i sztucznym zwiekszeniem ilosci wykonanych kwantow
    for seq in data:
        waiting_times_in_current_seq = []
        elapsed_q = 0
        while any(process != 0 for process in seq):
            for idx, process in enumerate(seq):
                if process-q >= 0:
                    process -= q
                    seq[idx] = process
                    elapsed_q += 1
                else:
                    waiting_times_in_current_seq.append(q*elapsed_q)
                    del seq[idx]
        avg_waiting_times.append(mean(waiting_times_in_current_seq))
    return mean(avg_waiting_times)


print(calculate_average_waiting_time(parse(), 0.5))
