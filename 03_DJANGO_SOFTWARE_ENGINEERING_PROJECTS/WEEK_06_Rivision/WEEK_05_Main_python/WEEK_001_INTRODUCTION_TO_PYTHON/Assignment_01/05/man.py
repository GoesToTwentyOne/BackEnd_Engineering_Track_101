import pyautogui
def draw_pyramid(num_rows):
    for i in range(1, num_rows+1):
        for j in range(1, i+1):
            pyautogui.typewrite('#')
        pyautogui.press('enter')           
num_rows = int(input())
draw_pyramid(num_rows)
