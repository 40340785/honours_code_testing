import urllib.request
import datetime
import time
import dateutil.relativedelta
import csv
import os

def write_to_csv(request_list, start_time, end_time, difference):
    if os.path.isdir('/app'):
        os.chdir('/app')
    else:
        os.chdir('files/native')

    file_time = time.time()
    file_name = "Get_request_" + str(datetime.datetime.fromtimestamp(file_time).strftime('%d-%m-%Y-%H:%M:%S-%f'))
    with open(file_name, 'w', newline='') as csvfile:
        cwriter = csv.writer(csvfile, delimiter='\n')
        cwriter.writerow(request_list)
        cwriter.writerow([start_time])
        cwriter.writerow([end_time])
        cwriter.writerow([difference])


def format_data(request_list, start_time, end_time):
    start_final = "Start: "+str(datetime.datetime.utcfromtimestamp(start_time).strftime('%H:%M:%S:%f %d-%m-%Y' ))
    end_final = "End:   "+str(datetime.datetime.utcfromtimestamp(end_time).strftime('%H:%M:%S:%f %d-%m-%Y' ))
    print(start_final)
    print(end_final)
    start_human = datetime.datetime.fromtimestamp(start_time)
    end_human = datetime.datetime.fromtimestamp(end_time)
    difference = dateutil.relativedelta.relativedelta(end_human, start_human)
    print(difference)
    write_to_csv(request_list, start_final, end_final, difference)


def main():
    print("Running")
    run_counter = 100
    #run_counter = input("How many runs do you want to perfom? ")
    url_name = "http://192.168.41.172:8080"
    x = 1
    request_list = []
    start_time = time.time()
    while x <= int(run_counter):
        urllib.request.urlopen(str(url_name)).read()
        request_list.append("MSG:" + str(x) + ":" + str(time.time()))
        x+=1
    end_time = time.time()
    format_data(request_list, start_time, end_time) 
main()
