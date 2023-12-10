import nltk


# Write phrase structure parsing rules
grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> NN XSN JK | NN JK
VP -> NP VP | VV EP EF
NN -> '아이' | '케이크'
XSN -> '들'
JK -> '이' | '를'
VV -> '먹'
EP -> '었'
EF -> '다'
""")


# Create a rule-based parser
parser = nltk.ChartParser(grammar)


# Perform phrase structure parsing
sent = ['아이', '들', '이', '케이크', '를', '먹', '었', '다']

for tree in parser.parse(sent):
  print(tree)