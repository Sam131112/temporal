# for Autonomous systems  networks 
import networkx as nx
import pickle
import numpy as np
import kcore_decomposition as kde
import kcorenew as kc
import jaccards as j
import make_seed as ms
import os
import matplotlib.pyplot as plt

topc = []
top5c = []
top5b = []
unodes = []
sp  = open("original_spread_result_wiki.txt","w")
sp1 = open("original_bet_result_wiki.txt","w")

for v in range(34,65,1):
	gn = "wiki/wiki_"+str(v)+".txt"
	g = nx.read_weighted_edgelist(gn,nodetype=int,create_using=nx.Graph())
        g = g.to_undirected()
        #cas.e_ratio(g,v,fr)
        Gc = max(nx.connected_component_subgraphs(g), key=len)
	nx.write_edgelist(Gc,"temps.txt",data=False)
	size = Gc.number_of_nodes()
	#g2 = nx.convert_node_labels_to_integers(g, first_label=0, ordering='default', label_attribute=None)
	print v,g.number_of_nodes(),g.number_of_edges(),nx.is_connected(Gc)
	#nx.write_edgelist(g,'as_'+str(v)+'.txt',data=False)
	#nx.write_edgelist(g2,gn2,data=False)
	c1 = pickle.load(open("wiki_results1/wiki_"+str(v)+"close.p","rb"))
        c2 = c1.items()
        c3 = sorted(c2,key = lambda x:x[1],reverse=True)
        c4 = c3[:10]
	ms.seed_file(c4,"close")
        cloa = []
        for x in c4:
                cloa.append(x[0])
        c1 = pickle.load(open("wiki_results1/wiki_"+str(v)+"betw.p","rb"))
        c2 = c1.items()
        c3 = sorted(c2,key = lambda x:x[1],reverse=True)
        c4 = c3[:10]
	ms.seed_file(c4,"betw")
        bwoa = []
        for x in c4:
                bwoa.append(x[0])
	output = os.popen('java MultiSpreads '+str(size)+" "+"temps.txt").read()
	out = os.popen('./new_centrality '+'seed_betw.txt '+gn).read()
	op = output.split()
	print out
	print op
	sp.write(str(v)+'\t'+str(op[0])+"\t"+str(op[1])+'\n')
	sp1.write(str(v)+'\t'+str(out)+"\n")
	#top5c.append(cloa)
	#top5b.append(bwoa)
	#os.system('./kcores -i:'+gn+' -o:'+gn1)
	#gcore = nx.read_edgelist(gn1+'.txt',nodetype=int)
	#print gcore.number_of_nodes(),gcore.number_of_edges()
	#topc.append(gcore.nodes())
	#unodes.append(g.number_of_nodes())
	#os.system('rm '+gn1+".txt")
sp.close()
sp1.close()

