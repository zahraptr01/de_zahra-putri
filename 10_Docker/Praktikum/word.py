def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

sample_text = "latihan tugas alterra"

result = count_words(sample_text)
print(f"Jumlah kata dalam teks : {result} ")