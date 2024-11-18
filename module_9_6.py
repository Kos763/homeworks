def all_variants(text):
    b = len(text)
    for i in range(1, b + 1):
        for c in range(b - i + 1):
            yield text[c:c + i]


a = all_variants("abc")
for i in a:
    print(i)
