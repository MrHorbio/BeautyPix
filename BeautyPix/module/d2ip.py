import socket
import re

def d2i(filename):
    with open(filename, "r") as f:
        domains = f.read().split()
        print("Read file")
    with open("ip.txt", "a") as f:
        for domain in domains:
         try:
            #cleaned_url = re.sub(r'https?://|/$', '', domain)  # Clean the URL
            ip_address = socket.gethostbyname(domain)
            
            data = f"{domain} : {ip_address}" # Get IP address
            f.write(data + "\n")  # Write IP address to file
         except socket.gaierror:
                print(f"Error resolving domain: {domain}")
            
    print("Operation Successfull & store in [ip.txt] file")



