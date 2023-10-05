n = 1
keys = open("01_keymaker_ordered.txt", "r")
while s != j:

    s = keys.readline(n)
    
    li = []
    l = len(s)
    for i in range (0,l):
    	li.append(s[i])
    
    
    for i in range(0,l):
    	for j in range(0,l):
    		if li[i]<li[j]:
    			li[i],li[j]=li[j],li[i]
    j=""
    
    for i in range(0,l):
    	j = j+li[i]
    	
    n += 1
print("Key found! Key is: " + j)
