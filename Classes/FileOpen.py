try:
    thefile = open('/root/Desktop/pythonTest/people.csv')

    print(thefile.name)
    print('\n\n', thefile.readline())
    thefile.closed()
except FileNotFoundError:
    print("Sorry, I don't see a file named people.csv here")
except Exception:
    print("Sorry, something else went wrong")
    
f = open('/root/Desktop/pythonTest/country.txt')
filecontents = f.read()
print(filecontents)
f.close()

with open('/root/Desktop/pythonTest/country.txt') as ff:
    filecontentss = ff.read()
    print(filecontentss)
# The unindented line below is outside the with... block;
print('File is closed: ',ff.closed)

with open('/root/Desktop/pythonTest/s.png','rb') as a:
    filecontenta = a.read()
    print(filecontenta)
    
    
with open('/root/Desktop/pythonTest/country.txt','r',encoding='utf-8') as b:
    filecontentb = b.read()
    print(filecontentb)  

with open('/root/Desktop/pythonTest/ohno.txt') as f:
    for one_line in enumerate(f.readlines()):
        if one_line[0] %2 == 0:
            print(one_line[1], end='')
        else:
            print('   ' + one_line[1])

#tell()
with open('/root/Desktop/pythonTest/ohno.txt',encoding='utf-8') as c:
    print(c.tell())
    one_linee = c.readline()
    # Keep reading one line at a time until there are no more.
    while one_linee:
        print(one_linee[:1], c.tell())
        one_linee = c.readline()



















    