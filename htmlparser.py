# -*- coding: utf-8 -*-
import HTMLParser

class TabularHTMLParser(HTMLParser.HTMLParser, object):
	def __init__(self):
		super(TabularHTMLParser, self).__init__()
		self.PassedHeader = False
		self.LinesOfHeader = 2
		self.ColumnCount = 0
		self.RowData = []
		self.Result = []
		self.Header = []
		self.TmpData = ''

 	def handle_starttag(self, tag, attrs):
 		#print 'start tag: ', tag, tag=='tr'
 		if tag == 'tr':
 			self.RowData = []
 		elif tag == 'td' or tag == 'th':
 			self.TmpData = ''
 		else:
 			pass
 
 	def handle_endtag(self, tag):
 		#print 'end tag: ', tag, tag=='tr'
 		if tag == 'tr':
 			if self.LinesOfHeader <= 0:
 				if len(self.RowData) > 0 and self.ColumnCount == len(self.RowData):
 					self.Result.append(self.RowData)
 			else:
 				self.LinesOfHeader -= 1
 				#print 'header append', self.RowData
 				if len(self.RowData) > 0:
 					self.Header.append(self.RowData)
 					self.ColumnCount = len(self.RowData)
 		elif tag == 'td' or tag == 'th':
	 		self.RowData.append(self.TmpData)
	 	else:
 			pass
 
 	def handle_data(self, data):
 		if not data == '\n':
 			self.TmpData += data
 
 	def unknown_decl(self, data):  
 		"""Override unknown handle method to avoid exception"""  
 		pass  
