def parse():
    parsed_data = []
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            burst_times = list(int(i) for i in line.split(';') if i.isdigit())
            parsed_data.append(burst_times)
    return parsed_data
