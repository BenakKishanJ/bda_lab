import sys
for line in stdin:
    line=line.strip()
    if not line: continue
    parts = line.split()
    a,b,value= parts
    if a.startswith('U'):
        print "%s\tR\t%s\t%s" %(b,a,value)
    elif a.startswith('I'):
        print "%s\tF\t%s\t%s" %(a,b,value)

