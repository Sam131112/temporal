import kcorenew
import networkx as nx
gn = "caida_20.txt"
g = nx.read_weighted_edgelist(gn,nodetype=int,create_using=nx.DiGraph())
a = kcorenew.ksize(g)
for x in a:
	print x,len(a[x])
