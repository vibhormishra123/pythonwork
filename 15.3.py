import re
string = 'vibhorformishra'
pattern = 'for'
match=(re.search(pattern, string))


print ("starting index", match.start())


print ("start and end index", match.span())
