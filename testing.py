def count_symbols(string: str) -> str:
    counting = {}
    for char in string:
        if char in counting:
            counting[char] += 1
        else:
            counting[char] = 1
    return counting


if __name__ == '__main__':
    s = "abracadabra"
    print(count_symbols(s))
