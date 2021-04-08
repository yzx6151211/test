import random
import math
RandomCode = ""
for i in range(0,32):
    t = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    RandomCode = RandomCode+str(t[math.floor(36*random.random())])
print(RandomCode)
RandomCode = str.lower(RandomCode)[0:8]+"-"+str.lower(RandomCode)[8:12]+"-"+str.lower(RandomCode)[12:16]+"-"+str.lower(RandomCode)[16:20]+"-"+str.lower(RandomCode)[20:32]
print(RandomCode)