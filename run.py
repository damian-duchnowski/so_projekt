import generate_data
import fcfs
import lcfs
import sjf
import roundRobin
import time

start_time = time.time()

file_name = 'input.txt'
generate_data.generate(100, 100, file_name)
fcfs.output(file_name)
lcfs.output(file_name)
sjf.output(file_name)
roundRobin.output(file_name)

end_time = time.time()

print('Czas wykonywania skryptu: ' + str(round(end_time-start_time, 2)) + 's')
