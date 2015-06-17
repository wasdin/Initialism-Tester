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
		
def generate_initialiams(2, initialisms):
	
	for a in range(65,91):
		for b in range(65,91):
			for c in range(65,91):
				initialism = chr(a) + chr(b) + chr(c)
				initialisms.append(initialism)
				
	return initialisms
		
print generate_initialiams()
	