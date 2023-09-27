def find_it(seq):
    for number in seq:
        if seq.count(number) % 2 != 0:
            return number
