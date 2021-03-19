from util import fillTemplate
from FillableTemplate import FillableTemplate
import json
import hashlib

f = open("grammar.txt", "r")
grammar_lines = f.readlines()
f.close()

f = open("lex.txt", "r")
lexiconLines = f.readlines()
f.close()


m = hashlib.sha256()
m.update(str(lexiconLines + grammar_lines).encode())
corpus_hash = m.hexdigest()

lexicon = {}

for line in lexiconLines:
	if len(line) > 3:
		key, word = line.strip().split(":")
		if(len(key) > 0 and key[0] != "#"):
			try:
				lexicon[key].append(word)
			except KeyError as e:
				lexicon[key] = [word]

grammar = {}
for line in grammar_lines:
	if len(line) > 3:
		intent, template = line.split(":")
		template_tokenized = template.strip().split(" ")
		ftmp = FillableTemplate(template_tokenized, intent)
		try:
			grammar[intent].append(ftmp)
		except KeyError as e:
			grammar[intent] = [ftmp]

expandedLines = []
for rule in grammar["ROOT"]:
	expandedLines.extend(fillTemplate(rule, lexicon, grammar))


utterances = []
for line in sorted(set(expandedLines), key=lambda x:len(" ".join(x.getTemplate()))):
	utterances.append(" ".join(line.getTemplate()))

f = open("corpus_" + corpus_hash + ".txt", "w")
for line in utterances:
	f.write(line + "\n")
f.close()
