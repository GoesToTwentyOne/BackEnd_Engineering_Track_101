class A:
    def __init__(self, a):
        self.x = a
        print("X =", self.x)


class B(A):
    def __init__(self, a, b):
        super().__init__(a)
        self.y = b
        print("Y =", self.y)


class C(B):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.z = c
        print("Z =", self.z)

ob = C(1, 2, 3)
