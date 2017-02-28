import networkx as nx
import pickle

edges = []
top5 = []
f = open("ht09_contact_list.dat")
count = 1
counts = 600
couns1 = 0
couns = 0
for v in f:
  couns=couns+1
  v = v.strip("\n")
  v = v.split("\t")
  t = []
  for x in v:
    try:
     t.append(int(x))
    except:
     pass
  if t[0] < count*counts:
	edges.append((t[1],t[2]))	
  else:
	couns1 = couns1+1
	count=count+1
	g = nx.Graph()
	g.add_edges_from(edges)
	print t[0],nx.number_of_nodes(g),nx.number_of_edges(g)
  	edges = []
	edges.append((t[1],t[2]))

print counts,count,couns1,couns
