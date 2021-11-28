def mean(x: list):
    res = sum(x) / len(x)
    return res


lister = [1, 2, 3, 4, 5]

if __name__ == '__main__':
    print(mean(lister))
