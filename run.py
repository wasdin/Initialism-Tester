from subprocess import *

url_stub = "https://en.wikipedia.org/wiki/" 
url = url_stub + "XXQ"


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

print output