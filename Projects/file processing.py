with open('devices.txt','r') as f:
    content= f.read().splitlines()
    devices=list()
    for line in content[1:]:
        devices.append(line.split(':'))

    print(devices)
