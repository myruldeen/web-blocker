import time
from datetime import datetime as dt

hosts_temp = "hosts"
# hosts_path = "/etc/hosts" # For Linux or Mac
hosts_path = r"C:\Windows\System32\drivers\etc\hosts" # For Windows
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "www.youtube.com", "www.twitter.com"] # List of website to block

def main():
    while True:
        # Check working hours example: 9:00 pm to 5:00 pm 
        if dt(dt.now().year, dt.now().month, dt.now().day,9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,18):
            print("Wroking hours...")
            # Open file and set permission to read/write
            with open(hosts_path, 'r+') as file:
                # Read file content
                content = file.read()
                for website in website_list:
                    if website in content:
                        pass
                    else:
                        # Write/append to file
                        file.write(redirect+" "+ website+"\n")
        else:
            with open(hosts_path, 'r+') as file:
                # Read file line by line
                content = file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in website_list):
                        file.write(line)
                file.truncate()
            print("Break hours...")
        time.sleep(5)      


if __name__ == "__main__":
    main()

