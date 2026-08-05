text = input("Введите текст: ")

text_lower = text.lower()

vowels = "аеёиоуыэюя"
vowel_count = 0

for char in text_lower:
    if char in vowels:
        vowel_count += 1

punctuation = ".,!?;:-—«»\"'()"
cleaned_text = ""

for char in text_lower:
    if char in punctuation:
        cleaned_text += " "
    else:
        cleaned_text += char

words = cleaned_text.split()

total_words = len(words)
longest_word = ""
word_counts = {}

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print("\n--- Результаты ---")
print("Количество слов:", total_words)
print("Самое длинное слово:", longest_word)
print("Количество гласных:", vowel_count)

print("\nСколько раз встречается каждое слово:")
for word in word_counts:
    print(word, ":", word_counts[word])
