from subprocess import *
from time import *
from pickle import *

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
	#sleep(.5)
	
	if ("200" in output):
		return True
	else:
		return False
		
def generate_initialiams():
	initialisms = []
	
	for a in range(65,91):
		for b in range(65,91):
			for c in range(65,91):
				initialism = chr(a) + chr(b) + chr(c)
				initialisms.append(initialism)
				
	return initialisms
	
def check_initialisms():
	url_stub = "https://en.wikipedia.org/wiki/" 
	trues = 0
	falses = []
	
	initialisms = generate_initialiams()
	for initialism in initialisms:
		url = url_stub + initialism
		if url_exists(url):
			trues = trues + 1
		else:
			falses.append(initialism)
		
	return trues, falses
			
def serialize_list(items, filename):
	file = open(filename,'w')
	dump(items, file)
			
			
		
trues, falses = check_initialisms()
print "Are initialisms:",trues, "out of", trues+len(falses)
serialize_list(falses, "output.txt")
	