import requests

word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

response = requests.get(word_site)
WORDS = response.content.splitlines()

def custom_generator(n):
    for i in range(1,n):
        mac_address= "02:00:00:%02x:%02x:%02x" % (random.randint(0, 255), random.randint(0, 255),random.randint(0, 255))
        sap_id= '.'.join('%s'%random.randint(0, 255) for i in range(4))
        hostname= "%.com"% (WORDS[random.randint(0, 255)],)
        loopback= '.'.join('%s'%random.randint(0, 255) for i in range(4))
        yield {"mac_address": mac_address, "sap_id": sap_id, "hostname": hostname, "loopback": loopback}


gen=custom_generator(2)
print(next(gen))