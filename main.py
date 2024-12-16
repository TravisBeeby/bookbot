from collections import Counter

def read_book():
    # Open the file and read its contents
    with open("books/frankenstein.txt", "r") as f:
        file_contents = f.read()
    return file_contents

def count_words(input_string):
    # Split the string on whitespace and count the words
    words = input_string.split()
    word_count = len(words)
    return word_count

def count_letters(input_string):
    # Convert the string to lowercase
    lower_string = input_string.lower()
    # Filter out non-alphabet characters
    filtered_string = ''.join(char for char in lower_string if char.isalpha())
    # Count occurrences of each letter
    letter_counts = Counter(filtered_string)
    # Sort by most common (highest count first)
    sorted_letter_counts = letter_counts.most_common()
    return sorted_letter_counts

if __name__ == "__main__":
    # Read the book's contents
    book_contents = read_book()
    
    # Count the words in the book's contents
    word_count = count_words(book_contents)
    print(f"Word Count: {word_count}")
    
    # Count the letters in the book's contents
    sorted_letter_count = count_letters(book_contents)
    
    # Export results as sentences
    for letter, count in sorted_letter_count:
        print(f"The '{letter}' character was found {count} times.")