from statistics import mean
from math import ceil


def count_non_zero_elements(seq):
    '''
    Funkcja zliczajaca ilosc jeszcze niezakonczonych procesow w danym ciagu.
    '''
    non_zero_cnt = 0
    for process in seq:
        if process > 0:
            non_zero_cnt += 1
    return non_zero_cnt


def find_remaining_non_zero_element(seq):
    '''
    Funkcja znajdujaca ostatni niezakonczony proces w danym ciagu.
    '''
    for idx, process in enumerate(seq):
        if process > 0:
            return idx


def roll_q(q, waiting_times_in_current_seq, current_idx, locked_idx):
    '''
    Funkcja dodajaca kolejne przeminiecie kwantu do procesow, ktore czekaja w kolejce.
    '''
    for wait_idx in range(len(waiting_times_in_current_seq)):
        # Funkcja nie zwiekszy czasu oczekiwania dla procesu, ktory sie w danej chwili wykonuje, ani dla procesow juz zakonczonych.
        if wait_idx != current_idx and wait_idx not in locked_idx:
            waiting_times_in_current_seq[wait_idx] += q


def count_q_needed(data, q):
    '''
    Funkcja obliczajaca ile kazdy proces potrzebuje kwantow, aby wykonac sie w calosci.
    '''
    q_needed_for_completion = []
    for seq in data:
        q_needed_for_completion_in_current_seq = []
        for process in seq:
            q_needed_for_completion_in_current_seq.append(ceil(process/q))
        q_needed_for_completion.append(q_needed_for_completion_in_current_seq)
    return q_needed_for_completion


def get_traversals(data, q):
    '''
    Funkcja zwracaja "diagramy Gantta" dla kazdego ciagu w zbiorze danych.
    '''
    q_needed_for_completion = count_q_needed(data, q)
    traversals = []
    for seq_idx, seq in enumerate(data):
        traversal_for_current_seq = []
        while any(q_needed_for_completion[seq_idx]) != 0:
            for process_idx in range(len(seq)):
                if q_needed_for_completion[seq_idx][process_idx] != 0:
                    traversal_for_current_seq.append(process_idx)
                    q_needed_for_completion[seq_idx][process_idx] -= 1
        traversals.append(traversal_for_current_seq)
    return traversals


def calculate_average_waiting_time(data, q):
    '''
    Funkcja obliczajaca sredni czas oczekiwania procesow ze wszystkich ciagow w podanych do niej danych.
    '''
    # Tablica, w ktorej zapisuje sredni czas oczekiwania procesow dla kazdego ciagu (seq)
    avg_waiting_times = []

    # Tablica, w ktorej przechowuje czasy oczekiwania procesow dla kazdego ciagu
    waiting_times_for_each_seq = []

    for seq in data:
        # Tablica, w ktorej zapisuje czas oczekiwania dla kazdego z procesow w aktualnym ciagu
        waiting_times_in_current_seq = [0]*len(seq)
        # Tablica indeksow procesow juz zakonczonych
        locked_idx = []

        # Petla wykonuje sie dopoki wszystkie procesy sie nie skoncza
        while any(seq) != 0:
            for idx, process in enumerate(seq):
                if count_non_zero_elements(seq) == 1:
                    locked_idx.append(find_remaining_non_zero_element(seq))
                if process <= q and idx not in locked_idx or count_non_zero_elements(seq) == 1:
                    process = 0
                    seq[idx] = process
                    locked_idx.append(idx)
                    roll_q(q, waiting_times_in_current_seq, idx, locked_idx)
                if process > 0:
                    process -= q
                    seq[idx] = process
                    roll_q(q, waiting_times_in_current_seq, idx, locked_idx)
        avg_waiting_times.append(mean(waiting_times_in_current_seq))
        waiting_times_for_each_seq.append(waiting_times_in_current_seq)
    return mean(avg_waiting_times), waiting_times_for_each_seq


def calculate_average_turnaround_time(data, q, traversals, waiting_times):
    avg_turnaround_times = []

    for seq_idx, seq in enumerate(data):
        turnaround_times_in_current_seq = []

        for process_idx, process in enumerate(seq):
            turnaround_times_in_current_seq.append(
                waiting_times[seq_idx][process_idx]+process)
        avg_turnaround_times.append(mean(turnaround_times_in_current_seq))
        print(turnaround_times_in_current_seq)
    return mean(avg_turnaround_times)
