import urllib.request
import datetime
import time
import dateutil.relativedelta
import csv
import os

def write_to_csv(start_final, end_final, difference, download_name):
    if os.path.isdir('/app'):
        os.chdir('/app')
    else:
        pass 
    file_time = time.time()
    file_name = "File_download_" + str(datetime.datetime.fromtimestamp(file_time).strftime('%d-%m-%Y-%H:%M:%S-%f'))
    with open(file_name, 'w', newline='') as csvfile:
        cwriter = csv.writer(csvfile, delimiter='\n')
        cwriter.writerow([download_name])
        cwriter.writerow([start_final])
        cwriter.writerow([end_final])
        cwriter.writerow([difference])

def format_data(start_time, end_time, download_name):
    start_final = "Start: "+str(datetime.datetime.utcfromtimestamp(start_time).strftime('%H:%M:%S:%f %d-%m-%Y' ))
    end_final = "End:   "+str(datetime.datetime.utcfromtimestamp(end_time).strftime('%H:%M:%S:%f %d-%m-%Y' ))
    print("File: " + str(download_name))
    print(start_final)
    print(end_final)
    print(str(start_time) + "\n" + str(end_time))
    start_human = datetime.datetime.fromtimestamp(start_time)
    end_human = datetime.datetime.fromtimestamp(end_time)
    difference = dateutil.relativedelta.relativedelta(end_human, start_human)
    print(difference)
    write_to_csv(start_final, end_final, difference, download_name)

def main():
    print("Starting")
    file_url = "http://192.168.88.234:8080/arp_scan.zip"
    download_name = "file.zip"
    if os.path.isdir('/app'):
        pass 
    else:
        os.chdir('files/native')
        os.system('pwd')
    start_time = time.time()
    urllib.request.urlretrieve(file_url, download_name)
    end_time = time.time()
    #end_time = datetime.datetime.now()
    print("Finished")
    format_data(start_time, end_time, download_name)
main()
