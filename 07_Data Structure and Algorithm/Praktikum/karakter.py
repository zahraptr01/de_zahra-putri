def collect_chars(word, rooms):
    repetition = rooms // len(word)
    remainder = rooms % len(word)
    result = word * repetition + word[:remainder]
    return result

print(collect_chars("alta", 10))
print(collect_chars("sepulsa", 20))
print(collect_chars("sepulsa mantap", 20))
    