#python3
import pandas

def getPvar(vals, mean):
    N = len(vals)
    su = 0
    for i in range(len(vals)):
        su = su + ((vals[i]-mean)*(vals[i]-mean))
    pvar = (1/N) * su
    return pvar

def getMean(vals):
    su = 0
    for i in range(len(vals)):
        su = su + vals[i]
    mean = su/(len(vals))
    return mean

def getMeanofDiffs(xvals, yvals):
    su = 0
    for i in range(len(xvals)):
        su = su + ((xvals[i] - yvals[i])*(xvals[i] - yvals[i]))
    meanodiffs = su/(len(xvals))
    return meanodiffs

def getCCC(pvarfe,pvarexp,meanofdiff,meanfe,meanexp):
    bottom = pvarfe + pvarexp + ((meanfe - meanexp)*(meanfe - meanexp))
    answer = 1 - (meanofdiff / bottom)
    return answer

def run(infile):
    data = pandas.read_csv(infile,header = 0)
    expdata = data['Exp'].tolist()
    fedata = data['FE'].tolist()
    meanfe = getMean(fedata)
    meanexp = getMean(expdata)
    meanofdiff = getMeanofDiffs(fedata,expdata)
    pvarfe = getPvar(fedata, meanfe)
    pvarexp = getPvar(expdata, meanexp)
    print('meanfe = ' + str(meanfe) + '\nmeanexp = ' + str(meanexp) + '\npvarfe = ' +str(pvarfe) + '\npvarexp = ' + str(pvarexp))
    print('ccc = ' + str(getCCC(pvarfe,pvarexp,meanofdiff,meanfe,meanexp)))

run('values.txt')
