import psutil
import time
import sys
import matplotlib.pyplot as plt

# Get PID of the process via
# ps aux | grep mongod | grep -v grep | awk '{print $2}'

def get_statistics(pid):
	process = psutil.Process(pid)

	file_cpu = open('cpuUsage.txt','w')
	file_memory = open('memoryUsage.txt','w')

	# To keep track of the time since the start of the program
	elapsed_time = 0

	while 1:
		cpu_usage = process.cpu_percent()
		memory_usage = (process.memory_info()[0])/(1024*1024) # in MB
		time.sleep(1) # This can vary according to usage

		file_cpu.write(str(cpu_usage) + " " + str(elapsed_time) + "\n")
		file_memory.write(str(memory_usage) + " " + str(elapsed_time) + "\n")

		elapsed_time = elapsed_time + 1

	file_cpu.close()
	file_memory.close()

if __name__ == "__main__":
	get_statistics(44083)