f=open("arbaz.txt")
#print(f.tell())
f.seek(12)
print(f.readline())
#print(f.tell())
print(f.readline())
#print(f.tell())
f.close()