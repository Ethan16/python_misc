#! /bin/sh

if [ -f "total_time.csv" ] ; then
	rm "total_time.csv"
fi
#FLUSHDB=`redis-cli -h 127.0.0.1 -p 6379 flushdb`
#$FLUSHDB
#USED_MEMORY=`redis-cli -h 127.0.0.1 -p 6379 info  memory  | grep "used_memory\>"`
#start_used_memory=`echo $USED_MEMORY |awk -F ":" '{print $2}'` 
count=30
echo $count
while [ "$count" -gt 0 ]
#while(( $count>=1 ))
do
	count=$(( $count - 1))
	echo `redis-cli flushdb`
	start_used_memory=`redis-cli -h 127.0.0.1 -p 6379 info  memory  | grep "used_memory\>" |awk -F ":" '{print $2}'`
#echo $start_used_memory
	python ./redis_single_used_memory.py
	end_used_memory=`redis-cli -h 127.0.0.1 -p 6379 info  memory  | grep "used_memory\>" |awk -F ":" '{print $2}'`

#end_used_memory=`echo $USED_MEMORY |awk -F ":" '{print $2}'` 
#echo $((end_used_memory))
#echo $start_used_memory

#echo $end_used_memory
	echo `expr $((end_used_memory)) - $((start_used_memory)) `
done
