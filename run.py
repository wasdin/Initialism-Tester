from subprocess import Popen

url_stub = "https://en.wikipedia.org/wiki/" 
url = url_stub + "AAA"


p = Popen([
   "curl", 
   "-o /dev/null",
   "--silent",
   "--head",
   "--write-out",
   "'%{http_code}\n'",
   url
])
