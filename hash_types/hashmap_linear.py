def hash_mod(n, m):
    return n % m


class Hashmap:

    def __init__(self, n):

        self.liste = [None] * n
        self.size = n

    def insert(self, e, f, n=11):
        h = f(e, n)
        if self.liste[h] is None:
            self.liste[h] = Element(e, f, n)
            return h
        else:
            j = 1
            i = (h + j) % self.size
            while self.liste[i] and j < self.size:
                j += 1
                i = (h + j) % self.size

            if j == self.size:
                return None
            else:
                self.liste[i] = Element(e, f, n)

    def __str__(self):

        s = ""
        for i in self.liste[:-1]:
            s += str(i) + ", "

        s += str(self.liste[-1])
        return s


class Element:

    def __init__(self, e, f, n):
        self. e = e
        self.hash = f(e, n)
        self.next = None

    def __str__(self):
        return "Eelemnt[{}, {}, {}]".format(self.e, self.hash, self.next)


if __name__ == "__main__":

    hm = Hashmap(11)

    lst = [10, 22, 31, 4, 15, 28, 83, 88, 59, 37]

    for e in lst:
        print("insert", e, "at", hm.insert(e, hash_mod, 11))

    print(hm)
