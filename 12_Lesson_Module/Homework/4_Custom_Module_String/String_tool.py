'''
This module provides a function to reverse a given string.
The function takes a string as input and returns the reversed version of that string.
Example usage:
    reversed_text = reverse_string("Hello, World!")
    print(reversed_text)  # Output: !dlroW ,olleH
'''
import random   
import string

#reverses a string by prepending each character to the growing reversed string
def reverse_string(text):
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text

#counts the number of words in a string
def count_words(text):
    words = text.split()
    return len(words)

#checks if a string is a palindrome (ignoring spaces and case)
def is_palindrome(text):
    cleaned_text = text.replace(" ", "").lower()
    return cleaned_text == reverse_string(cleaned_text)

#capitalizes the first letter of each word in a string
def capitalize_words(text): 
    words = text.split()
    capitalized_words = [word.capitalize() for word in words]
    return " ".join(capitalized_words)

#removes all vowels from a string
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return "".join(char for char in text if char not in vowels)

#replaces all occurrences of a substring with another substring
def replace_substring(text, old, new):
    return text.replace(old, new)

#checks if a string contains only digits
def is_numeric(text):   
    return text.isdigit()

#checks if a string contains only alphabetic characters
def is_alpha(text):
    return text.isalpha()

#checks if a string contains only alphanumeric characters
def is_alphanumeric(text):
    return text.isalnum()

#converts a string to uppercase
def to_uppercase(text):
    return text.upper()

#converts a string to lowercase
def to_lowercase(text):
    return text.lower()

#trims leading and trailing whitespace from a string
def trim_whitespace(text):
    return text.strip()

#count vowels in a string
def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

#count consonants in a string
def count_consonants(text): 
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char.isalpha() and char not in vowels)

#find the most common character in a string
def most_common_character(text):
    char_count = {}
    for char in text:
        if char.isalpha():  # Consider only alphabetic characters
            char = char.lower()  # Convert to lowercase for case-insensitivity
            char_count[char] = char_count.get(char, 0) + 1
    if not char_count:
        return None  # Return None if there are no alphabetic characters
    most_common = max(char_count, key=char_count.get)
    return most_common, char_count[most_common]

#find the least common character in a string
def least_common_character(text):
    char_count = {}
    for char in text:
        if char.isalpha():  # Consider only alphabetic characters
            char = char.lower()  # Convert to lowercase for case-insensitivity
            char_count[char] = char_count.get(char, 0) + 1
    if not char_count:
        return None  # Return None if there are no alphabetic characters
    least_common = min(char_count, key=char_count.get)
    return least_common, char_count[least_common]

#find the longest word in a string
def longest_word(text):
    words = text.split()
    if not words:
        return None  # Return None if there are no words
    longest = max(words, key=len)
    return longest, len(longest)

#find the shortest word in a string
def shortest_word(text):    
    words = text.split()
    if not words:
        return None  # Return None if there are no words
    shortest = min(words, key=len)
    return shortest, len(shortest)

#count the number of sentences in a string (assuming sentences end with '.', '!', or '?')
def count_sentences(text):  
    sentences = text.split('.')
    sentences = [s for s in sentences if s.strip()]  # Remove empty sentences
    return len(sentences)

#count the number of paragraphs in a string (assuming paragraphs are separated by two newlines)
def count_paragraphs(text): 
    paragraphs = text.split('\n\n')
    paragraphs = [p for p in paragraphs if p.strip()]  # Remove empty paragraphs
    return len(paragraphs)  

#count the number of lines in a string
def count_lines(text):
    lines = text.split('\n')
    lines = [l for l in lines if l.strip()]  # Remove empty lines
    return len(lines)

#count the number of characters in a string (excluding spaces)
def count_characters(text):
    return len(text.replace(" ", ""))

#count the number of unique characters in a string
def count_unique_characters(text):
    unique_characters = set(text.replace(" ", ""))
    return len(unique_characters)

#count the number of repeated characters in a string
def count_repeated_characters(text):
    char_count = {}
    for char in text:
        if char.isalpha():  # Consider only alphabetic characters
            char = char.lower()  # Convert to lowercase for case-insensitivity
            char_count[char] = char_count.get(char, 0) + 1
    repeated_characters = {char: count for char, count in char_count.items() if count > 1}
    return repeated_characters

