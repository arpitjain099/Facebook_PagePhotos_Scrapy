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
			print n.nameofpage+'/'+l
			if os.path.exists(n.nameofpage+'/'+l):
				print "already exists"
			else:
				wgetter.download(i[0], outdir=n.nameofpage+'/')

from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import PageBreak
from reportlab.lib import colors
from reportlab.platypus import Paragraph, Frame, Spacer, Image, Table, TableStyle, SimpleDocTemplate
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics.charts.legends import Legend
import wgetter
import csv
import os.path
import nameofpage as n
from PIL import Image as pilimage
def calltofunction(count,story):
	doc = SimpleDocTemplate(n.nameofpage+"/"+n.nameofpage+str(count)+'.pdf',pagesize=landscape(letter), topMargin=.13* inch)
	doc.build(story)


story = []
styles = getSampleStyleSheet()
styleN = styles['Normal']
count=0
globalcount=0
with open(n.nameofpage+'csv.csv', 'r') as csvfile:
	spamreader = csv.reader(csvfile)
	for index,i in enumerate(spamreader):
		if index > 0:
			#par=Paragraph("\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n",styles['Normal'])
			#par.hAlign = 'CENTER'
			#story.append(par)

			l=i[0].split("/")[-1]
			if '?' in l:
				l=l.split("?")[0]
			if os.path.exists(n.nameofpage+'/'+l):
				#im2=pilimage.open(n.nameofpage+'/'+l)
				#print im2.size
				






				im = Image(n.nameofpage+'/'+l, width=11*inch, height=7*inch)
				im.hAlign = 'CENTER'
				story.append(im)
				par=Paragraph("\n"+i[1],styles['Normal'])
				par.hAlign = 'CENTER'
				story.append(par)
				story.append(PageBreak())
				if count>100:
					calltofunction(globalcount+1,story)
					count=0
					story=[]
					globalcount=globalcount+1
					print globalcount
				count=count+1