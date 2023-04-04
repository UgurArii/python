import re

text = "foo   bar\t baz \tqux"

print(re.split('\s+', text))
regex = re.compile('\s+')

print(regex.findall(text))

text1 = """Dave dave@google.com
Steve steve@gmail.com
Rob rob@gmail.com
Ryan ryan@yahoo.com
"""

pattern = r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'

regex = re.compile(pattern, flags=re.IGNORECASE)
print(regex.findall(text1))
m = regex.search(text1)
print(m)
print(text1[m.start():m.end()])
print(regex.match(text1))
print(regex.sub('REDACTED', text1))
pattern = r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'
regex = re.compile(pattern, flags=re.IGNORECASE)
m = regex.match('wesm@bright.net')
print(m.groups())
print(regex.findall(text1))
print(regex.sub(r'Username: \1, Domain: \2, Suffix: \3', text1))
