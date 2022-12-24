string_unicode = " Python is easy \u200c to learn. "
string_encode = string_unicode.encode("ascii", "ignore")
string_decode = string_encode.decode()
print(string_decode)