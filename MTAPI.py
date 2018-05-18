from google.transit import gtfs_realtime_pb2
import urllib.request as ur
import time as pyTime


api_key = '4528d540df98d9dd40598e65e1acf4b2'
GTFS_head = 'http://datamine.mta.info/mta_esi.php?key='
ace_tail = '&feed_id=26'
tail_123 = '&feed_id=1'

acefeedurl = GTFS_head + api_key + ace_tail
feed123url = GTFS_head + api_key + tail_123

feed = gtfs_realtime_pb2.FeedMessage()
response = ur.urlopen(acefeedurl)
feed.ParseFromString(response.read())

a_message = feed.entity

response = ur.urlopen(feed123url)
feed.ParseFromString(response.read())

message_1 = feed.entity

def list_first_item():
    print(message_1[0])

def list_A_times():
    print("Upcoming trips from 175th St Station:")
    print("-----------------------")
    up_tc = 0
    down_tc = 0
    for item in a_message:    
        if not item.HasField('trip_update'):
            continue
        tu = item.trip_update
        
        for stu in tu.stop_time_update:
            
            if stu.stop_id == "A07S" or stu.stop_id == "A07N":

                if stu.stop_id == "A07S":
                    #if stu.HasField('arrival'):
                        #print('Arrival: '+ pyTime.ctime(stu.arrival.time))
                    sDiff = stu.departure.time - pyTime.time()
                    if stu.HasField('departure') and sDiff > 0 and sDiff < 1800:
                        m, s = divmod(sDiff, 60)
                        msDiff = "%02d:%02d" % (m, s)
                        print('Downtown departure: '+ pyTime.ctime(stu.departure.time))
                        print(msDiff + " minutes from now.")
                        down_tc += 1
                else:
                    sDiff = stu.departure.time - pyTime.time()
                    if stu.HasField('departure') and sDiff > 0 and sDiff < 1800:
                        m, s = divmod(sDiff, 60)
                        msDiff = "%02d:%02d" % (m, s)
                        print('Uptown departure: '+ pyTime.ctime(stu.departure.time))
                        print(msDiff + " minutes from now.")
                        up_tc += 1

    print("There are %d downtown and %d uptown trains in the next 30 mins." % (down_tc, up_tc))
        
def list_1_times():
    print("\n")
    print("<<<<<----------------181st St Station---------------->>>>>")
    print("")
    up_tc = 0
    down_tc = 0
    for item in message_1:    
        if not item.HasField('trip_update'):
            continue
        tu = item.trip_update
        
        for stu in tu.stop_time_update:
            
            if stu.stop_id == "111S" or stu.stop_id == "111N":
            
                if stu.stop_id == "111S":
                    #if stu.HasField('arrival'):
                        #print('Arrival: '+ pyTime.ctime(stu.arrival.time))
                    sDiff = stu.departure.time - pyTime.time()
                    if stu.HasField('departure') and sDiff > 0 and sDiff < 1800:
                        m, s = divmod(sDiff, 60)
                        msDiff = "%02d:%02d" % (m, s)
                        print('Downtown departure: '+ pyTime.ctime(stu.departure.time))
                        print(msDiff + " minutes from now.")
                        down_tc += 1

                else:
                    sDiff = stu.departure.time - pyTime.time()
                    if stu.HasField('departure') and sDiff > 0 and sDiff < 1800:
                        m, s = divmod(sDiff, 60)
                        msDiff = "%02d:%02d" % (m, s)
                        print('Uptown departure: '+ pyTime.ctime(stu.departure.time))
                        print(msDiff + " minutes from now.")
                        up_tc += 1
    print("There are %d downtown and %d uptown trains in the next 30 mins." % (down_tc, up_tc))

            
#list_first_item()

def monitor_subway():
    while True:
        print("======= MAN CAVE SUBWAY MONITOR for "+pyTime.ctime()+ " ========")
        list_A_times()
        list_1_times()
        for _ in range(60):
            print("=",end='')
            pyTime.sleep(0.25)
        print("\n")

monitor_subway()
#print (entity[0:5])
#print (feed.entity[0])
#if entity.HasField('time'):
    
