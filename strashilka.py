def count_vowels(text):
    vowels = "аеёиоуыэюя"
    return sum(1 for char in text.lower() if char in vowels)


def clean_and_split_text(text):
    punctuation = ".,!?;:-—«»\"'()"
    text_lower = text.lower()
    for char in punctuation:
        text_lower = text_lower.replace(char, " ")
    return text_lower.split()


def find_longest_word(words):
    if not words:
        return ""
    return max(words, key=len)


def count_word_frequencies(words):
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


def main():
    text = input("Введите текст: ")

    vowel_count = count_vowels(text)
    words = clean_and_split_text(text)
    longest_word = find_longest_word(words)
    word_counts = count_word_frequencies(words)

    print("\n--- Результаты ---")
    print("Количество слов:", len(words))
    print("Самое длинное слово:", longest_word)
    print("Количество гласных:", vowel_count)

    print("\nСколько раз встречается каждое слово:")
    for word, count in word_counts.items():
        print(f"{word} : {count}")


if __name__ == "__main__":
    main()
