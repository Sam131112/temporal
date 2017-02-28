def jaccards(x,n):
		f = open(n+".txt","w")
		count = 1 
		for x1,y1 in zip(x,x[1:]):
				num = set(x1).intersection(set(y1))
	                        den = set(x1).union(set(y1))
        	                j1 = len(num)/(1.0*len(den))
				f.write(str(count)+'\t'+str(j1)+'\n')
				count = count+1
		f.close()
