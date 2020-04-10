fname = input('enter text file: ')
fhandle = open(fname)
count = dict()

for line in fhandle:
    line = line.rstrip()
    words = line.split()
    for word in words:
        count[word] = count.get(word,0)+1
print(count.items())

print('top 10 words..')
lst = list()
for key,val in count.items():
    lst.append((val,key))
    lst.sort(reverse=True)
for val,key in lst[:10]:
        print(key, val)
# print(lst)
