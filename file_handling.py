#open(file name,mode)
#modes-r-read,w-write,a-append,x-create
#write
x=open("DEMO.txt","w") 
x.write("This is Python File Handling")
x.close()

#append
y=open("DEMO.txt","a")
y.write("\nThis is an appended text")
y.close()

#read
z=open("DEMO.txt","r")
print(z.read())
z.close()

file=open("Mine.txt","w")
file.write("Hello im Python")
file.write("\nHello im Python")
file.close()
