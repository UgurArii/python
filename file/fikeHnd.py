Filehnd1 = open("/root/Desktop/pythonTest/country.txt", "r")
print("Name of the file:",Filehnd1.name)

Filehnd1.close()
print("Closed or not",Filehnd1.closed)
print("Opening mode:",Filehnd1.mode)

Filehnd2 = open("/root/Desktop/pythonTest/country.txt", "w+")
Filehnd2.write("Python Processing Files\nMAy 2018''\n")
Filehnd2.close()







