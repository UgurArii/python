import subprocess
ret = subprocess.getoutput('date -u | wc')
print(ret)