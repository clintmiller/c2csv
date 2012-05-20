#/usr/bin/python

import csv

class Convert2CSV():
	
	def __init__(self,qfx_lines,qfx_tags):
		self.qfx_lines = qfx_lines
		self.qfx_tags = qfx_tags

	def parse_qfx(self,qfx_file_name):
		#print "Parsing QFX file now...."		
		#read file
		file_reader = open(qfx_file_name, 'r')
		# read lines
		all_lines = file_reader.readlines()
		# add to qfxNodes
		for line in all_lines:
			#print line
			#Remove blank lines and add to qfx_nodes list
			self.qfx_lines.append(line.strip())
				
			

	def qfx_2_csv(self):
		# open csv writer
		# read qfxNodes
		# write to csv file
		print "Writing to CSV now...."
qfx_lines = []
qfx_tags = ['<OFX>','<BANKACCTFROM>','<BANKID>','<ACCTID>','<ACCTTYPE>','<BANKTRANLIST>','<DTSTART>','<DTEND>','<STMTTRN>','<TRNTYPE>','<DTPOSTED>','<DTUSER>','<TRNAMT>','<FITID>','<NAME>','<MEMO>','<LEDGERBAL>','<BALAMT>','<DTASOF>',]
qfx_file_name = "quickenExport.QFX"

myC2csv = Convert2CSV(qfx_lines,qfx_tags)
myC2csv.parse_qfx(qfx_file_name)
#myC2csv.qfx_2_csv()
for x in qfx_lines:
	print x		
