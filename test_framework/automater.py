import os
import sys
import glob
import os
import statistics
from datetime import timedelta
from shutil import copyfile
import time
import matplotlib.pyplot as plt
import urllib.request 

def graph_builder(platform, user_choice, new_data_list):
    #This function is responsible for building the graph shown at the end.
    counter = 1
    x = []
    while counter <= len(new_data_list):
        x.append("Run " + str(counter))
        counter += 1
    plt.bar(x, new_data_list)
    plt.show()    

def data_collator(platform, user_choice):
    #This function is responsible for collecting all of the data from outputted files and showing averages.
    if user_choice == "1": 
        user_choice = "/home/user/scripts/python/file_open/docker_code"
        file_names = ["File_open_"]
    elif user_choice == "2":
        ps_list_path = "/home/user/scripts/python/ps_list/docker_code"
        file_names = ["Ps_list_"]
    elif user_choice == "3":
        user_choice = "/home/user/scripts/python/simple_ping_test/docker_code"
        file_names = ["Ping_test_"]
    elif user_choice == "4":
        user_choice = "/home/user/scripts/python/download_file/docker_code"
        file_names = ["File_download_"]
    elif user_choice == "5":
        user_choice = "/home/user/scripts/python/file_write/docker_code"
        file_names = ["File_write_"]
    elif user_choice == "6":
        user_choice = "/home/user/scripts/python/simple_get_request/docker_code"
        file_names = ["Get_request_"]
    elif user_choice == "7":
        user_choice = "/home/user/scripts/python/simple_post_request/docker_code"
        file_names = ["Post_request_"]
    elif user_choice == "8":
        file_names = ["File_open_", "Ps_list_", "Ping_test_", "File_download_", "File_write_", "Get_request_", "Post_request_"]
   
    #os.chdir(user_choice + '/files/')
    os.chdir('files/'+str(platform))
    read_data = []
    file_name_list = []
    #for file in glob.glob('File*'):
    x = 0
    while x <= len(file_names) - 1:
        for file in glob.glob(str(file_names[x])+"*"):
            #print(str(file).rstrip()) 
            file_name_list.append(file)
            with open(file, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    read_data.append(line)
        x+=1

    matching = [s for s in read_data if "relativedelta" in s]
    #This matches onto the string we are looking for.
    data_list = []
    for val in matching:
        test = val.split('+')
        test2 = test[-1]
        data_list.append(test2[0:-2])
    new_data_list = list(map(int, data_list))
    #This takes the list and turns all values of it into integers.
    average_time_micro = str(statistics.mean(new_data_list))
    
    counter = 0 
    while counter <= len(file_name_list) - 1:
        print(str(file_name_list[counter]) + " time to complete: " + str(new_data_list[counter]))
        counter += 1
    print("The average of the runs time are: " + str(statistics.mean(new_data_list)) + " microseconds.")
    #print("AVG time " + str(timedelta(microseconds=float(average_time_micro))) + " seconds.")
    graph_builder(platform, user_choice, new_data_list)

def test_execution(counter, platform_command):
    #Functions purpose is to execute the tests, it is in a seperate function for certain tests to work.
    print("Test: " + str(counter))
    os.system(str(platform_command))


def test_setup(user_choice, run_count, platform):
    #Function sets up the tests, before calling the executing function.
    if platform == "native":
        platform_command = "python3 $(pwd)/files/native/script.py"
    elif platform == "docker":
        platform_command = "docker run -it -v $(pwd)/files/docker:/app/ auto_test:latest"
    elif platform == "gvisor":
        platform_command = "docker run --runtime=runsc -it -v $(pwd)/files/gvisor:/app/ auto_test:latest"

    if user_choice == "1":
        print("File Open Test")
        copyfile('file_open_csv_v2.py', 'files/'+ str(platform) +'/script.py')
        counter = 1
        while counter <= int(run_count):
            test_execution(counter, platform_command)
            counter+=1

    elif user_choice == "2":
        print("Process List Test")
        copyfile('ps_list_csv_v2.py', 'files/'+ str(platform) +'/script.py')
        counter = 1
        while counter <= int(run_count):
            test_execution(counter, platform_command)
            counter+=1

    elif user_choice == "3":
        print("Ping Test")
        copyfile('simple_ping_test_csv_v2.py', 'files/'+ str(platform) +'/script.py')
        counter = 1
        while counter <= int(run_count):
            test_execution(counter, platform_command)
            counter+=1

    elif user_choice == "4":
        print("File Download Test")
        copyfile('simple_file_download_csv_v2.py', 'files/'+ str(platform) +'/script.py')
        counter = 1
        while counter <= int(run_count):
            test_execution(counter, platform_command)
            counter+=1

    elif user_choice == "5":
        print("File Write Test")
        copyfile('file_write_csv_v2.py', 'files/'+ str(platform) +'/script.py')
        counter = 1
        while counter <= int(run_count):
            test_execution(counter, platform_command)
            counter+=1

    elif user_choice == "6":
        print("GET Request Test")
        copyfile('simple_get_request_csv_v2.py', 'files/'+ str(platform) +'/script.py')
        counter = 1
        while counter <= int(run_count):
            test_execution(counter, platform_command)
            counter+=1

    elif user_choice == "7":
        print("POST Request Test")
        copyfile('simple_post_request_csv_v2.py', 'files/'+ str(platform) +'/script.py')
        counter = 1
        while counter <= int(run_count):
            test_execution(counter, platform_command)
            counter+=1

    elif user_choice == "8":
        print("POST Request Test")
        #os.chdir(ps_list_path)
        counter = 1
        while counter <= int(run_count):
            copyfile('file_open_csv_v2.py', 'files/'+ str(platform) +'/script.py')
            test_execution(counter, platform_command)
            copyfile('ps_list_csv_v2.py', 'files/'+ str(platform) +'/script.py')
            test_execution(counter, platform_command)
            copyfile('simple_ping_test_csv_v2.py', 'files/'+ str(platform) +'/script.py')
            test_execution(counter, platform_command)
            copyfile('simple_file_download_csv_v2.py', 'files/'+ str(platform) +'/script.py')
            test_execution(counter, platform_command)
            copyfile('file_write_csv_v2.py', 'files/'+ str(platform) +'/script.py')
            test_execution(counter, platform_command)
            copyfile('simple_get_request_csv_v2.py', 'files/'+ str(platform) +'/script.py')
            test_execution(counter, platform_command)
            copyfile('simple_post_request_csv_v2.py', 'files/'+ str(platform) +'/script.py')
            test_execution(counter, platform_command)
            counter+=1

    elif user_choice == "q" or user_choice == "Q":
        sys.exit()

    else:
        print("Error invalid choice!")
        sys.exit()
def input_tests(platform, user_choice, run_count):
    #Function is for verifying user input is valid, in a seperate function for simplicity and readability of Main.
    try:
        int(user_choice)
        int(run_count)
        int(platform)
        if int(user_choice) >= 1 and int(user_choice) <=8:
            pass
        else:
            print("Invalid choice!")
            sys.exit()

        if int(platform) >= 1 and int(platform) <=3:
            if platform == "1":
                platform = "native"
                return platform
            elif platform == "2":
                platform = "docker"
                return platform
            elif platform == "3":
                platform = "gvisor"
                return platform

        else:
            print("Invalid choice!")
            sys.exit()
    except Exception as e:
        print('Error invlaid choice')
        print(repr(e))
        sys.exit()

def main():
    platform = input("Platform choice: \n1: Native \n2: Docker \n3: Docker with gVisor \n")
    user_choice = input("Choices: \n1: File Open Test \n2: Process List Test \n3: Ping Test \n4: File Download Test \n5: File Write Test \n6: GET Request Test \n7: POST Request Test \n8: Run All Tests \n")
    run_count = input("How many runs of this test are to be performed? ")
    if user_choice == "6" or user_choice == "7" or user_choice == "8":
        try:
            urllib.request.urlopen("http://192.168.41.172:8080").read()
        except:
            print("Error no connection to URL 'http://192.168.41.172:8080' open, check connectivity!")
            sys.exit()
    
    platform = input_tests(platform, user_choice, run_count) 
    test_setup(user_choice, run_count, platform)
    data_collator(platform, user_choice)
main()
