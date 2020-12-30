print("Hellow World")

# print(5)
# print(-10)
# print(3.14)
# print(1000)
# print(5+8)
# print(2*3)
# print(10/1)
# print(2**3)
# print(5%3)
# print(10%3)
# print(10//3)

# print("풍선")
# print("=="*10)

# print(5>10)
# print(5<10)
# print(5>=10)
# print(5<=10)
# print(10 == 10)
# print(10 != 10)
# print(True)
# print(False)

# animal = "강아지"
# name = ["연탄이","아이고"]
# age = 4
# key = 12.26
# sex = True

# print(type(animal))
# print(type(name))
# print(type(age))
# print(type(key))
# print(type(sex))


# from random import *
# print(random())
# print(random() * 10)
# print(int(random() * 10))

# print(randrange(100, 146))

# print("a"+ "b")
# print("a","b")

# print("나는 %d살 입니다." %20)
# print("나는 %s을 좋아해요." %"파이썬")
# print("Apple은 %c로 시작 합니다." %"A")

# print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# print("나는 {}을 좋아해요.".format("파이썬"))
# print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
# print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))
# print("나는 {age}살이며 {color}색을 좋아해요.".format(age=20, color="빨간"))

# age=20
# color="빨간"
# print(f"나는 {age}살이며 {color}색을 좋아해요.")

# print("백문이 불여일견 \n백견이 불여일타")
# print("저는 '개발자' 압니다.")
# print("저는 \"개발자\" 압니다.")

#####  <class 'list'>  #################
# subway = [10,20,30]
# print(subway)

# subway = ["유재석","조세호","박명수"]
# print(subway)
# print(type(subway))

# subway.append("하하")
# print(subway)

# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

#####  <class 'dict'>  #################
# cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet)
# print(type(cabinet))

# print(cabinet[3])
# print(cabinet.get(3))
# # print(cabinet[5])
# print(cabinet.get(5))
# print(cabinet.get(5, "사용가능"))

#####  <class 'tuple'>  #################
# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])

# print(type(menu))

# (name, age) = "김종국", 23
# print(name, age)

# print(type(name))           # str
# print(type((name, age)))    # tuple

#####  <class 'set'>  #################
# my_set = {1,2,3,4,5}
# print(my_set)
# print(type(my_set))

# jave = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])

# print(jave & python)
# print(jave.intersection(python))

# print(jave | python)
# print(jave.union(python))

# print(jave - python)
# print(jave.difference(python))

#####  자료구조 변경  #################
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = dict(menu)
# print(menu, type(menu))


#####  퀴즈  #################
# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst, 1))


#####  함수  #################
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# open_account()

# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance+money))
#     return balance + money

# balance = 0
# balance = deposit(balance, 1000)
# print(balance)

# def profile(name, age, *language):
#     print("이름:{0} 나이:{1}".format(name, age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()

# profile("유재석", 23, "Python", "Java", "C", "C++", "C#")
# profile("김태호", 27, "Kotlin", "Swift")

#####  파일 IO  #################
# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n")
# score_file.write("코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines()
# for line in lines:
#     print(line, end="")
# score_file.close()

#####  pickle  #################
# import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프"]}
# print(profile)
# pickle.dump(profile, profile_file)
# profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close()

#####  with  #################
# import pickle
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부 하고 있습니다.")

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())

#####  tyr  ###################
# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg
#     def __str__(self):
#         return self.msg    

# try:
#     print("나누기 전용 계산기 입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요. : "))
#     num2 = int(input("두 번째 숫자를 입력하세요. : "))

#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))        # 사용자 정의 Err

#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
# except Exception as ex:
#     print(ex)
# finally:
#     print("계산기를 이용해 주셔서 감사합니다.")    

#####  module  ###################
# import pymodule
# print(pymodule.SYS_NAME)
# print(pymodule.SYS_NUM)
# pymodule.price(2)
# pymodule.price_morning(5)
# pymodule.price_soldier(7)

# import pymodule as mod
# print(mod.SYS_NAME)
# print(mod.SYS_NUM)
# mod.price(2)
# mod.price_morning(4)
# mod.price_soldier(9)

# from pymodule import *
# print(SYS_NAME)
# print(SYS_NUM)
# price(3)
# price_morning(6)
# price_soldier(4)

# from pymodule import SYS_NAME, price, price_morning
# print(SYS_NAME)
# price(2)
# price_morning(2)

# from pymodule import price_soldier as price
# price(4)


#####  package  ###################
# import pypackage.thailand
# trip_to = pypackage.thailand.ThailandPackage()
# trip_to.detail()

# from pypackage.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from pypackage.vietnam import VietnamPackage
# trip_to = VietnamPackage()
# trip_to.detail()

#from pypackage import *
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# trip_to1 = thailand.ThailandPackage()
# trip_to1.detail()

#####  package 위치 찾기 ###################
import inspect
import random
import pypackage
print(inspect.getfile(random))      # C:\Program Files\Python39\lib\random.py
print(inspect.getfile(pypackage))   # e:\Development\Python\nadocoding\pypackage\__init__.py

# package 이동
print(inspect.getfile(random))      # C:\Program Files\Python39\lib\random.py
print(inspect.getfile(pypackage))   # C:\Program Files\Python39\lib\pypackage\__init__.py