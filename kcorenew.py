import networkx as nx
def ksize(g):
    sh = {}
    g1 = g.copy()
    print nx.is_directed(g1)
    count  = 1
    #print g1.number_of_nodes()
    while g1.number_of_nodes() > 0:
        sh[count] = []
	flag = True
	while flag:
		flag = False
        	nd = g1.nodes()
     	 	for v in nd:
        	    	if g1.in_degree(v) <= count:
                			g1.remove_node(v)
                			sh[count].append(v)
					flag = True
        count = count + 1
    #print g1.number_of_nodes(),count
    #return (sh,count-1)
    #print sh
    sh1 = {}
    counts = count-1

    for x in sh:
                for y in sh[x]:
			sh1[y]=x
    #for y in sh:
    #				print y,len(sh[y])
    return sh
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
    #return (sh2,n)
