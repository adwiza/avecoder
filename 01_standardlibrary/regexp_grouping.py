import re

# print(re.search('(coder)', 'ave coder moder'))
# print(re.search('coder', 'ave coder moder'))

# print(re.search('coder+', 'ave coder moder'))
# print(re.search('coder+', 'ave coderrr moder'))

# print(re.search('(coder)+', 'ave codercoder moder'))
# print(re.search('(coder)+', 'ave codercoderoder moder'))
# print(re.search('(coder)+', 'ave coder moder'))

# print(re.search('([cm]oder){1,5}(noder)?', 'ave codermodernoder'))
# print(re.search('([cm]oder){1,5}(noder)?', 'ave codermoder'))
# print(re.search('([cm]oder){1,5}(noder)?', 'ave moder'))
# print(re.search('([cm]oder){1,5}(noder)?', 'ave modernoder'))


# print(re.search('(ave(coder)?)+(\d{1,3})?', 'avecoder123'))
# print(re.search('(ave(coder)?)+(\d{1,3})?', 'avemaria'))
# print(re.search('(ave(coder)?)+(\d{1,3})?', 'avemaria123'))
# print(re.search('(ave(coder)?)+(\d{1,3})?', 'ave123'))


# m = re.search('(\w+),(\w+),(\w+)', 'ave,coder,moder')
# print(m)
# print(m.groups())
# print(m.group(3))
# print(m.group(0))
# print(m.group(1,2))
# print(len(m.groups()))
# print(len(m.group()))

### BACKREFERENCES ###

# pattern = r'(\w+),\1'

# m = re.search(pattern, 'ave,ave')
# print(m)
#
# m = re.search(pattern, 'coder,coder')
# print(m)
#
# m = re.search(pattern, 'ave,coder')
# print(m)

##### (?P<name><regex>)

m = re.search('(?P<name1>\w+),(?P<name2>\w+),(?P<name3>\w+)', 'ave,coder,moder')

# print(m.groups())
# print(m.group(3))
# print(m.group('name3'))

### (?P<name>)

pattern = r'(\w+),\1'

m = re.search(pattern, 'ave,ave')
print(m)

m = re.search(r'(?P<salutation>\w+),(?P=salutation)', 'ave,ave')
print(m)
print(m.group('salutation'))