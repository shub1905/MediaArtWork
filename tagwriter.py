import fileinfo
import os

rootdir = '/Users/satan/Music/iTunes/iTunes\ Media/Music/'

for root, subdirs, files in os.walk(rootdir):
	print 'heh', subdirs
	for sub in subdirs:
	    for info in fileinfo.listDirectory(sub, [".mp3"]):
	        print "\n".join(["%s=%s" % (k, v) for k, v in info.items()])
