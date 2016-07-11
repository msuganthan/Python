if 9<10:
    print("true")
if 9<=10:
    print("true")
if 9>10:
    print("false")
if 9>=10:
    print("false")
if 9==10:
    print("false")
if 9!=10:
    print("true")

if 9<10 and 9!=10:
    print("true")
if 9<10 or 9!=10:
    print("true")

string = "abcde"
if 'a' in string:
    print("a is in string")

a = [1, 3, 4]
b = [1, 3, 4]

if a is b:
    print("a is b")
else:
    print("a is not b")

c = d = [1, 2, 3]

if c is d:
    print("c is d")
