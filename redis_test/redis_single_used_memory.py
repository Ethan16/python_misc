import redis
from multiprocessing import Process
import psutil
import time,threading
import matplotlib.pyplot as plt
import csv

write_process=[]
DICT={}
CPU_PERCENT_LIST=[]
MEMORY_PERCENT_LIST=[]


def draw_picture(colunm):
	plt.plot(range(COUNT),colunm,label="memory_percent",linewidth=3,color='r')
	#plt.plot(range(total_users),MEMORY_PERCENT_LIST,label="memory_percent",linewidth=1,color='b')
	plt.ylabel("redis-server memory percent")
	plt.title("users insert hash data into redis")
	plt.legend()
	plt.show()


def read_csv():
	with open("redis_data.csv","rb") as file:
		reader=csv.reader(file)
		memory=[float(row[0]) for row in reader]
		print len(memory)
	draw_picture(memory)

def cal_cpu_memory_percent(name,proce_id):
	process=psutil.Process(proce_id)
	memory=process.memory_percent()
	cpu=process.cpu_percent()
	#print "%0.7f,%0.7f" %(memory,cpu)
	with open("redis_data.csv","ab+") as file:
		writer=csv.writer(file)
		writer.writerow([memory])
def save_total_time(total_time):
	with open("total_time.csv","ab+") as file:
		writer=csv.writer(file)
		writer.writerow([total_time])
	
	#global CPU_PERCENT_LIST
	#global MEMORY_PERCENT_LIST
	#print "%s cpu percent is %.2f %%" % (name,
	#CPU_PERCENT_LIST.append(process.cpu_percent())
	#print MEMORY_PERCENT_LIST
	#MEMORY_PERCENT_LIST.append(process.memory_percent())
	#print "%s memory percent is %.2f %%" % (name,

def produce_data(length_of_key_value):
	for i in range(length_of_key_value):
		DICT[str(i)]='a'


def writing_data(virtualID):
	#global redis_server_process_id
	#start_time=time.time()
	r=redis.StrictRedis(host='127.0.0.1',port=6379)
	#r.flushdb()
	pipe=r.pipeline()
	#r.hmset(virtualID,DICT)
	for i in range(COUNT):
		pipe.hmset(str(virtualID)+str(i),DICT)
		#r.hset(virtualID,i,'a')
		#cal_cpu_memory_percent("child process %d" %virtualID,redis_server_process_id)
	pipe.execute()
	#end_time=time.time()
	#print "time is %f" %(end_time-start_time)
	#pipe.hset(virtualID,)

def write_redis(process_count):
	for i in range(process_count):
		p=Process(target=writing_data,args=(i,))
		#p=threading.Thread(target=writing_data,args=(i,))
		p.start()
		#start_time=time.time()
		write_process.append(p)
	for write in write_process:
		write.join()


total_users=10#input("please input total users count:")
redis_server_process_id=2454
COUNT=30#input("please input the numer:")
if __name__ == '__main__':
	produce_data(100)
	start_time=time.time()
	#cal_cpu_memory_percent("start_redis_server",redis_server_process_id)
	write_redis(total_users)
	end_time=time.time()
	save_total_time(end_time-start_time)
	print "total time is %f" %(end_time-start_time)
	#read_csv()
	#print len(CPU_PERCENT_LIST)
	#print len(MEMORY_PERCENT_LIST)
	#draw_picture()

