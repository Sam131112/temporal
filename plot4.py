import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['xtick.labelsize']=15
plt.rcParams['ytick.labelsize']=15
with open("node_overlap.txt") as f:
    data = f.read()

data = data.split('\n')
x = [row.split('\t')[0] for row in data[0:len(data)-1]]
y = [row.split('\t')[1] for row in data[0:len(data)-1]]

fig = plt.figure()

ax1 = fig.add_subplot(111)
ax1.set_ylim([0,1.2])
ax1.set_title("As Node overlap",fontsize=20)    
ax1.set_xlabel('time',fontsize=20)
ax1.set_ylabel('JC',fontsize=20)

#ax1.plot(x,y, c='b', label='nodes',linewidth=3.0)
ax1.plot(x,y,c='b',linewidth=2.0)
#leg = ax1.legend()
fig.savefig("n_overlap.png")
#plt.show()
