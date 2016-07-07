from urllib.request import urlopen
from bs4 import BeautifulSoup
import subprocess

page_code = urlopen("http://aktu.ac.in/results_even_15_16.html").read()
soup = BeautifulSoup(page_code, 'html.parser')
for string in soup.strings:
    if "B.tech" in string or "B.Tech" in string or "b.tech" in string:
        subprocess.Popen(['notify-send' , "I guess results are out :P "])
