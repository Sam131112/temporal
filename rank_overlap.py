def rank(x):
		import numpy as np
		import scipy.stats as st 
		alls = []
		for xa,ya in zip(x,x[1:]):
			x1 = xa[:]
			y1 = ya[:]
			#print "****************************"
			#print x1,len(x1)
			#print "***************************"
			#print y1,len(y1)
			#print "***********************"
			temp = []
			for v in x1:
				if v not in y1:
					temp.append(v)	
			for v in temp:
				x1.remove(v)	
			temp = []
			for v in y1:
                                if v not in x1:
                                        temp.append(v)
			for v in temp:
                                y1.remove(v)
			#print "*************************"
			#print x1
			#print "****************************"
			#print y1
			#print "***************************"
			if len(x1) <=1:
					alls.append(0)
					#print 0
			else:
					alls.append(st.kendalltau(x1,y1)[0])
					#print st.kendalltau(x1,y1)[0]
		return np.mean(alls)
		
