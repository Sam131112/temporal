import networkx as nx
def ksize(nw):
    if nw.find("graphml") == -1:
    	g = nx.read_edgelist(nw,nodetype=int,data=False)
    else:
	g = nx.read_graphml(nw,node_type=int)
    sh = {}
    se_lp = g.selfloop_edges(data='False')
    g.remove_edges_from(se_lp)
    g1 = g.copy()
    count  = 1
    #print g1.number_of_nodes()
    while g1.number_of_nodes() > 0:
        sh[count] = []
	flag = True
	while flag:
		flag = False
        	nd = g1.nodes()
     	 	for v in nd:
        	    	if g1.degree(v) <= count:
                			g1.remove_node(v)
                			sh[count].append(v)
					flag = True
        count = count + 1
    #print g1.number_of_nodes(),count
    #return (sh,count-1)
    #print sh
    sh1 = {}
    counts = count-1

    #for x in sh:
    #            print x,len(sh[x])
    #print   
    '''
    while counts >=1:
			temp = sh[counts]
			c = counts
			while len(temp)<5:
				c = c-1
				if c <=0:
					break
				else:
					temp = temp + sh[c]
			#print len(temp)
			sh1[c] = temp
			if c<counts:
				counts = c-1
			else:
				counts = counts-1

    for x in sh1:
    		print x,len(sh1[x])
    sh2 = {}
    #print
    n = 1
    for x in  sh1:
    		sh2[n] = sh1[x]
		n = n +1
    #for x in sh2:
    #           print x,len(sh2[x])
    '''
    return sh


if __name__ == "__main__":
    #nts = ["dolphin.txt","football.txt","lemis.txt","as1.txt","as2.txt","power.txt","celegan.txt","grgc_n.txt"]
    nts = ['grgc_n.txt']
    for n in nts:
		count = 0
		g = nx.read_edgelist(n,nodetype=int,data=False)
		se_lp = g.selfloop_edges(data='False')
	        g.remove_edges_from(se_lp)
		sh = ksize(n)	
		for x in sh:
				if len(sh[x])>0:
						count = count + 1
		print n,count
		for x in sh:
			if len(sh[x])>0:
				g1 = g.subgraph(sh[x])
				print g1.number_of_nodes(),nx.density(g1),(1.0*g1.number_of_nodes())/g.number_of_nodes()
		print "\n"

