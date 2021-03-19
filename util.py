from FillableTemplate import FillableTemplate

def fillTemplate(ftmp, lexicon, grammar):
	fills = []

	if(validateTemplate(ftmp, lexicon, grammar)):
		fills.append(ftmp)
		return fills

	template_tok = ftmp.getTemplate()
	
	branched = False
	for i in range(len(template_tok)):
		token = template_tok[i]
		if(token in lexicon.keys()):
			datum = lexicon[token]
			for word in datum:
				temp_template_tok = template_tok[:i] + [word] + template_tok[i+1:]
				ftmp_update = FillableTemplate(temp_template_tok, ftmp.getIntent())
				fills.extend(fillTemplate(ftmp_update, lexicon, grammar))
				branched = True
		if(token in grammar.keys()):
			datum = grammar[token]
			for rule in datum:
				temp_template_tok = template_tok[:i] + rule.getTemplate() + template_tok[i+1:]
				ftmp_update = FillableTemplate(temp_template_tok, ftmp.getIntent())
				fills.extend(fillTemplate(ftmp_update, lexicon, grammar))
				branched = True
		if(branched):
			break
	return fills
				

def validateTemplate(to_valid, lexicon, grammar):
	for word in to_valid.getTemplate():
		if(word in lexicon.keys()):
			return False
		if(word in grammar.keys()):
			return False
	return True


