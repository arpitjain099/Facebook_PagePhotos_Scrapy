import wgetter
import csv
import os.path
import nameofpage as n
with open(n.nameofpage+'csv.csv', 'r') as csvfile:
	spamreader = csv.reader(csvfile)
	for index,i in enumerate(spamreader):
		if index > 0:
			print i[0]
			
			l=i[0].split("/")[-1]
			if '?' in l:
				l=l.split("?")[0]
			print n.nameofpage+'/'+l
			if os.path.exists(n.nameofpage+'/'+l):
				print "already exists"
			else:
				wgetter.download(i[0], outdir=n.nameofpage+'/')

