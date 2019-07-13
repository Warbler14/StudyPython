strData = "Hello World"

print(strData[0])
print(strData[-1])
print(strData[1:2])
print(strData[0:])
print(strData[1:])
print(strData[:3])

testStr1 = "abcdefgh"

print(testStr1[::2])
print(testStr1[::2] * 3)
print(len(testStr1))

splitStringData = strData.split(" ")
print(splitStringData)

print("abc" in testStr1)
print("--------------------------------")
L = [1, 2, 3]
print(len(L))
print(L + L)

L.append(4)
print(L)
del L[0]
print(L)

L.reverse()
print(L)
L.sort()
print(L)

print(3 in L)

print("--------------------------------")
T = (1, 2, 3)
print(len(T))
print(T[0])
print(T[0:2])
print(T[::2])

print(T * 2)
print(T + T)
print(1 in T[1:2] + T[0:1])

TL = list(T)
print(TL)
LT = tuple(L)
print(LT)

print("--------------------------------")
TT = ((1, 2, 3), [4, 5, 6])
print(TT)
TTL = list(TT)
print(TTL)

LL = [[1, 2, 3], (4, 5, 6)]
print(LL)
LLT = tuple(LL)
print(LLT)

print("--------------------------------")
D = {"one": 1, "two": 2, "three": 3}
print(D)
print(D.get("one"))
print(D["one"])
print(D.keys())
print(D.values())
print(D.items())

print(list(D.keys()))
print(list(D.values()))
print(list(D.items()))

