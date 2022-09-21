# tallies = {
#     'I': 1,
#     'V': 5,
#     'X': 10,
#     'L': 50,
#     'C': 100,
#     'D': 500,
#     'M': 1000,
# }
# a = 'XYM'
# print(tallies[a[-1]])
# for i in range(len(a)-2,-1,-1):
#     print(i)
# d = ['Kunal','Gobinda','Kakali']
# print(type(d))

# a = lambda x: x*x
# print(a(2))
###form image 
# import cv2
# face = cv2.CascadeClassifier(r"C:\Users\UDCIND\OneDrive - UDC\Smaple_Program_ML\.xml")
# img = cv2.imread(r"C:\Users\UDCIND\OneDrive - UDC\Smaple_Program_ML\istockphoto-1368965646-170667a.jpg")
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# faces = face.detectMultiScale(gray,1.1,4)
# for (x, y, w, h) in faces: 
#     cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
# cv2.imshow('img',img)
# cv2.waitKey()
# cv2.imwrite("face_detected.png", img) 
# print('Successfully saved')
# def clean(text):
#     try:
#         import re
#         import string
#         from nltk.corpus import stopwords
#         from nltk.tokenize import word_tokenize
#         stopword=set(stopwords.words('english'))
#         text = re.sub('\[.*?\]', '', text)
#         text = re.sub('https?://\S+|www\.\S+', '', text)
#         text = re.sub('<.*?>+', '', text)
#         text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
#         text = re.sub('\n', '', text)
#         text = re.sub('\w*\d\w*', '', text)
#         result = [word + " " for word in word_tokenize(text) if word not in stopword]
#         result = " ".join(result)
#         return result
#     except Exception:
#         return Exception
# print(clean("The quick brown fox jumps over the lazy dog"))
# print(type("https://hackernoon.com/future-of-python-language-bright-or-dull-uv41u3xwx"))


# class Car:
#     def __init__(self,type_car,power,capacity,price):
#         self.Car_Type = type_car
#         self.Car_power = power
#         self._price = price
#         self.Car_Capacity = capacity
        
#     def name_car(self,name):
#         return f"Car Name is {name} & Type of Car is {self.Car_Type}"
    
#     @property
#     def price_ip(self):
#         return self._price
#     @price_ip.setter
#     def price_ip(self,new_price):
#         self._price = max(new_price,0)


# fortuna = Car("4 Wheelear", "Electric", 4000, -25)
# fortuna.price_ip = -32
# print(fortuna._price)

# def fibonaci(n):
#     try:
#         if n == 0:
#             return 0
#         if n == 1:
#             return 1
#         else:
#             return fibonaci(n-1) + fibonaci(n-2)
#     except Exception as ex:
#         return ex
# n = 5
# for i in range(0,n+1):
#     print(fibonaci(i), end=" ")


# def sum_ddd(n,target,s1,d1,d2):
#     if n == len(s1):
#         if target == 0:
#             d1.append(d2.copy())
#         return
#     if n <= target:
#         d2.append(s1[n])
#         sum_ddd(n,target-s1[n],s1,d1,d2)
#         d2.remove(s1[n])
#     sum_ddd(n+1,target,s1,d1,d2)
#     return d1

# print(sum_ddd(0,2,s1=[1,2,1],d1=[[]],d2=[]))


def tower_of_hanoi(number,source,destanation,intermediate):
    if number == 1:
        print(f"Move Disk {number} from {source} to {destanation}")
        return
    tower_of_hanoi(number - 1,source,intermediate,destanation)
    print(f"Move Disk {number} from {source} to {destanation}")
    tower_of_hanoi(number - 1,intermediate,destanation,source)

tower_of_hanoi(2,'A','C','B')
