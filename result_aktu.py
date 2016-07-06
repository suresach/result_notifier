from urllib.request import urlopen
from bs4 import BeautifulSoup

page_code = urlopen("http://aktu.ac.in/results_even_15_16.html").read()
for lines in page_code:
	if "MCA" in lines:
		print("found")