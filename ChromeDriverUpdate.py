# python 3.7

import subprocess

def chromeDriverUpdate():

    command = 'dir /B /O-N "C:\Program Files (x86)\Google\Chrome\Application" | findstr "^[0-9].*\>'
    chromeVersionBytes = subprocess.check_output(command, shell=True)  # b'86.0.4240.75\r\n' Type:bytes
    chromeVersion = chromeVersionBytes.decode("UTF-8").strip()         # 86.0.4240.75
    majorVersion = chromeVersion.split('.')[0]                         # 86
    
    command = 'pip install chromedriver-binary==' + str(majorVersion) + '.*'
    subprocess.check_output(command, shell=True)