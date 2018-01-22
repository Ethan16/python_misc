import matplotlib.pyplot as plt
import csv


def draw_picture(file_name,info):
	plt.plot(range(len(info)),info,label=file_name,linewidth=3,color='r')
	#plt.plot(range(total_users),MEMORY_PERCENT_LIST,label="memory_percent",linewidth=1,color='b')
	plt.ylabel(file_name)
	plt.title(file_name)
	plt.legend()
	plt.show()


def read_csv(file):
	with open(file,"rb") as fd:
		reader=csv.reader(fd)
		info=[float(row[0]) for row in reader]
		#print len(memory)
		print type(file)
	draw_picture(file.split('.')[0],info)

if __name__ == '__main__':
	file="total_time.csv"
	read_csv(file)

