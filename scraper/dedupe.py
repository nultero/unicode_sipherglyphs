def dedupe(cipherkeys=str):
    chars = []
    for i in cipherkeys:
        if i in chars:
            pass
        else: # i not in chars
            chars.append(i)

    return chars