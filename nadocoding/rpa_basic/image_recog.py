import os
import sys
import time
import pyautogui

# 이미지 위치 정보
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")

# 단일 이미지 선택 (화면전체 검색)
# file_name = pyautogui.locateOnScreen(os.path.join(image_path, "user.png"))  # Box(left=1837, top=112, width=41, height=38)
# print(file_name)
# pyautogui.click(file_name)

# screen = pyautogui.locateOnScreen(os.path.join(image_path, "all.png"))  # Box(left=1837, top=112, width=41, height=38)
# print(screen)
# pyautogui.click(screen)

# 다중 이미지 선택 (화면전체 검색)
# for check in pyautogui.locateAllOnScreen(os.path.join(image_path, "checkbox.png")):
#     print(check)
#     pyautogui.click(check)


# 1.이미지 검색 속도 개선 (흑백 화면 검색)
# file_name = pyautogui.locateOnScreen(os.path.join(image_path, "user.png"))
# print(file_name)
# pyautogui.click(file_name)

# file_name = pyautogui.locateOnScreen(os.path.join(image_path, "user.png"), grayscale=True)
# print(file_name)
# pyautogui.click(file_name)

# 2.이미지 검색 속도 개선 (부분 화면 검색)
# file_name = pyautogui.locateOnScreen(os.path.join(image_path, "user.png"), region=(1675, 80, 1890-1675, 173-80))
# print(file_name)
# pyautogui.click(file_name)

# 3.이미지 검색 속도 개선 (화면 정확도 검색)
# pip install opencv-python
# file_name = pyautogui.locateOnScreen(os.path.join(image_path, "user.png"), confidence=0.9)
# print(file_name)
# pyautogui.click(file_name)


# 자동화 대상이 화면에 없는 경우 (계속 기다리기)
# file_note = pyautogui.locateOnScreen(os.path.join(image_path, "file.png"))

# while file_note is None:
#     file_note = pyautogui.locateOnScreen(os.path.join(image_path, "file.png"))
#     print("발견 실패")

# pyautogui.click(file_note)


# 자동화 대상이 화면에 없는 경우 (일정시간 기다리기)
# timeout = 20
# start = time.time()
# file_note = None
# while file_note is None:
#     file_note = pyautogui.locateOnScreen(os.path.join(image_path, "file.png"))
#     print("검색중")
#     end = time.time()

#     if end - start > timeout:
#         print("시간종료")
#         sys.exit()

# pyautogui.click(file_note)

