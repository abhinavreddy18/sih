import io
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt) 
f1=open('D:\Abhinav\simulate.txt','r')
for line in f1:
    print(re.search("^/[",str(line)))
print(x)
