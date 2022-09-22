class demo():
    a = 5
    def demo1(N):
        N = 10
        return N

abc = demo.a

print(abc)

abc = demo.demo1(abc)

print(abc)

