import time
import random
print("じんざいルーレット")
input("Enterを押してね")
a=random.randint(1,100)
if 1<=a<=10:
  ans="人罪"
elif 11<=a<=30:
  ans="人在"
elif 31<=a<=90:
  ans="人材"
else:
  ans="人財"
time.sleep(1.0)
print("結果は「"+ans+"」だよ")
