import json
import codecs

class ImportMapping(object):
	def __init__(self, mappingfile):
		f = codecs.open(mappingfile, 'r', 'utf-8')
		fstr = f.read()
		f.close()
		self.mapping = json.loads(fstr)
	
	def Match(self, headerlist):
		for mapping in self.mapping:
			if mapping['Columns'] == headerlist:
				return mapping
			else:
				pass
		return None

otcQFIISMapping = ImportMapping('otcQFIISImportMapping.json')
twseQFIISMapping = ImportMapping('twseQFIISImportMapping.json')
