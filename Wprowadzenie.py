class A:
    attr1: int
    attr2: int

    def __init__(self, attr1, attr2=20):
        self.attr1 = attr1
        self.attr2 = attr2

    def sum(self) -> int:
        return self.attr1 + self.attr2

    def set_attr1(self, value: int):
        self.attr1 = value

    def __repr__(self):
        return f'attr1: {self.attr1}, attr2: {self.attr2}'

    def __len__(self):
        return self.sum()

obj1 = A(attr1=5)
obj2 = A(attr2=8, attr1=2)

print(obj1)
print(obj2)

print(len(obj1))
print(len(obj2))

obj_test = A(attr1=4)

assert obj_test.attr2 == 20