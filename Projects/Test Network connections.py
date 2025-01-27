import subprocess 
# command = 'ping -n 1 8.8.8.3'
# # command = 'ping c 1 8.8.8.8.9' this will give error 

# output = subprocess.check_output(command.split()) 
# print(output.decode())


with open('hosts.txt') as f:
    ip_addresses = f.read().splitlines()  
for ip in ip_addresses:
    try:
        command = f'ping -n 1 {ip}'  
        output = subprocess.check_output(command.split(), stderr=subprocess.STDOUT)
        
        # Decode and print the output
        print(f"Ping for {ip}:\n{output.decode()}\n")
    except Exception as e:
        print(f"Host {ip} is down:{e}")
    print('*'*50)