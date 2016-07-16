from urllib.request import urlopen
from bs4 import BeautifulSoup
import subprocess
import time

subprocess.Popen(['notify-send' , "I'll inform you the moment results are out :P"])
while 1:
    subprocess.Popen(['notify-send' , "I am working"])
    page_code = urlopen("http://aktu.ac.in/results_even_15_16.html").read()
    soup = BeautifulSoup(page_code,'html.parser')
    print(soup.strings)
    for string in soup.strings:
        if "B.tech Second Year" in string or "B.Tech Second Year" in string or "b.tech second year" in string:
            subprocess.Popen(['notify-send' , "I guess results are out :P "])
    time.sleep(600)