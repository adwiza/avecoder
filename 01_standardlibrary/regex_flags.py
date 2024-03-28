import re

### re.I ### re.IGNORECASE

# print(re.search('x+', 'xxxXXX'))
# print(re.search('X+', 'xxxXXX'))

# print(re.search('x+', 'xxxXXX', re.I))
# print(re.search('X+', 'xxxXXX', re.IGNORECASE))
#
# print(re.search('[a-z]+', 'aVeCoDeR', re.I))
# print(re.search('[a-z]+', 'aVeCoDeR', re.IGNORECASE))

### re.M ### re.MULTILINE


s = 'ave\ncoder\nmoder'

# print(s)
#
# print(re.search('^ave', s))
# print(re.search('^coder', s))
# print(re.search('^moder', s))
#
# print(re.search('ave$', s))
# print(re.search('coder$', s))
# print(re.search('moder$', s))
#
# print(re.search('^ave', s, re.M))
# print(re.search('^coder', s, re.M))
# print(re.search('^moder', s, re.M))

### re.S ### re.DOTALL

# print(re.search('ave.coder', 'ave\ncoder'))
# print(re.search('ave.coder', 'ave\ncoder', re.DOTALL))
# print(re.search('ave.coder', 'ave\ncoder', re.S))

### re.X ### re.VERBOSE

regex = r'^(\(\d{3}\))?\s*\d{3}[-.]\d{4}$'

# print(re.search(regex, '123.4567'))
# print(re.search(regex, '123-4567'))
# print(re.search(regex, '(890)123-4567'))
# print(re.search(regex, '(890) 123-4567'))

# regex = '''^
#             (\(\d{3}\))?
#             \s*
#             \d{3}
#             [-.]
#             \d{4}
#             $
#             '''

# print(re.search(regex, '123.4567', re.VERBOSE))
# print(re.search(regex, '123-4567', re.VERBOSE))
# print(re.search(regex, '(890)123-4567', re.VERBOSE))
# print(re.search(regex, '(890) 123-4567', re.VERBOSE))

### re.DEBUG

# print(re.search('ave.coder', 'aveXcoder', re.DEBUG))
# print(re.search(regex, '123.4567', re.DEBUG))

### re.A ### re.ASCII
### re.U ### re.UNICODE
### re.L ### re.LOCALE

s = '\u0437\u042E\u0437\u044F'

# print(s)
#
# print(re.search('\w+', s))

s = 'sch\u00f6n'

# print(s)
#
# print(re.search('\w+', s, re.ASCII))
# print(re.search('\w+', s, re.UNICODE))
# print(re.search('\w+', s))

### Combine

# print(re.search('^ave', 'AVE\nCODER\n\MODER', re.I|re.M))

### (?<flags>)

print(re.search('^ave', 'AVE\nCODER\n\MODER', re.I|re.M))
print(re.search('(?im)^ave', 'AVE\nCODER\n\MODER'))

print(re.search('(?s)ave.coder.moder', 'AVE\nCODER\n\MODER'))

### (?<set_flags>-<remove_flags>:<regex>)

print(re.search('(?i:ave)coder', 'AVEcoder'))
print(re.search('(?i:ave)coder', 'AVECODER'))