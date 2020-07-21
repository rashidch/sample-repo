import time


def sum_of_n_2(n):

    start = time.time()
    the_sum = 0
    for i in range(1, n + 1):

        the_sum += i

    end = time.time()

    return the_sum, end - start


def sum_of_n_3(n):
    start = time.time()

    sum3 = (n * (n + 1)) / 2

    end = time.time()

    return sum3, end - start


def anagram_solution4(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord("a")
        c1[pos] = c1[pos] + 1
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord("a")
        c2[pos] = c2[pos] + 1
    j = 0
    still_ok = True
    while j < 26 and still_ok:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            still_ok = False
    return still_ok


if __name__ == "__main__":

    for i in range(5):
        print("Sum is %d required %10.7f seconds" % sum_of_n_2(1000000))

    print("------------------------------------------------------------")
    for i in range(5):
        print("Sum3 is %d required %10.15f seconds" % sum_of_n_3(100000000))

    print(anagram_solution4("apple", "pleap"))

