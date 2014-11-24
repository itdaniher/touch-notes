import pylab, numpy, os

def openFile(filename):
	return open(filename).read().split('\r\n')[7:-1]

def smoothListGaussian(list,strippedXs=False,degree=5):  
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


filenames = os.listdir('./').next()[2]
filesToParse = []
for filename in filenames:
	if os.path.splitext(filename)[1] == '.txt':
		filesToParse.append(filename)

for filename in filesToParse:
	data = openFile(filename)
	data = map(float, data)
	data = smoothListGaussian(data, degree=400)
	pylab.plot(data, 'k-')
	pylab.xlabel('milliseconds')
	pylab.ylabel('volts')
	pylab.title(os.path.splitext(filename)[0])
	pylab.savefig(filename+".png", dpi=300)
	pylab.clf()
