'''tup = ("Python", "Linux", "Network", "Cyber", "Security")
# Print the 3rd element
# Print the last element'''
# tup = ("Python", "Linux", "Network", "Cyber", "Security")
# print(tup[2])
# print(tup[-1]) #print(tup[len(tup)-1])

'''The second last item in this tuple:
tup = ("Firewall", "Encryption", "Hashing", "Antivirus", "Threats")'''
# tup = ("Firewall", "Encryption", "Hashing", "Antivirus", "Threats")
# print(tup[-2])

'''Write a program that checks whether "Malware" is present in this tuple:
tools = ("Nmap", "Wireshark", "Burp", "Nikto", "Malware", "JohnTheRipper")'''
# tools = ("Nmap", "Wireshark", "Burp", "Nikto", "Malware", "JohnTheRipper")
# if "Malware" in tools:
#     print("Malware is present in the tuple")
# else:
#     print("Malware is not present in the tuple")

'''Print the tuple elements from index 2 to 5:
services = ("HTTP", "HTTPS", "FTP", "SSH", "SMTP", "DNS", "DHCP")'''
# services = ("HTTP", "HTTPS", "FTP", "SSH", "SMTP", "DNS", "DHCP")
# print(services[2:6])

'''Using slice and step, print every second service from this tuple:
protocols = ("SSL", "TLS", "IPSec", "IKE", "SSH", "HTTPS", "DNSSEC")'''
# protocols = ("SSL", "TLS", "IPSec", "IKE", "SSH", "HTTPS", "DNSSEC")
# print(protocols[::2])

'''Get everything till a given index:
Print all items from the beginning to the 4th index.'''
# protocols = ("SSL", "TLS", "IPSec", "IKE", "SSH", "HTTPS", "DNSSEC")
# print(protocols[:4])

'''Threat Log Analysis:
You have this tuple of security alerts (ordered by time):
alerts = ("Phishing", "DDoS", "Malware", "SQLi", "XSS", "Ransomware", "Rootkit")
Print only the last 3 alerts using slicing.
Print the alerts in reverse order using slicing.'''
# alerts = ("Phishing", "DDoS", "Malware", "SQLi", "XSS", "Ransomware", "Rootkit")
# print(alerts[-3:])
# print(alerts[::-1])

'''Tuple Filter via Condition (manual way):
From the tuple below, manually create a new tuple (or list) of items that are longer than 4 characters:
cyber_terms = ("VPN", "Key", "Payload", "Trojan", "Bot", "Rootkit", "Spy")'''
# cyber_terms = ("VPN", "Key", "Payload", "Trojan", "Bot", "Rootkit", "Spy")
# numtup = []
# for i in cyber_terms:
#   if len(i) > 4:
#     numtup.append(i)
# print(numtup)

'''data = ("OSINT", "Red", "Blue", "Purple", "PenTest", "Audit")
# Print from "Red" to "PenTest" using a single slice'''
# data = ("OSINT", "Red", "Blue", "Purple", "PenTest", "Audit")
# print(data[1:5])

'''tup = ("Kali", "Parrot", "BlackArch", "BackBox", "Tails")
# Write code to check if there are more than 4 distros in the list.'''
# tup = ("Kali", "Parrot", "BlackArch", "BackBox", "Tails")
# if len(tup) > 4:
#     print("There are more than 4 distros in the list")
# else:
#     print("There are 4 or fewer distros in the list")

'''# Given:
tools = ("Nmap", "Nikto", "Burp", "Wireshark")
# Task: Add "Metasploit", remove "Nikto", and replace "Burp" with "ZAP"
# Convert to list, modify, and convert back to tuple'''
# tools = ("Nmap", "Nikto", "Burp", "Wireshark")
# temp = list(tools)
# temp.append("Metasploit")
# temp.remove("Nikto")
# index = temp.index("Burp")      
# temp[index] = "ZAP"  
# updated_tools = tuple(temp)
# print(updated_tools)

'''# Given:
scanning = ("Nmap", "Masscan")
web_tools = ("ZAP", "Burp Suite")
# Task: Create one tuple with all tools and print it'''
# scanning = ("Nmap", "Masscan")
# web_tools = ("ZAP", "Burp Suite")
# tup = scanning + web_tools
# print(tup)

'''# Tuple: ("Trojan", "Ransomware", "Keylogger", "Rootkit")
# Remove "Keylogger" and print final tuple'''
# Tuple = ("Trojan", "Ransomware", "Keylogger", "Rootkit")
# temp = list(Tuple)
# temp.remove("Keylogger")
# updated_tup = tuple(temp)
# print(updated_tup)

'''logs = ("403", "200", "404", "403", "500", "403")
# Count how many times "403" appears'''
# logs = ("403", "200", "404", "403", "500", "403")
# print(logs.count("403"))

'''attacks = ("XSS", "SQLi", "DoS", "Brute Force", "SQLi")
# Find first index of "SQLi"'''
# attacks = ("XSS", "SQLi", "DoS", "Brute Force", "SQLi")
# print(attacks.index("SQLi"))

'''Write a program that checks whether "Phishing" is in the tuple:
threats = ("DDoS", "Malware", "Ransomware", "Rootkit", "Spyware")
# # If yes, print the index. Otherwise, print "Not Found"'''
# threats = ("DDoS", "Malware", "Ransomware", "Rootkit", "Spyware")
# if "Phishing" in threats:
#     print(threats.index("Phishing"))
# else:
#     print("Not Found")

'''# Devices connected to a secure network:
devices = ("laptop", "mobile", "tablet", "router")
# Add a new device "firewall", remove "tablet", replace "mobile" with "desktop"'''
# devices = ("laptop", "mobile", "tablet", "router")
# temp = list(devices)
# temp.append("firewall")
# temp.remove("tablet")
# index = temp.index("mobile")
# temp[index] = "desktop"
# updated_devices = tuple(temp)
# print(updated_devices)

'''events = ("login", "fail", "fail", "login", "fail", "logout")
# Count how many times "fail" occurred (indicates brute force)'''
# events = ("login", "fail", "fail", "login", "fail", "logout")
# print(events.count("fail"))

'''hacker_tools = ("nc", "nmap", "hydra", "john", "nmap")
# Count how many times "nmap" appears
# If more than once, alert: "Multiple scans detected"'''
hacker_tools = ("nc", "nmap", "hydra", "john", "nmap")
print(hacker_tools.count("nmap"))
# if hacker_tools.count("nmap") > 1:
#     print("Multiple scans detected")
# else:
#     print("No multiple scans detected")

