#!/usr/bin/python

import csv


class BankStatementQFX():

	def __init__(self,ccy,route_code,acct_number,acct_type,trans_list):
		self.ccy = ccy
		self.route_code = route_code
		self.acct_number = acct_number
		self.acct_type = acct_type
		self.trans_list = trans_list

	
	
	def print_bank_statement(self):
		self.trans_list.print_transaction_list()

	def bankstatement_to_csv(self,csvfilename,delimiter):
		csvfile_handler = csv.writer(open(csvfilename, 'wb'), delimiter=delimiter,quotechar='"', quoting=csv.QUOTE_MINIMAL)
		header = ['trans_asof_end','trans_type','date_posted','date_user_activity','amount','account_num','name','memo']
		csvfile_handler.writerow(header)		
		for trans in self.trans_list.trans_list_details:
			lst = []
			a = trans.trans_type
			a1 = trans.dt_posted
			a2 = trans.dt_user
			a3 = trans.amount
			a4 = trans.fitid
			a5 = trans.name
			a6 = trans.memo
			#lst.append(self.trans_list.trans_list_start)
			lst.append(self.trans_list.trans_list_end)
			lst.append(a)
			lst.append(a1)
			lst.append(a2)
			lst.append(a3)
			lst.append(a4)
			lst.append(a5)
			lst.append(a6)
			csvfile_handler.writerow(lst)
		

class Transaction():
	def __init__(self,trans_type,dt_posted,dt_user,amount,fitid,name,memo):
		self.trans_type = trans_type
		self.dt_posted = dt_posted
		self.dt_user = dt_user
		self.amount = amount
		self.fitid = fitid
		self.name = name
		self.memo = memo
	
	def print_transaction(self):
		print self.trans_type
		print self.dt_posted
		print self.dt_user
		print self.amount
		print self.fitid
		print self.name
		print self.memo


class TransactionList():
	def __init__(self,trans_list_start,trans_list_end,trans_list_details):
		self.trans_list_start = trans_list_start
		self.trans_list_end = trans_list_end
		self.trans_list_details = trans_list_details

	def print_transaction_list(self):
		print self.trans_list_start
		print self.trans_list_end
		for x in self.trans_list_details:
			x.print_transaction()

	def add_transaction(self,curr_trans):
		self.trans_list_details.append(curr_trans)

def main():
	
	
	trans1 = Transaction('DEBIT','date1','date1a','100.23','fitxx','wellsfargo','some memo')
	trans2 = Transaction('DEBIT','date2','date2a','88.23','fityy','chase','some memo 2')
	temp_list = []
	trans_list = TransactionList('20120518','20120518',temp_list)
	trans_list.add_transaction(trans1)
	trans_list.add_transaction(trans2)
	bst = BankStatementQFX('USD','001','80010233','CHECKING',trans_list)
	bst.print_bank_statement()
	csvfilename = "csvtester.csv"
	delimiter = ";"
	bst.bankstatement_to_csv(csvfilename,delimiter)

if __name__ == '__main__':
	main()
