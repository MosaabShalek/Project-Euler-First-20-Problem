import inflect

p = inflect.engine()
counter = 0
for i in range(1,1001):
    c = p.number_to_words(i)
    c = c.replace(' ', '')
    c = c.replace('-', '')
    counter += len(c)
print(counter)

