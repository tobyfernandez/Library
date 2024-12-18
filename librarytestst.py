from library import create_table, caesar_cipher, merge, merge_sort, calculate_idf, bubble_sort

def test_bubble_sort():
    assert bubble_sort([5, 3, 8, 6, 2]) == [2, 3, 5, 6, 8]
    assert bubble_sort([5, 3, 8, 6, 2], reverse=True) == [8, 6, 5, 3, 2]
    assert bubble_sort([]) == []
    assert bubble_sort([1]) == [1]
    assert bubble_sort([5, 1, 5, 1]) == [1, 1, 5, 5]
    print("bubble_sort passed the tests")

def test_caesar_cipher():
    assert caesar_cipher('Hello', 13) == 'Uryyb'
    assert caesar_cipher('HELLO...', 3) == 'KHOOR...'
    assert caesar_cipher('HELLO, WORLD!?>*', 3) == 'KHOOR, ZRUOG!?>*'
    assert caesar_cipher('', 3) == ''
    assert caesar_cipher('HELLO', 26) == 'HELLO'
    print("caesar_cipher passed the tests")

def test_merge():
    assert merge([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge([5, 3, 1], [6, 4, 2], reverse=True) == [6, 5, 4, 3, 2, 1]
    assert merge([], []) == []
    print("merge passed the tests")

def test_merge_sort():
    assert merge_sort([3, 1, 4, 1, 5, 9, 2]) == [1, 1, 2, 3, 4, 5, 9]
    assert merge_sort([3, 1, 4, 1, 5, 9, 2], reverse=True) == [9, 5, 4, 3, 2, 1, 1]
    assert merge_sort([]) == []
    print("merge_sort passed the tests")

def test_calculate_idf():
    # Basic test with multiple terms
    sentences = [['tea', 'coffee'], ['water', 'tea'], ['coffee', 'water', 'tea']]
    expected_output = {'tea': 0.0, 'coffee': 0.4054651081081644, 'water': 0.4054651081081644}
    assert calculate_idf(sentences) == expected_output

    # Test with empty input
    assert calculate_idf([]) == {}

    # Test with all terms in a single sentence
    sentences = [['tea', 'coffee', 'water']]
    expected_output = {'tea': 0.0, 'coffee': 0.0, 'water': 0.0}
    assert calculate_idf(sentences) == expected_output

    # Test with duplicate terms
    sentences = [['tea', 'tea', 'water'], ['coffee', 'coffee', 'water'], ['tea', 'coffee', 'water']]
    expected_output = {'tea': 0.4054651081081644, 'water': 0.0, 'coffee': 0.4054651081081644}
    assert calculate_idf(sentences) == expected_output

    print("calculate_idf passed the tests")

test_calculate_idf()
test_merge()
test_merge_sort()
test_bubble_sort()
test_caesar_cipher()




