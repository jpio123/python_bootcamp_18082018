import sys

emails = set()

with open(sys.argv[1], encoding='utf-8') as f:

    raw = f.read(      )
    raw = raw.splitlines()

    emails = set()

    for line in raw:
        line = line.lower().strip()
        if line.count("@") == 1:
            emails.add(line)


with open(sys.argv[2], 'w') as f_out:
    for line in sorted(emails):
        f_out.write(line + '\n')

