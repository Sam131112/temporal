# for Autonomous systems  networks 
import networkx as nx
import pickle
import numpy as np
import kcore_decomposition as kde
import kcorenew as kc
import jaccards as j
import os

f1 = open("density.txt","w")
fu = open("unique_nodes.txt","w")
topc = []
top5c = []
top5b = []
unodes = []

for v in range(120):
	gn = "n_caida/caida_"+str(v)+".txt"
	gn1 = 'caida_'+str(v)
	g = nx.read_weighted_edgelist(gn,nodetype=int)
	print g.number_of_nodes()
	nx.write_edgelist(g,'caida_'+str(v)+'.txt',data=False)
	c1 = pickle.load(open("caida_"+str(v)+"close.p","rb"))
        c2 = c1.items()
        c3 = sorted(c2,key = lambda x:x[1],reverse=True)
        c4 = c3[:5]
        cloa = []
        for x in c4:
                cloa.append(x[0])
        c1 = pickle.load(open("caida_"+str(v)+"betw.p","rb"))
        c2 = c1.items()
        c3 = sorted(c2,key = lambda x:x[1],reverse=True)
        c4 = c3[:5]
        bwoa = []
        for x in c4:
                bwoa.append(x[0])
	top5c.append(cloa)
	top5b.append(bwoa)
	os.system('./kcores -i:'+gn+' -o:'+gn1)
	gcore = nx.read_edgelist(gn1+'.txt',nodetype=int)
	print gcore.number_of_nodes(),gcore.number_of_edges()
	topc.append(gcore.nodes())
	f1.write(str(v)+'\t'+str(nx.density(gcore))+'\n')
	unodes.append(g.number_of_nodes())
	os.system('rm '+gn1+".txt")

x = 1
for i in unodes:
	fu.write(str(x)+'\t'+str(i)+'\n')
	x=x+1

j.jaccards(top5c,'close')
j.jaccards(top5b,'bets')
j.jaccards(topc,'kcore')
pickle.dump(top5c,open('topclose5.p','wb'))
pickle.dump(top5b,open('topbet5.p','wb'))
pickle.dump(topc,open('topcore.p','wb'))
f1.close()
fu.close()
