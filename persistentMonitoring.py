# -*- coding: utf-8 -*-ç
#Version: 0.0.5

import urllib
import psutil
import os
import time
import sys
from PyQt4 import QtGui  
from PyQt4.QtGui import QMessageBox  
aplicacion = QtGui.QApplication(sys.argv)


i = 0
while i == 0:
	cpu = psutil.cpu_percent()
	time.sleep( 1 )
	if cpu > 30.0:
			
			cpu = psutil.cpu_percent()
			os.system('netstat > net.html')
			scan = "net.html"
			lines = urllib.urlopen(scan).read()
			search = lines.find('coinhive')
			search1 = lines.find('rs-solution.de')
			search2 = lines.find('ns3033653.ip-164')
			search3 = lines.find('104.25.6.31')
			search4 = lines.find('104.24.104.76')
			search5 = lines.find('104.18.55.211')
			search6 = lines.find('104.27.185.32')
			search7 = lines.find('ns546545.ip-158-6')
			search8 = lines.find('beta00.cortacoin')
			search9 = lines.find('mail.aba.ae')
			search10 = lines.find('104.31.93.36')
			search11 = lines.find('104.31.92.36')
			search12 = lines.find('ec2-52-57-80-78')
			search13 = lines.find('5.255.86.116')
			search14 = lines.find('45.77.196.10')
			search15 = lines.find('45.63.109.36')
			search16 = lines.find('207.246.116.117')
			search17 = lines.find('45.77.192.104')
			search18 = lines.find('188.166.33.242')			
			search19 = lines.find('178.62.227.52')	 		
			search20 = lines.find('104.18.46.158')
			search21 = lines.find('104.27.152.155')
			search22 = lines.find('104.18.54.211')
			search23 = lines.find('crypto-webminer')
			search24 = lines.find('104.28.16.102')
			search25 = lines.find('ns3083487.ip-145')
			search26 = lines.find('ns3104461.ip-54')

			if search != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with Coinhive',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search1 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with gustaver.ddns.net',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search2 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with pon.ewtuyytdf45.com',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search3 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with crypto-loot.com',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search4 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with mepirtedic.com',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search5 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with aster18cdn.nl',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search6 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with cdn.whysoserius.club',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search7 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with gtg02.bestsecurepractice.com',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search8 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with beta00.cortacoin.com',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search9 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with "mail.aba.ae" used by: freecontent.*, hashing.win, webassembly.stream, coinimp.com...',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search10 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with crypto-loot.com',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search11 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with crypta-loot.com',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search12 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with webminerpool.com',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search13 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with Proxy: wss://javascriptcdn.stream:8892/proxy , Coinhive',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search14 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with: herphemiste.com',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search15 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with: herphemiste.com',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search16 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with: herphemiste.com',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search17 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with: herphemiste.com',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search18 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with: web.stati.bid',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search19 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with: g-content.bid',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search20 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with: coin-have.com',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search21 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with: 1q2w3.website',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search22 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with aster18cdn.nl',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search23 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with eth-pocket.de',
				QMessageBox.Ok,
				QMessageBox.Ok)	
			elif search24 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with tulip18.com/amo.js',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search25 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining s2.skencituer.com',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search26 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining s3.skencituer.com',
				QMessageBox.Ok,
				QMessageBox.Ok)

			time.sleep( 10 )