#count the number of non-alphanumeric characters in a string
def count_non_alphanumeric_characters(text):
    return sum(1 for char in text if not char.isalnum() and not char.isspace())

#count the number of uppercase characters in a string
def count_uppercase_characters(text):
    return sum(1 for char in text if char.isupper())    

#count the number of lowercase characters in a string
def count_lowercase_characters(text):
    return sum(1 for char in text if char.islower())

#count the number of whitespace characters in a string
def count_whitespace_characters(text):
    return sum(1 for char in text if char.isspace())

#count the number of punctuation characters in a string
def count_punctuation_characters(text):
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    return sum(1 for char in text if char in punctuation)

#count the number of any specific character in a string
def count_specific_character(text, character):
    return text.count(character)

#generate a random string of a given length
def generate_random_string(length):
    letters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(letters) for i in range(length))

#generate a default string of a given length (using 'x' as the default character)
def generate_default_string(length):
    return 'x' * length

#generate a default string for the user (using a specified character as the default)
def generate_user_default_string(length, character):
    return character * length

#generate a default sentence of a given length (using 'Lorem ipsum' as the default sentence)
def generate_default_sentence(length):
    default_sentence = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    return (default_sentence * (length // len(default_sentence) + 1))[:length]

#generate a default paragraph of a given length (using 'Lorem ipsum' as the default paragraph)
def generate_default_paragraph(length):
    default_paragraph = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
    return (default_paragraph * (length // len(default_paragraph) + 1))[:length]

#generate a default text of a given length (using 'Lorem ipsum' as the default text)
def generate_default_text(length):
    default_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
    return (default_text * (length // len(default_text) + 1))[:length]

#convert a string to title case (capitalizing the first letter of each word)
def to_title_case(text):
    return text.title()

#convert a string to sentence case (capitalizing the first letter of the first word and making the rest lowercase)
def to_sentence_case(text):
    if not text:
        return ""
    return text[0].upper() + text[1:].lower()

#convert a string to camel case (removing spaces and capitalizing the first letter of each word except the first one)
def to_camel_case(text):
    words = text.split()
    if not words:
        return ""
    camel_case = words[0].lower() + ''.join(word.capitalize() for word in words[1:])
    return camel_case

#convert a string to snake case (replacing spaces with underscores and making all letters lowercase)
def to_snake_case(text):
    return text.replace(" ", "_").lower()

#convert a string to kebab case (replacing spaces with hyphens and making all letters lowercase)
def to_kebab_case(text):
    return text.replace(" ", "-").lower()   

#convert a string to pascal case (capitalizing the first letter of each word and removing spaces)
def to_pascal_case(text):
    words = text.split()
    pascal_case = ''.join(word.capitalize() for word in words)
    return pascal_case

#convert a string to alternating case (capitalizing every other letter)
def to_alternating_case(text):
    alternating_case = ''.join(char.upper() if i % 2 == 0 else char.lower() for i, char in enumerate(text))
    return alternating_case

#convert a string to reverse alternating case (capitalizing every other letter starting with the second letter)
def to_reverse_alternating_case(text):  
    reverse_alternating_case = ''.join(char.upper() if i % 2 != 0 else char.lower() for i, char in enumerate(text))
    return reverse_alternating_case

#convert a string to leetspeak (replacing certain letters with numbers or symbols)
def to_leetspeak(text):
    leetspeak_dict = {
        'A': '4', 'a': '4',
        'E': '3', 'e': '3',
        'I': '1', 'i': '1',
        'O': '0', 'o': '0',
        'S': '5', 's': '5',
        'T': '7', 't': '7'
    }
    leetspeak = ''.join(leetspeak_dict.get(char, char) for char in text)
    return leetspeak

#convert a string into Morse code
def to_morse_code(text):
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        ', ': '--..--', '. ': '.-.-.-', '? ': '..--..', '/ ': '-..-.',
        '- ': '-....-', '( ': '-.--.', ') ': '-.--.-'
    }
    morse_code = ''.join(morse_code_dict.get(char.upper(), char) for char in text)
    return morse_code

#convert a string into binary code
def to_binary_code(text):
    binary_code = ' '.join(format(ord(char), '08b') for char in text)
    return binary_code

#convert a string into hexadecimal code
def to_hexadecimal_code(text):
    hexadecimal_code = ' '.join(format(ord(char), '02x') for char in text)
    return hexadecimal_code

#convert a string into octal code
def to_octal_code(text):    
    octal_code = ' '.join(format(ord(char), '03o') for char in text)
    return octal_code

#convert a string into base64 code
def to_base64_code(text):
    import base64
    base64_code = base64.b64encode(text.encode()).decode()
    return base64_code

#convert a string into URL encoding
def to_url_encoding(text):
    import urllib.parse
    url_encoded = urllib.parse.quote(text)
    return url_encoded

#convert a string into HTML encoding
def to_html_encoding(text):
    import html
    html_encoded = html.escape(text)
    return html_encoded

#convert a string into a list of characters
def to_character_list(text):
    return list(text)

#convert a string into a list of words
def to_word_list(text): 
    return text.split()

#convert a string into a list of sentences (assuming sentences end with '.', '!', or '?')
def to_sentence_list(text):
    import re
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]  # Remove empty sentences and trim whitespace
    return sentences

#convert a string into a dictionary of character counts
def to_character_count_dict(text):
    char_count = {}
    for char in text:
        if char.isalpha():  # Consider only alphabetic characters
            char = char.lower()  # Convert to lowercase for case-insensitivity
            char_count[char] = char_count.get(char, 0) + 1
    return char_count

#convert a string into a dictionary of word counts
def to_word_count_dict(text):
    word_count = {}
    words = text.split()
    for word in words:
        word = word.lower()  # Convert to lowercase for case-insensitivity
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

#convert a string into a set of unique characters
def to_unique_character_set(text):  
    unique_characters = set(text.replace(" ", ""))
    return unique_characters

#convert a string into a set of unique words
def to_unique_word_set(text):   
    unique_words = set(text.split())
    return unique_words

#check Two words similarity using Jaccard similarity
def jaccard_similarity(word1, word2):
    set1 = set(word1.lower())
    set2 = set(word2.lower())
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    if not union:
        return 0.0  # Avoid division by zero
    similarity = len(intersection) / len(union)
    return similarity

#check Two words similarity using Levenshtein distance
def levenshtein_distance(word1, word2):
    if len(word1) < len(word2):
        return levenshtein_distance(word2, word1)
    if len(word2) == 0:
        return len(word1)
    previous_row = range(len(word2) + 1)
    for i, c1 in enumerate(word1):
        current_row = [i + 1]
        for j, c2 in enumerate(word2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    return previous_row[-1]

#check Two words similarity using Cosine similarity
def cosine_similarity(word1, word2):
    from collections import Counter
    import math
    word1_count = Counter(word1.lower())
    word2_count = Counter(word2.lower())
    all_chars = set(word1_count.keys()).union(set(word2_count.keys()))
    dot_product = sum(word1_count[char] * word2_count[char] for char in all_chars)
    magnitude1 = math.sqrt(sum(count ** 2 for count in word1_count.values()))
    magnitude2 = math.sqrt(sum(count ** 2 for count in word2_count.values()))
    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0  # Avoid division by zero
    similarity = dot_product / (magnitude1 * magnitude2)
    return similarity

#check two words by converting each one of them into a list and than counts the number of similar characters in both lists and divides it by the total number of unique characters in both lists
def simple_similarity(word1, word2):
    set1 = set(word1.lower())
    set2 = set(word2.lower())
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    if not union:
        return 0.0  # Avoid division by zero
    similarity = len(intersection) / len(union)
    return similarity

#check two words by converting each one of them into a list and than counts the number of similar characters in both lists and return the similarity as a percentage
def percentage_similarity(word1, word2):
    set1 = set(word1.lower())
    set2 = set(word2.lower())
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    if not union:
        return 0.0  # Avoid division by zero
    similarity = (len(intersection) / len(union)) * 100
    return similarity

#check two sentences similarity by converting each one of them into a list and than counts the number of similar words in both lists and return the similarity as a percentage
def check_similarity(text1, text2):
    # Convert texts to lowercase and split into words
    words1 = text1.lower().split()
    words2 = text2.lower().split()
    # Find the set of common words
    common_words = set(words1) & set(words2)
    # Calculate the union of words
    all_words = set(words1) | set(words2)
    # Calculate similarity percentage using Jaccard similarity
    if len(all_words) == 0:
        similarity_percentage = 0.0
    else:
        similarity_percentage = (len(common_words) / len(all_words)) * 100
    return similarity_percentage

