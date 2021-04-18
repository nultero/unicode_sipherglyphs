from package import package

with open('cipher.txt', 'r+') as chars:
    package(chars.read(), flag='to_cipher')