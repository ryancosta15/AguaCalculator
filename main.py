#how much water should i drink
from time import sleep
print("Let's see how much water you should drink in a day")
sleep (3)
weight = float(input('What is your weight? (use dots "." instead of commas "," ) '))
water = round((weight * 0.035), 3)
waterstr = str(water)
wtrlenp1 =  int(len(waterstr) + 1)
print("If you weight is {} you should drink...".format(weight))
sleep(2)
print("Calculating...")
sleep(1)
print ("-" * wtrlenp1)
print(waterstr + "L")
print ("-" * wtrlenp1)