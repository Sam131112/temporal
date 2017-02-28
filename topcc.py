#create a dictionary of closeness and betweenness for caida network from precompute values
import csv
import pickle
f = open("files_all.txt","r")
for row in f:
		row = row.strip('\r\n')
		rows = row.split(".")
		f1 = open("cum_hepph_result/"+row,'r')
		f1.readline()
		f1.readline()
		f1.readline()
		ft = csv.reader(f1,delimiter='\t')
		cl = {}
		bt = {}
		for r1 in ft:
			cl[int(r1[0])] = float(r1[2])
			bt[int(r1[0])] = float(r1[3])
		#for k1,k2 in zip(cl,bt):
		#	print k1,cl[k1],k2,bt[k2]
		pickle.dump(cl,open('cum_hepph_result1/'+rows[0]+"close"+".p","w"))
		pickle.dump(bt,open('cum_hepph_result1/'+rows[0]+"betw"+".p","w"))
		f1.close()

f.close()
