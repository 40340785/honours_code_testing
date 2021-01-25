import os
import time
import datetime
import dateutil.relativedelta
import csv
import os

def write_to_csv(ps_list, start_final, end_final, difference):
    if os.path.isdir('/app'):
        os.chdir('/app')
    else:
        os.chdir('files/native')

    file_time = time.time()
    file_name = "Ps_list_" + str(datetime.datetime.fromtimestamp(file_time).strftime('%d-%m-%Y-%H:%M:%S-%f'))
    with open(file_name, 'w', newline='') as csvfile:
        cwriter = csv.writer(csvfile, delimiter='\n')
        cwriter.writerow(ps_list)
        cwriter.writerow([start_final])
        cwriter.writerow([end_final])
        cwriter.writerow([difference])

def format_data(ps_list, start_time, end_time):
    start_final = "Start: "+str(datetime.datetime.utcfromtimestamp(start_time).strftime('%H:%M:%S:%f %d-%m-%Y' ))
    end_final = "End:   "+str(datetime.datetime.utcfromtimestamp(end_time).strftime('%H:%M:%S:%f %d-%m-%Y' ))
    print(start_final)
    print(end_final)
    start_human = datetime.datetime.fromtimestamp(start_time)
    end_human = datetime.datetime.fromtimestamp(end_time)
    difference = dateutil.relativedelta.relativedelta(end_human, start_human)
    print(difference)
    write_to_csv(ps_list, start_final, end_final, difference)


def main():
    print("Starting")
    run_counter = 10
    #run_counter = input("How many runs do you want to perfom? ")
    x = 1
    ps_list = []
    start_time = time.time()
    while x <= int(run_counter):
        os.system("ps -e > /dev/null")
        ps_list.append("Count:" + str(x) + ":" + str(time.time()))
        x = x + 1

    end_time = time.time()
    print("Finished")
    format_data(ps_list, start_time, end_time)
main()
