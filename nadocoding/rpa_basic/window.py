import pyautogui
import pyperclip


# Window 활성화 찾기
# fw = pyautogui.getActiveWindow()
# print(fw.title)
# print(fw.size)
# print(fw.left, fw.top, fw.right, fw.bottom)

# for w in pyautogui.getAllWindows():
#     print(w)

# w = pyautogui.getWindowsWithTitle("제목 없음")[0]
# print(w.isActive)

# if w.isActive == False:
#     w.activate()

# if w.isMaximized == False:
#     w.maximize()

# pyautogui.sleep(1)

# w.restore()


# 키보드 
w = pyautogui.getWindowsWithTitle("제목 없음")[0]
if w.isActive == False:
    w.activate()

pyautogui.write("12345")
pyautogui.write("NadoCoding", interval=0.25)

# pyautogui.keyDown("shift")
# pyautogui.press("4")
# pyautogui.keyUp("shift")

# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a")
# pyautogui.keyUp("ctrl")

# hot key (연속동작)
# pyautogui.hotkey("ctrl", "a")


# 한글 입력
# pip install pyperclip
pyperclip.copy("나도 코딩")
pyautogui.hotkey("ctrl", "v")

# 자동화 종료
# win : ctrl + alt + del


# 메시지 
# pyautogui.alert("자동화 수행에 실패 했습니다.","경도")

# 사용자 확인
# result = pyautogui.confirm("계속 진행 하시겠습니까?", "확인")
# print(result) # OK, Cancel

# 사용자 입력
result = pyautogui.prompt("파일명을 무엇으로 하시겠습니까?", "입력")
print(result) # 

result = pyautogui.password("비밀번호 입력", "입력")
print(result) # 
