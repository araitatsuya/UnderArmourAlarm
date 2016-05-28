import time
import urllib2
from urllib2 import urlopen

def  UnderArmourReport(RLSID):
    try:
    	sourceCode = urllib2.urlopen('http://investor.underarmour.com/releasedetail.cfm?ReleaseID='+RLSID).read()
    	RLSDate = sourceCode.split('<div class="wsh_printDate">')[1].split('</div>')[0]
    	H1 = sourceCode.split('<h1>')[1].split('</h1>')[0]
    	H2 = sourceCode.split('<h2>')[1].split('</h2>')[0]
    	print RLSID
    	print RLSDate
    	print H1
    	#print H2

    except Exception, e:
        #print 'failed in the main loop', str(e)
        pass


for x in xrange(952146, 990000):
	UnderArmourReport(str(x))


###########################################################
#
#   Q2 2016?
#       ??????
#
#   Q1 2016
#       966143 (966144)
#
#   Q4 2015
#       952146 (952147)
#
#   Q3 2015
#       937825 (937826)
#
#   Q2 2015
#       923400 (923401)
#
#   Q1 2015
#       907514 (907515)
#
#           May 28th 2016
#                   Tatsuya J. Arai
#                   araitatsuyaj@gmail.com
#
#
###########################################################