import re

### (?=<lookahead_regex>)

# print(re.search('ave(?=[a-z])', 'avecoder'))
# print(re.search('ave(?=[a-z])', 'ave000coder'))
# print(re.search('ave([a-z])', 'avecoder'))

### (?!=<lookahead_regex>)

# print(re.search('ave(?=[a-z])', 'avecoder'))
# print(re.search('ave(?![a-z])', 'ave000coder'))
# print(re.search('ave(?![a-z])', 'avecoder000'))

### (?<=<lookbehind_regex>)
# print(re.search('(?<=ave)coder', 'avecoder'))
# print(re.search('(?<=ave)coder', 'coderaveR'))

# print(re.search('(?<=a+)ve', 'aaaaaavecoder'))
# print(re.search('(?<=a{5})ve', 'aaaaaaavecoder'))

### (?!<=<lookbehind_regex>)
print(re.search('(?<!ave)coder', 'avecoder'))
print(re.search('(?<!coder)ave', 'avecoder'))
