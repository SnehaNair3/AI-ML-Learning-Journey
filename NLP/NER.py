
import spacy

nlp=spacy.load('en_core_web_sm')

nlp.pipe_names

text = nlp("Tesla Inc is going to acquire twitter for $45 billion")

for ent in text.ents:
  print(ent.text, " | ", ent.label_, " | ", spacy.explain(ent.label_))



from spacy import displacy

displacy.render(text, style="ent")



text2 = nlp("Elon Musk runs an organisation named Tesla")

from spacy import displacy

displacy.render(text2, style="ent")

nlp.pipe_labels['ner']

doc = nlp("Michael Bloomberg founded Bloomberg in 1982")

from spacy import displacy

displacy.render(doc, style="ent")



# Setting own entities

doc = nlp("Tesla Inc is going to acquire twitter for $45 billion")
for ent in doc.ents:
  print(ent.text, " | ", ent.label_)


s = doc[3:6]
s
type(s)


from spacy.tokens import Span

s1 = Span(doc, 0, 2, label='ORG')
s2 = Span(doc, 8,11, label='ORG')

doc.set_ents([s1,s2], default='unmodified')


for ent in doc.ents:
  print(ent.text, " | ", ent.label_)


text2 = nlp("Satyajit Pattnaik runs an organisation named Zep Analytics")

s1 = Span(doc, 0, 2, label='PERSON')
s2 = Span(doc, 6,8, label='ORG')

text2.set_ents([s1,s2], default='unmodified')

from spacy import displacy

displacy.render(text2, style="ent")