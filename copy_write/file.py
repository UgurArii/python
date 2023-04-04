import shutil
import os
shutil.copy('/root/Desktop/pythonTest/output.txt','/root/Desktop/pythonTest/ohno.txt')
os.renames('/root/Desktop/pythonTest/ohno.txt', '/root/Desktop/pythonTest/ohnowell.txt')

fout = open('/root/Desktop/pythonTest/ohno.txt','wt')
fout.write('''Cheerful and happy was his mood,
He to the poor was kind and good,
And he oft' times did find them food,
Also supplies of coal and wood,
He never spake a word was rude,
And cheer'd those did o'er sorrows brood,
He passed away not understood,
Because no poet in his lays
Had penned a sonnet in his praise,
'Tis sad, but such is world's ways.
''')

fout.close()