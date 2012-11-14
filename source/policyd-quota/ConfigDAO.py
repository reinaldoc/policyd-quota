
import ConfigParser

class ConfigDAO(object):
	def __init__(self, configfile):
		self.config = ConfigParser.RawConfigParser()
		self.config.read(configfile)
		print self.config.sections()
	
