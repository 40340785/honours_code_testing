import os
import csv
import time
import dateutil.relativedelta
import datetime
import os

def write_to_csv(ping_list, start_time, end_time, difference):
    os.chdir('/app')
    file_time = time.time()
    file_name = "Ping_test_" + str(datetime.datetime.fromtimestamp(file_time).strftime('%H:%M:%S-%d-%m-%Y'))
    with open(file_name, 'w', newline='') as csvfile:
        cwriter = csv.writer(csvfile, delimiter='\n')
        cwriter.writerow(ping_list)
        cwriter.writerow([start_time])
        cwriter.writerow([end_time])
        cwriter.writerow([difference])


def format_data(ping_list, start_time, end_time):
    start_final = "Start: "+str(datetime.datetime.utcfromtimestamp(start_time).strftime('%H:%M:%S:%f %d-%m-%Y' ))
    end_final = "End:   "+str(datetime.datetime.utcfromtimestamp(end_time).strftime('%H:%M:%S:%f %d-%m-%Y' ))
    print(start_final)
    print(end_final)
    start_human = datetime.datetime.fromtimestamp(start_time)
    end_human = datetime.datetime.fromtimestamp(end_time)
    difference = dateutil.relativedelta.relativedelta(end_human, start_human)
    print(difference)
    write_to_csv(ping_list, start_final, end_final, difference)


def main():
    print("Starting") 
    run_counter = 5
    #run_counter = input("How many runs do you want to perfom? ")
    dest_ip = '1.1.1.1'
    x = 1 
    ping_list = []
    start_time = time.time()
    while x <= int(run_counter):
        os.system("ping -c 1 "+dest_ip)
        ping_list.append("Ping:"+str(x)+":"+str(time.time()))
        x+=1
    end_time = time.time()
    #print("Length " + str(len(ping_list)))
    print("Finished")
    format_data(ping_list, start_time, end_time)
main()
