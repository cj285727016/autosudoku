from pynput.mouse import Controller as MouseController
from pynput.keyboard import Controller as KeyboardController, Key
import time

def move_mouse_and_press_key(x, y, key='1'):
    # 创建鼠标控制器对象
    mouse = MouseController()
    
    # 创建键盘控制器对象
    keyboard = KeyboardController()
    
    # 移动鼠标到指定坐标
    mouse.position = (x, y)
    #print(f"Mouse moved to ({x}, {y})")
    
    # 暂停一小段时间，确保鼠标移动到位
    time.sleep(0.1)
    
    # 按下并释放指定的键盘键
    keyboard.press(key)
    keyboard.release(key)
    #print(f"Key '{key}' pressed and released")
    time.sleep(0.1)

# 示例：移动鼠标到 (100, 100) 并按键盘的 '1' 键

if __name__ == "__main__":
    x = 100
    y = 100
    move_mouse_and_press_key(x, y)