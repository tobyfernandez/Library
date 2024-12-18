import math
import string
from collections import defaultdict

def create_table(headers: list, data: list[list] | list[dict]):
    """Creates a list of strings that make up a table of values and their corresponding headers
    where data is either a list of lists or a list of dictionaries"""
    if all(isinstance(row, list) for row in data):
        data_type = 'list'
    elif all(isinstance(row, dict) for row in data):
        data_type = 'dict'
    else:
        raise ValueError("Data must be list of lists or list of dicts")

    col_info = {header: {'max_width': len(header), 'align': 'left'} for header in headers}

    if data_type == 'list':
        for row in data:
            for i, value in enumerate(row):
                str_value = str(value) if value is not None else ""  # For determining length
                if isinstance(value, str):
                    col_info[headers[i]]['align'] = 'left'
                elif isinstance(value, int) and not isinstance(value, bool):  # Necessary since bool is subtype of int
                    col_info[headers[i]]['align'] = 'right'
                elif isinstance(value, float):
                    col_info[headers[i]]['align'] = 'right'
                    str_value = f"{value:.2f}"
                elif isinstance(value, bool):
                    col_info[headers[i]]['align'] = 'center'
                col_info[headers[i]]['max_width'] = max(col_info[headers[i]]['max_width'], len(str_value))
    elif data_type == 'dict':
        for row in data:
            for key, value in row.items():
                str_value = str(value) if value is not None else ""  # For determining length
                if isinstance(value, str):
                    col_info[key]['align'] = 'left'
                elif isinstance(value, int) and not isinstance(value, bool):  # Necessary since bool is subtype of int
                    col_info[key]['align'] = 'right'
                elif isinstance(value, float):
                    col_info[key]['align'] = 'right'
                    str_value = f"{value:.2f}"
                elif isinstance(value, bool):
                    col_info[key]['align'] = 'center'
                col_info[key]['max_width'] = max(col_info[key]['max_width'], len(str_value))

    table_list = []

    header_str = '| ' + ' | '.join(
        f"{header.center(col_info[header]['max_width']) if col_info[header]['align'] == 'center' \
            else header.rjust(col_info[header]['max_width']) if col_info[header]['align'] == 'right' \
            else header.ljust(col_info[header]['max_width'])}"
        for header in headers) + ' |'
    separator_str = '| ' + ' | '.join(f"{'-' * col_info[header]['max_width']}" for header in headers) + ' |'

    table_list.append(header_str)
    table_list.append(separator_str)

    if data_type == 'list':
        for row in data:
            row_str = '| ' + ' | '.join(
                f"{str(value).center(col_info[headers[i]]['max_width']) if col_info[headers[i]]['align'] == 'center' \
                    else str(value).rjust(col_info[headers[i]]['max_width']) if col_info[headers[i]]['align'] == 'right' \
                    else str(value).ljust(col_info[headers[i]]['max_width'])}"
                for i, value in enumerate(row)) + ' |'
            table_list.append(row_str)
    elif data_type == 'dict':
        for row in data:
            row_str = '| ' + ' | '.join(
                f"{str(row.get(header, '')).center(col_info[header]['max_width']) if col_info[header]['align'] == 'center' \
                    else str(row.get(header, '')).rjust(col_info[header]['max_width']) if col_info[header]['align'] == 'right' \
                    else str(row.get(header, '')).ljust(col_info[header]['max_width'])}"
                for header in headers) + ' |'
            table_list.append(row_str)

    return '\n'.join(table_list)


def caesar_cipher(plaintext: str, rotation: int = 13) -> str:
    """Takes the plaintext and encrypts it by rotating the standard Latin alphabet by the specified amount.
    Returns the resulting encrypted string."""
    alphabet = string.ascii_lowercase  # Standard lowercase alphabet
    upper = string.ascii_uppercase  # Standard uppercase alphabet
    cipherbet = alphabet[rotation:] + alphabet[:rotation]  # The shifted alphabet
    cipherbet_upper = upper[rotation:] + upper[:rotation]  # An uppercase version of the shifted alphabet
    encryption = ''
    for character in plaintext:
        if character in alphabet or character in upper:
            if character.islower():  # Looks for lowercase letters to encrypt
                index = alphabet.index(character)
                encryption = encryption + cipherbet[index]
            else:  # Looks for uppercase letters to encrypt
                index = upper.index(character)
                encryption = encryption + cipherbet_upper[index]
        else:  # Preserves all non-letter characters
            encryption = encryption + character
    return encryption

def merge(left: list, right: list, reverse=False) -> list:
    """Merges two sorted lists into a single list, reversing the order if needed"""
    merged = []
    lindex = 0
    rindex = 0
    while lindex < len(left) and rindex < len(right):
        if (left[lindex] <= right[rindex] and not reverse) \
                or (left[lindex] >= right[rindex] and reverse):
            merged.append(left[lindex])
            lindex += 1
        else:
            merged.append(right[rindex])
            rindex += 1
    merged.extend(left[lindex:])
    merged.extend(right[rindex:])
    return merged

def merge_sort(data: list, reverse=False) -> list:
    """Splits a list into halves to sort, using merge to split the
    resulting sorted halves. Returns a single sorted list."""
    if len(data) <= 1: return data

    split_list = lambda lst: (lst[:len(lst) // 2], lst[len(lst) // 2:])
    listx, listy = split_list(data)

    lhalf = merge_sort(listx, reverse)
    rhalf = merge_sort(listy, reverse)

    return merge(lhalf, rhalf, reverse)

def calculate_idf(sentences: list[list[str]]) -> dict[str, float]:
    """Calculate the Inverse Document (Sentence) Frequency of each term.
    Returns a table of terms and their idf values."""
    matrix = defaultdict(float)
    num_sentences = len(sentences)
    for sentence in sentences:
        terms_checked = set()
        for term in sentence:
            if term not in terms_checked:
                matrix[term] += 1  # Indicates that the term has been found in another sentence
                terms_checked.add(term)  # Ensures the term is counted only once per sentence
    for term in matrix:
        matrix[term] = math.log(num_sentences / float(matrix[term]))  # Calculates IDF
    return matrix

def bubble_sort(data: list, reverse=False) -> list:
    """Compares each adjacent pair of elements in a list and swaps
    when out of order, repeating until returning a sorted list"""
    length = len(data)
    for loop in range(length):
        for pair in range(0, length - loop - 1):
            if (not reverse and data[pair] > data[pair+1]) or (reverse and data[pair] < data[pair+1]):
                data[pair], data[pair+1] = data[pair+1], data[pair]
    return data