#!/usr/bin/python

import sys
import csv
from bank_statement_qfx import *

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
		# add each line to qfx list
		for line in all_lines:
			#Remove blanks/newlines
			self.qfx_lines.append(line.strip())
		
		ccy = ""
		routeCode = ""
		acctNumber = ""
		acctType = ""	
		dtStart = ""
		transTypeList = []
		transPostedList = []
		transUserList = []
		transAmountList = []
		transFitIdList = []
		transNameList = []
		transMemoList = []

		for tagline in self.qfx_lines:
			
			ccyTag = tagline.find("<CURDEF>",0,len(tagline))
			routeCodeTag = tagline.find("<BANKID>",0,len(tagline))
			acctNumberTag = tagline.find("<ACCTID>",0,len(tagline))
			acctTypeTag = tagline.find("<ACCTTYPE>",0,len(tagline))
			transListTag = tagline.find("<BANKTRANLIST>",0,len(tagline))
			dtStartTag = tagline.find("<DTSTART>",0,len(tagline))
			dtEndTag = tagline.find("<DTEND>",0,len(tagline))
			
			# transactions tags
			
			transTypeTag = tagline.find("<TRNTYPE>",0,len(tagline))
			if transTypeTag >=0:
				transTypeList.append(tagline[9:])

			transPostedTag = tagline.find("<DTPOSTED>",0,len(tagline))
			if transPostedTag >=0:
				transPostedList.append(tagline[10:])

			transUserTag = tagline.find("<DTUSER>",0,len(tagline))
			if transUserTag >=0:
				transUserList.append(tagline[8:])
		
			transAmountTag = tagline.find("<TRNAMT>",0,len(tagline))
			if transAmountTag >=0:
				transAmountList.append(tagline[8:])

			transFitIdTag = tagline.find("<FITID>",0,len(tagline))
			if transFitIdTag >=0:
				transFitIdList.append(tagline[7:])
			
			transNameTag = tagline.find("<NAME>",0,len(tagline))
			if transNameTag >=0:
				transNameList.append(tagline[6:])

			transMemoTag = tagline.find("<MEMO>",0,len(tagline))
			if transMemoTag >=0:
				transMemoList.append(tagline[6:])

			if ccyTag >=0:
				ccy = tagline[8:]
			if routeCodeTag >=0:
				routeCode = tagline[8:]
			if acctNumberTag >=0:
				acctNumber = tagline[8:]
			if acctTypeTag >=0:
				acctType = tagline[10:]
			if dtStartTag >=0:
				dtStart = tagline[9:]
			if dtEndTag >=0:
				dtEnd = tagline[7:]
		"""	
		print ccy
		print routeCode
		print acctNumber
		print acctType	
		print dtStart
		print dtEnd
		print "length of transTypeList = ",len(transTypeList)
		"""
		temp_list = []
	 	trans_list = TransactionList(dtStart,dtEnd,temp_list)	

		for x in range (len(transTypeList)):
			currTransaction = Transaction(transTypeList[x],transPostedList[x],transUserList[x],\
			transAmountList[x],transFitIdList[x],transNameList[x],transMemoList[x])
			trans_list.add_transaction(currTransaction)
		bst = BankStatementQFX(ccy,routeCode,acctNumber,acctType,trans_list)
		return bst
	
		
		
	
def main(argv):
	qfx_lines = []
	qfx_tags =['<OFX>','<BANKACCTFROM>','<BANKID>','<ACCTID>','<ACCTTYPE>','<BANKTRANLIST>','<DTSTART>','<DTEND>','<STMTTRN>','<TRNTYPE>','<DTPOSTED>','<DTUSER>','<TRNAMT>','<FITID>','<NAME>','<MEMO>','<LEDGERBAL>','<BALAMT>','<DTASOF>',]
	#qfx_file_name = "quickenExport.QFX"
	qfx_file_name = argv[1]
	csvfilename = argv[2]
	delimiter = ";"

	myC2csv = Convert2CSV(qfx_lines,qfx_tags)
	bst = myC2csv.parse_qfx(qfx_file_name)
	bst.bankstatement_to_csv(csvfilename,delimiter)

if __name__ == '__main__':
	main(sys.argv)
