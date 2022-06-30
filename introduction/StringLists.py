jjj = { 'chuck' : 1, 'fred' : 42, 'jan' : 100}
print(list(jjj))
print(jjj.keys())
print(jjj.values())
print(jjj.items())

name = input('Enter file: ')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[words] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
