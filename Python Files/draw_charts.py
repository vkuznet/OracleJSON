import matplotlib.pyplot as plt

def draw_charts():
	# CPU Statistics
	with open('../Performance Statistics/cpu_stats.txt') as f1:
		data1 = f1.read()
		
	data1 = data1.split('\n')

	x1 = []
	y1 = []

	for row in range(len(data1)-1):
		x1.append(data1[row].split(' ')[1])
		y1.append(data1[row].split(' ')[0])

	# Memory Statistics
	with open('../Performance Statistics/mem_stats.txt') as f2:
		data2 = f2.read()
		
	data2 = data2.split('\n')

	x2 = []
	y2 = []

	for row in range(len(data2)-1):
		x2.append(data2[row].split(' ')[1])
		y2.append(data2[row].split(' ')[0])

	# Plot Graphs
	plt.figure(1)
	plt.subplot(211)
	plt.ylabel('CPU Percent Usage')
	plt.plot(x1,y1)

	plt.subplot(212)
	plt.ylabel('RAM Usage (in MB)')
	plt.plot(x2,y2)
	plt.show()

if __name__ == "__main__":
	draw_charts()
	