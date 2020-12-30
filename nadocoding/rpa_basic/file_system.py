import os

# 경로 이동
print(os.getcwd())
os.chdir("nadocoding")
print(os.getcwd())
os.chdir("..")
print(os.getcwd())
os.chdir("../..")
print(os.getcwd())
os.chdir("c:/")
print(os.getcwd())

os.chdir("E:\\Development\\Python")

# 경로
file_path = os.path.join(os.getcwd(), "myfile.txt")
print(file_path)