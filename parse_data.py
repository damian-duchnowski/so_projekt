def parse():
    '''
    Funkcja wczytujaca dane z pliku.
    '''
    # Tablica, w ktorej przechowuje odczytane dane w postaci listy ciagow procesow (lista list dok)
    parsed_data = []
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            burst_times = list(int(i) for i in line.split(';') if i.isdigit())
            parsed_data.append(burst_times)
    return parsed_data
