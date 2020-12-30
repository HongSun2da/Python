import pyautogui

print(pyautogui.size()) #화면크기

# (절대 좌표) 마우스 이동
# pyautogui.moveTo(200, 100)
# pyautogui.moveTo(400, 600, duration=5)  
# pyautogui.moveTo(100, 100, duration=0.5)
# pyautogui.moveTo(200, 200, duration=0.5)
# pyautogui.moveTo(200, 300, duration=0.5)

# (상대 좌표) 마우스 이동
# pyautogui.move(-100, 100, duration=0.5)
# print(pyautogui.position())
# pyautogui.move(-200, 200, duration=0.5)
# print(pyautogui.position())
# pyautogui.move(-200, 300, duration=0.5)
# print(pyautogui.position())

# 좌표 정보
# pyautogui.sleep(3)    # 대기(초)
# p = pyautogui.position()
# print(p[0], p[1])
# print(p.x, p.y)

# pyautogui.click(1973,14)
# pyautogui.click(clicks=3)

# pyautogui.mouseDown()
# pyautogui.mouseUp()
# pyautogui.doubleClick()

# pyautogui.scroll(-200)

# mouseInfo Util
# pyautogui.mouseInfo()

# for i in range(10):
#     pyautogui.move(100, 100)
#     pyautogui.sleep(1)

# 스크린
# img = pyautogui.screenshot()
# img.save("pyautogui_screen.png")