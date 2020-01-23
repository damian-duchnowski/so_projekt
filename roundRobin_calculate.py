from statistics import mean
from parse_data import parse  # USUN TO!


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


def calculate_average_waiting_time(data, q):
    # Tablica, w ktorej zapisuje sredni czas oczekiwania procesow dla kazdego ciagu (seq)
    avg_waiting_times = []

    # Tablica przechowujaca "diagramy Gantta" na potrzebny funkcji obliczajacej sredni czas przetwarzania
    traversals = []

    for seq in data:
        # Tablica, w ktorej zapisuje czas oczekiwania dla kazdego z procesow w aktualnym ciagu
        waiting_times_in_current_seq = [0]*len(seq)
        # Tablica indeksow procesow juz zakonczonych
        locked_idx = []
        # Tablica zapisujaca "diagram Gantta" dla danego ciagu
        traversal = []

        # Petla wykonuje sie dopoki wszystkie procesy sie nie skoncza
        while any(seq) != 0:
            for idx, process in enumerate(seq):
                if count_non_zero_elements(seq) == 1:
                    locked_idx.append(find_remaining_non_zero_element(seq))
                if process <= q and idx not in locked_idx or count_non_zero_elements(seq) == 1:
                    process = 0
                    seq[idx] = process
                    locked_idx.append(idx)
                    traversal.append(idx)
                    roll_q(q, waiting_times_in_current_seq, idx, locked_idx)
                if process > 0:
                    process -= q
                    seq[idx] = process
                    traversal.append(idx)
                    roll_q(q, waiting_times_in_current_seq, idx, locked_idx)
        print("Traversal: " + str(traversal))  # DEBUG!
        print("Waiting times: " + str(waiting_times_in_current_seq))  # DEBUG!
        avg_waiting_times.append(mean(waiting_times_in_current_seq))
        traversals.append(traversal)
    return mean(avg_waiting_times), traversals


print(calculate_average_waiting_time(parse(), 1)[0])
