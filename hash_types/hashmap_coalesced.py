def hash_mod(n, m):
    return n % m


class Hashmap:

    def __init__(self, n, r):

        self.liste = [None] * int(n + n * r)
        self.size = n
        self.cursor = int(n + n * r) - 1

    def insert(self, e, f, n=11):
        h = f(e, n)
        if self.liste[h] is None:
            self.liste[h] = Element(e, f, n)
            return h
        else:
            if self.cursor > self.size - 1:
                el = self.liste[h]
                while el.next is not None:
                    el = el.next

                self.liste[self.cursor] = el.next = Element(e, f, n)
                self.cursor -= 1

                return self.cursor
            else:
                return None

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

    hm = Hashmap(11, 0.8)
    print("Cursor: ", hm.cursor)

    lst = [10, 22, 31, 4, 15, 28, 83, 88, 59, 37]

    for e in lst:
        print("insert: ", e, "at", hm.insert(e, hash_mod, 11))

    print(hm)
