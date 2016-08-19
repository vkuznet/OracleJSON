import matplotlib.pyplot as plt

def draw_charts():
	# CPU Statistics
	with open('cpuUsage.txt') as f1:
		data1 = f1.read()
	
	# In cpuUsage.txt, the first column refers to the CPU Usage 
	# and the second column refers to the time
	data1 = data1.split('\n')

	x1 = []
	y1 = []

	for row in range(len(data1)-1):
		x1.append(data1[row].split(' ')[1])
		y1.append(data1[row].split(' ')[0])

	# Memory Statistics
	with open('memoryUsage.txt') as f2:
		data2 = f2.read()
	
	# In memoryUsage.txt, the first column refers to the Memory Used (in MB) 
	# and the second column refers to the time
	data2 = data2.split('\n')

	x2 = []
	y2 = []

	for row in range(len(data2)-1):
		x2.append(data2[row].split(' ')[1])
		y2.append(data2[row].split(' ')[0])

	# Plot Graphs
	plt.figure(1)
	# plt.subplot(211)
	plt.ylabel('CPU Percent Usage')
	plt.plot(x1,y1)

	# plt.subplot(212)
	# plt.ylabel('RAM Usage (in MB)')
	# plt.plot(x2,y2)
	plt.show()

if __name__ == "__main__":
	draw_charts()
	