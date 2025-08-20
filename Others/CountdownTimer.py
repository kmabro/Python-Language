import time

mt = int(input("Enter the time in seconds: "))

for x in range(mt , 0, -1):
    s = x%60
    m = int(x/60)%60
    h = int((x/3600))
    print(f"{h:02}:{m:02}:{s:02}")
    time.sleep(1)

print("TIME'S UP!")