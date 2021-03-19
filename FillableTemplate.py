import hashlib

class FillableTemplate:
	def __init__(self, template, intent):
		self.__template = template
		self.__intent = intent

	def getIntent(self):
		return self.__intent

	def setTemplate(self, template):
		self.__template = template

	def getTemplate(self):
		return self.__template
		
	def __str__(self):
		return str(self.__template)

	def getAsJson(self):
		return {"text": " ".join(self.__template), "intent":str(self.__intent)}

	def __hash__(self):
		return int(hashlib.sha224(str(self.getAsJson()).encode("utf-8")).hexdigest(), 16)

	def __eq__(a, b):
		return hash(a) == hash(b)