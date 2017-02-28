import os
no = 0
f = open("networks.txt")
for v in f:
        n = v.strip("\r\n")
        cmd = "mv "+n+" caida_"+str(no)+".txt"
	os.system(cmd)
        #print cmd
        no = no+1
f.close()
