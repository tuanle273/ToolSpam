import pyautogui, pyperclip, random, time
print("Tool Spam")
msg = input("Nhap noi dung spam: ").split(" || ")
n = int(input("Nhap so lan spam: "))
m = float(input("Nhap time delay: "))

print("Loading")
for i in range(5,0,-1):
    print(i,end="...", flush='True')
    print("start")

    for i in range(n):
        pyperclip.copy(random.choice(msg))
        pyautogui.hotkey("ctrl","v")
        pyautogui.press("enter")
        time.sleep(m)