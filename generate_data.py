from random import randint


def generate():
    with open('input.txt', 'w') as f:
        for line in range(3):
            burst_times = []
            for burst in range(3):
                burst_times.append(randint(1, 20))
                f.write(str(burst_times[burst]) + ';')
            f.write('\n')
