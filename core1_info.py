def e_ratio(g,i,f):
		import pickle
		import numpy as np
		import networkx as nx
		from collections import defaultdict
		g.remove_edges_from(g.selfloop_edges())
		g = g.to_undirected()
		diff = defaultdict(int)
		gcore_edge = defaultdict(int)
		gcores = {}
		cn = nx.core_number(g)
		cnum = sorted(list(set(cn.values())),reverse=False)
		#print cnum
		for x1 in cnum:
				gcores[x1] = nx.k_core(g,k=x1)
		for cr in gcores:
				print cr,gcores[cr].number_of_nodes(),gcores[cr].number_of_edges(),nx.density(gcores[cr])		
		'''
		gcore = nx.k_core(g,k=cnum[-1])
		dg = g.degree(gcore.nodes())
		all_e = g.edges(gcore.nodes())
		
	        c1 = pickle.load(open("caida_"+str(i)+"close.p","rb"))
        	c2 = c1.items()
        	c3 = sorted(c2,key = lambda x:x[1],reverse=True)
       		c4 = c3[:20]
        	cloa = []
        	for x in c4:
                	cloa.append(x[0])
		top_close = set(gcore.nodes()).intersection(set(cloa))
        	c1 = pickle.load(open("caida_"+str(i)+"betw.p","rb"))
        	c2 = c1.items()
        	c3 = sorted(c2,key = lambda x:x[1],reverse=True)
        	c4 = c3[:20]
        	bwoa = []
        	for x in c4:
                	bwoa.append(x[0])
		
		top_bet = set(gcore.nodes()).intersection(set(bwoa))
		#print len(all_e),gcore.number_of_nodes(),gcore.number_of_edges(),sum(dg.values())
		for u,v in all_e:
			 gcore_edge[cn[u]] = gcore_edge[cn[u]]+1
			 gcore_edge[cn[v]] = gcore_edge[cn[v]]+1
		diffs  = gcore_edge.items()
		diffs= sorted(diffs,key = lambda x:x[0],reverse = False)
		den = len(all_e)-gcore.number_of_edges()
		#start = [(x[1]/float(den))*nx.density(gcores[x[0]]) for x in diffs[:5]]
		#end = [(x[1]/float(den))*nx.density(gcores[x[0]]) for x in diffs[-6:-1]]
		start = [(x[1]/float(den)) for x in diffs[:5]]
                end = [(x[1]/float(den)) for x in diffs[-6:-1]]

		print "Core and Edge"
		for v in gcore_edge:
				print v,gcore_edge[v]
		#print -np.log(np.array(start)),-np.log(np.array(end))
		#f.write(str(i)+'\t'+str(len(top_bet))+'\t'+str(len(top_close))+'\n')
		f.write(str(i)+'\t'+str(start[0])+'\t'+str(start[1])+'\t'+str(start[2])+'\t'+str(start[3])+'\t'+str(start[4])+'\t'+str(end[0])+'\t'+str(end[1])+'\t'+str(end[2])+'\t'+str(end[3])+'\t'+str(end[4])+'\n')
'''
