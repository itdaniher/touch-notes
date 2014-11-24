import pylab, numpy, os

def openFile(filename):
	tree = []
	columns = open(filename).read().split('\r\n')
#split into rows by \r\n
	print len(columns)
#print number of datapoints for debugging
	for row in columns:
		try:
			row = row.split('\t')
			row = map(float, row)
			ai0 = row[1]
#analog input 0
			ai1 = row[2]
#analog input 1
			ratio = ai1/ai0
#factor out PSU noise by dividing out the input voltage
			tree.append(ratio)
		except:
			print "data failure"
#last row of every dataset malformed; quick fix
	return tree

def smoothListGaussian(list,strippedXs=False,degree=5):  
#standard gaussian smoothing; not my algo
	window=degree*2-1  
	weight=numpy.array([1.0]*window)  
	weightGauss=[]  
	for i in range(window):  
		i=i-degree+1  
		frac=i/float(window)  
		gauss=1/(numpy.exp((4*(frac))**2))  
		weightGauss.append(gauss)  
	weight=numpy.array(weightGauss)*weight  
	smoothed=[0.0]*(len(list)-window)  
	for i in range(len(smoothed)):  
		smoothed[i]=sum(numpy.array(list[i:i+window])*weight)/sum(weight)  
	return smoothed

if __name__ == '__main__':
	filenames = os.walk('./').next()[2]
#check out files in ./
	filesToParse = []
	for filename in filenames:
		if os.path.splitext(filename)[1] == '.tdv':
#check to see whether they're tab-deliniated-value
#NB: should bt tsv - tab-separated-value, as tab is the separator not deliniator
				filesToParse.append(filename)
	for filename in filesToParse:
		data = openFile(filename)
		data = smoothListGaussian(data, degree=200)
#smoothing with a 200-unit window
		pylab.plot(data, 'k-')
#plot with a black line
		pylab.ylim(0, 1.25)
#fix our y window to between 0 and 1.25
		pylab.ylabel('difference')
#label it 'difference'
		title = os.path.splitext(filename)[0]
#parse filename for dataset title
		pylab.title(title)
		pylab.show()
		pylab.savefig(title+".png", dpi=300)
#save figure
		pylab.clf()
