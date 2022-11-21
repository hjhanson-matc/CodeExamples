#Hunter Hanson

#Inital Entries
fqdndb = {
    'server1.testlab.com' : '192.168.1.10',
    'server2.testlab.com' : '192.168.1.11',
    'server3.testlab.com' : '192.168.1.12',
    'server4.testlab.com' : '192.168.1.13',
    'server5.testlab.com' : '192.168.1.14',
    'server6.testlab.com' : '192.168.1.15'
}
#List of all FQDN's
print (f"Here are all the FQDN's in the dictionary:\n{fqdndb.keys()}")
print ()
#List of all IP addresses
print (f"Here are all the IP addresses in the dictionary:\n{fqdndb.values()}")
print ()
#List of all full records
print (f"Here are all the key/value pairs in the dictionary:\n{fqdndb.items()}")
print ()
#Additional entries
fqdndb["server7.testlab.com"] = "192.168.1.16"
fqdndb["server8.testlab.com"] = "192.168.1.17"
#Test entries
print (f"The ip for server2 is {fqdndb.get('server2.testlab.com', 'does not exist')}")
print (f"The ip for server10 is {fqdndb.get('server10.testlab.com', 'does not exist')}")
