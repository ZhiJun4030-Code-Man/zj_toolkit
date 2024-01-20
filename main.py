import zj_toolkit
import time
items = list(range(0, 100))
i = 0
l = len(items)
for i in items:

    zj_toolkit.printProgress(i+1,l,"printing","deb",0,50)

    i+=1
    time.sleep(0.1)
time.sleep(0.1)
print("\n")
for i in range(10):
    print(zj_toolkit.hexman(1000,1000))
