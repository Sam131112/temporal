# for Infocom and HT09  modified from version 1.4 and will be applied on sleep time removed datasets
# Successfully removed sleeping time from infocom / HT by addind the while loop

import networkx as nx
import pickle
import numpy as np
import kcore_decomposition as kde
import kcorenew as kc
import jaccards as j

f1 = open("density.txt","w")
fu = open("unique_node.txt","w")
topc = []
edges = []
top5c = []
top5b = []
unodes = []
count = 1
counts = 3600
couns1 = 0
couns = 0
var = 20
f = pickle.load(open('modi_ht.p','rb'))
#print f[:25]
for t in f:
  couns=couns+1
  #print t[0]
  if t[0] < count*counts:
	edges.append((t[1],t[2]))
  
  else:
	couns1 = couns1+1
	while t[0]>=count*counts:
		count=count+1
	g = nx.Graph()
	g.add_edges_from(edges)
	if g.number_of_nodes()<=0:
		continue
	c1 = nx.closeness_centrality(g)
        c2 = c1.items()
        c3 = sorted(c2,key = lambda x:x[1],reverse=True)
        c4 = c3[:5]
        cloa = []
        for x in c4:
                cloa.append(x[0])
        c1 = nx.betweenness_centrality(g)
        c2 = c1.items()
        c3 = sorted(c2,key = lambda x:x[1],reverse=True)
        c4 = c3[:5]
        bwoa = []
        for x in c4:
                bwoa.append(x[0])
	#print t[0],nx.number_of_nodes(g),nx.number_of_edges(g)
	top5c.append(cloa)
	top5b.append(bwoa)
	sh = kc.ksize(g)
	v = sh.items()
	print v,g.number_of_nodes(),g.number_of_edges()
	topc.append(v[-1][1])
	g1 = g.subgraph(v[-1][1])
  	edges = []
	edges.append((t[1],t[2]))
	f1.write(str(count)+'\t'+str(nx.density(g1))+'\n')
	unodes.append(g.number_of_nodes())
	fu.write(str(count)+'\t'+str(g.number_of_nodes())+'\n')
 
#print len(times),len(f)
print len(top5c),len(top5b),len(topc),len(unodes)
j.jaccards(top5c,'close')
j.jaccards(top5b,'bets')
j.jaccards(topc,'kcore')
pickle.dump(top5c,open('topclose5.p','wb'))
pickle.dump(top5b,open('topbet5.p','wb'))
pickle.dump(topc,open('topcore.p','wb'))
f1.close()
fu.close()
