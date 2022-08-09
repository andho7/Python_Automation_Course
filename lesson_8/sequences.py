"""
- sequences:
  * підрахунок елементу у послідовності (count(element));
  * рандомний список довжиною N, з елементами у діапазоні a-b (random(N, a, b));
  * сортування бульбашкою (bubble(N, i, j));
  * quicksort (quick(N, i, j));
  * статистика літер та слов у реченні (letter_stats(seq, letter), word_stats(seq, word));
  * лінейний пошук (linear_search(seq, element));
  * бінарний пошук (binary_search(seq, element));
"""
import random


def count(seq, element):
    # search for character in the string and count matches:
    matches = 0
    for j in seq:
        if j == element:
            matches += 1
    return matches


def random_list(N, a, b):
    # generate the list
    generated_list = []
    for i in range(N):
        generated_list.append(random.randint(a, b))
    return generated_list


def bubble(N):
    elements = len(N)
    swap = False
    for i in range(elements - 1):
        for j in range(0, elements - i - 1):
            if N[j] > N[j + 1]:
                swap = True
                N[j], N[j + 1] = N[j + 1], N[j]
        if not swap:
            return N
    return N


def quick(N, i, j):
    quicksort(N, i, j)
    return N


def partition(seq, left_idx, right_idx):
    pivot = left_idx
    for i in range(left_idx+1, right_idx+1):
        if seq[i] < seq[left_idx]:
            pivot += 1
            seq[i], seq[pivot] = seq[pivot], seq[i]
    seq[left_idx], seq[pivot] = seq[pivot], seq[left_idx]
    return pivot


def quicksort(seq, left_idx, right_idx):
    if left_idx >= right_idx:
        return
    pivot = partition(seq, left_idx, right_idx)
    quicksort(seq, left_idx, pivot-1)
    quicksort(seq, pivot+1, right_idx)


def letter_stats(seq, letter):
    matches = 0
    for i in seq:
        if i == letter:
            matches += 1
    return matches


def word_stats(seq, word):
    # cleanup non-letters
    for letter in seq:
        if not letter.isalpha() and letter != ' ':
            user_input = seq.replace(letter, '')
    words_list = seq.split()
    matches = 0
    for i in words_list:
        if i == word:
            matches += 1
    return matches


def linear_search(seq, element):
    for i, v in enumerate(seq):
        if v == element:
            return i


def binary_search(seq, element):
    low = 0
    high = len(seq) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if seq[mid] < element:
            low = mid + 1
        elif seq[mid] > element:
            high = mid - 1
        else:
            return mid
    return -1
