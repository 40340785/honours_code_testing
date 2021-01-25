import requests
import time
import datetime
import dateutil.relativedelta
import csv
import os

def write_to_csv(post_list, start_final, end_final, difference):
    if os.path.isdir('/app'):
        os.chdir('/app')
    else:
        os.chdir('files/native')

    file_time = time.time()
    file_name = "Post_request_" + str(datetime.datetime.fromtimestamp(file_time).strftime('%d-%m-%Y-%H:%M:%S-%f'))
    with open(file_name, 'w', newline='') as csvfile:
        cwriter = csv.writer(csvfile, delimiter='\n')
        cwriter.writerow(post_list)
        cwriter.writerow([start_final])
        cwriter.writerow([end_final])
        cwriter.writerow([difference])

def format_data(post_list, start_time, end_time):
    start_final = "Start: "+str(datetime.datetime.utcfromtimestamp(start_time).strftime('%H:%M:%S %d-%m-%Y' ))
    end_final = "End:   "+str(datetime.datetime.utcfromtimestamp(end_time).strftime('%H:%M:%S %d-%m-%Y' ))
    print(start_final)
    print(end_final)
    start_human = datetime.datetime.fromtimestamp(start_time)
    end_human = datetime.datetime.fromtimestamp(end_time)
    difference = dateutil.relativedelta.relativedelta(end_human, start_human)
    print(difference)
    write_to_csv(post_list, start_final, end_final, difference)

def main():
    print("Running")
    url = 'http://192.168.41.172:8080'
    #url = 'http://127.0.0.1:8080'
    run_counter = 1000
    #run_counter = input("How many runs do you want to perfom? ")
    x = 1
    post_list = []
    start_time = time.time()
    #print("Sending "+ str(num_of_msg) + " messages, please hold.")
    while x <= int(run_counter):
        msg = requests.post(url, data = "MSG:" + str(x))
        post_list.append("Post:"+str(x)+":"+str(time.time()))
        x = x+1
    end_time = time.time()
    format_data(post_list, start_time, end_time)
main()

