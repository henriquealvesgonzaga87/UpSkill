lista = ["apple", "banana", "cherry"]
x = lista.pop(0)
print(x,lista)



b = "Hello, World!"
print(b[:5])
print(b[7:12])

def X (n):
  if n == 1 or n == 2:
    return n;
  else:
    return X (n-1) + n * X (n-2);

print(X(4))