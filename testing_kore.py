import networkx as nx
import kcore_decomposition as kde
import kcorenew as kc
from collections import defaultdict

pr = defaultdict(list)
g = nx.read_edgelist("as_1.txt",nodetype=int)
t1 = kc.ksize(g)
t2 = kde.getCoreNumbers(g)

for tz in t2:
	pr[t2[tz]].append(tz)

for z in pr:
	print z,len(pr[z])
	

