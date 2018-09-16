import re

post_code_pattern = re.compile('\d{2}-\d{3}')
email_pattern = re.compile('[a-zA-Z0-9.\-_]+@[a-zA-Z0-9.\-_]+\.\w+')
date_pattern = re.compile('\d{2} \w\w\w \d{4}')
with open("input.txt") as f:
    tekst = f.read()
    kody = post_code_pattern.findall(tekst)
    print(kody)
    emaile = email_pattern.findall(tekst)
    print(emaile)
    daty = date_pattern.findall(tekst)
    print(daty)