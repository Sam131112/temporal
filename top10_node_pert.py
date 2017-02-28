import networkx as nx
import numpy
import random

# Find Top 10 nodes jaccard for addition and deletions
    

if __name__ == "__main__":
    #nts = ["football.txt","lemis.txt","as1.txt","as2.txt","power.txt","celegan.txt","grgc_n.txt"]
    nts = ["football.txt"]
    n = [0.2,0.4,0.6,0.8,1]
    for ns in nts:
        i = ns.find(".")
        nw = ns[0:i]
        g = nx.read_edgelist("new_"+ns,nodetype=int)
        g1 = nx.read_graphml(nw+"_new"+".graphml",node_type=int)
        c1 = nx.closeness_centrality(g)
        c2 = c1.items()
        c3 = sorted(c2,key = lambda x:x[1],reverse=True)
        c4 = c3[:10]
        cloa = []
        for x in c4:
                cloa.append(x[0])
        c1 = nx.betweenness_centrality(g)
        c2 = c1.items()
        c3 = sorted(c2,key = lambda x:x[1],reverse=True)
        c4 = c3[:10]
        bwoa = []
        for x in c4:
                bwoa.append(x[0])
        c1 = nx.closeness_centrality(g1)
        c2 = c1.items()
        c3 = sorted(c2,key = lambda x:x[1],reverse=True)
        c4 = c3[:10]
        clod = []
        for x in c4:
                clod.append(x[0])
        c1 = nx.betweenness_centrality(g1)
        c2 = c1.items()
        c3 = sorted(c2,key = lambda x:x[1],reverse=True)
        c4 = c3[:10]
        bwod = []
        for x in c4:
                bwod.append(x[0])
        c10u = []
        c10a = []
        b10u = []
        b10a = []	
        for n1 in n:
                    jcs1 = []
                    jcs2 = []
                    jcs3 = []
                    jcs4 = []
                    for x in range(1,6):
                        nw1 =  str(nw)  +"_new"+str(n1)+str(x)+".graphml"
                        nw2 = "ad" + str(n1) + '_'+str(x)+str(ns)
                        g2 = nx.read_graphml(nw1,node_type=int)
                        g3 = nx.read_edgelist(nw2,nodetype=int)
                        c1 = nx.closeness_centrality(g2)
                        c2 = c1.items()
                        c3 = sorted(c2,key = lambda x:x[1],reverse=True)
                        c4 = c3[:10]
                        clp1 = [] 
                        for x in c4:
                            clp1.append(x[0])
                        c1 = nx.betweenness_centrality(g2)
                        c2 = c1.items()
                        c3 = sorted(c2,key = lambda x:x[1],reverse=True)
                        c4 = c3[:10]
                        bwp1 = []
                        for x in c4:
                            bwp1.append(x[0])
                        c1 = nx.closeness_centrality(g3)
                        c2 = c1.items()
                        c3 = sorted(c2,key = lambda x:x[1],reverse=True)
                        c4 = c3[:10]
                        clp2 = []
                        for x in c4:
                            clp2.append(x[0])
                        c1 = nx.betweenness_centrality(g3)
                        c2 = c1.items()
                        c3 = sorted(c2,key = lambda x:x[1],reverse=True)
                        c4 = c3[:10]
                        bwp2 = []
                        for x in c4:
                            bwp2.append(x[0])
                        num = set(clod).intersection(set(clp1))
                        den = set(clod).union(set(clp1))
                        j1 = len(num)/(1.0*len(den))
                        jcs1.append(j1)
                        num = set(bwod).intersection(set(bwp1))
                        den = set(bwod).union(set(bwp1))
                        j1 = len(num)/(1.0*len(den))
                        jcs2.append(j1)
                        num = set(cloa).intersection(set(clp2))
                        den = set(cloa).union(set(clp2))
                        j1 = len(num)/(1.0*len(den))
                        jcs3.append(j1)
                        num = set(bwoa).intersection(set(bwp2))
                        den = set(bwoa).union(set(bwp2))
                        j1 = len(num)/(1.0*len(den))
                        jcs4.append(j1)
                    c10u.append(numpy.mean(jcs1))
                    c10a.append(numpy.mean(jcs3))
                    b10u.append(numpy.mean(jcs2))
                    b10a.append(numpy.mean(jcs4))
        print ns,"Top 10 Deletion","closenesss jaccard",str(numpy.mean(c10u)),"betweeness",str(numpy.mean(b10u))
        print ns,"Top 10 Additive","closenesss jaccard",str(numpy.mean(c10a)),"betweeness",str(numpy.mean(b10a))
        print "\n"			

