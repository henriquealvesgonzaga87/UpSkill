i=0
for c in range(32, 127):
   i = (i+1) % 70
   if i==0:
       print()
   print("{:c}".format(c), end='')

print()
for c in range(0x1F600, 0x1F607):
    print("{:c}".format(c))

i = 0
for c in range(0x1F1FF,0x1F600):
   i = (i+1) % 70
   if i==0:
       print()
   print("{:c}".format(c), end='')

i = 0
for c in range(1, 20000):
    i = (i+1) % 70
    if i==0:
       print()
    try:
        print("{:c}".format(c), end='')
    except:
        pass


