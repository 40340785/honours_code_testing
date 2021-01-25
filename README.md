# honours_code_testing
Upload of code so far for testing, use the following instructions below to get started, let me know if there are any issues.

docker build -t auto_test -f Dockerfile .

#Run this command from inside of the “honours_code_testing/test_framework” directory.

For this to work you will need to modify some code, specifically the following variables:
automater.py - url 
simple_file_download_csv_v2.py - file_url
simple_get_request_csv_v2.py - url_name
simple_post_request_csv_v2.py - url
simple_ping_test_csv_v2.py - dest_ip
#The above variables need to be changed to a url that you control, and have a file to download, I suggest the following command:
python3 -m http.server 8080
#Run this from a directory and use the outward facing IP address, also rename the download file to test.

To run the program use the following command:

python3 automater.py
