word = 'word'
result = [itm.upper() for i, itm in enumerate(word, 1) if not i & 1]
print(result)
