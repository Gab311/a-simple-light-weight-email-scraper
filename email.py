import re

emailregex = re.compile("""
[a-z A-Z 0-9 ._?/\%$#*,;`]+
@
[a-z A-Z 0-9 ._?/\%$#*,;`]+
.
[a-z A-Z 0-9 ._?/\%$#*,;`]+


""", re.VERBOSE)
scraped = []
print("Input what you want to scrape")
spam = input()
egg = emailregex.findall(spam)
for i in egg:
    scraped.append(egg[0])
s = ", ".join(scraped)
print(s)
