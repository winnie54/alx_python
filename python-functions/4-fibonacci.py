#!/usr/bin/python3
def fibonacci_sequence(n):
    sequence = []
    if n <= 0:
        return sequence
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
        return sequence 