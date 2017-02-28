def seed_file(c,e,typ):
		import numpy as np
		c = [x[0] for x in c]
		#np.random.shuffle(c)
		frt = c[:10]
		lst = c[10:]
		e = abs(e)
		count = int((100-e)*0.01*10)
		#print count,10-count
		#print num,count
		sd1 = np.random.choice(np.array(frt),0,replace=False)
		sd2 = np.random.choice(np.array(lst),10,replace=False)
		sd3 = np.concatenate((sd1,sd2))
                f  = open("seed_"+typ+".txt","w")
                for v in sd3:
                        f.write(str(v)+"\n")
                f.close()

