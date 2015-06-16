from subprocess import *

url_stub = "https://en.wikipedia.org/wiki/" 
url = url_stub + "XXQ"

def url_exists(url):
	p = Popen([
	   "curl", 
	   "-o /dev/null",
	   "--silent",
	   "--head",
	   "--write-out",
	   "'%{http_code}\n'",
	   url
	], stdout=PIPE)

	output, error = p.communicate()
	
	if ("200" in output):
		return true
	else:
		return false
		
def generate_initialiams(length):
	initialisms = []
	initialism = ""
	
	while (len(initialism)) < (length):
		for letter in range(65,91):
			initialism += chr(letter)
		
print generate_initialiams(2)
	