import psutil
import time
import sys
import matplotlib.pyplot as plt

def get_statistics(pid):
	process = psutil.Process(pid)

	file_cpu = open('cpuUsage.txt','w')
	file_memory = open('memoryUsage.txt','w')

	elapsed_time = 0
	while 1:
		cpu_usage = process.cpu_percent()
		memory_usage = (process.memory_info()[0])/(1024*1024)
		time.sleep(1)

		file_cpu.write(str(cpu_usage) + " " + str(elapsed_time) + "\n")
		file_memory.write(str(memory_usage) + " " + str(elapsed_time) + "\n")

		elapsed_time = elapsed_time + 1

	file_cpu.close()
	file_memory.close()

if __name__ == "__main__":
	get_statistics(44083)