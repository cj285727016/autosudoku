from PIL import Image
import mss
import mss.tools
import os

def capture_screen_area(left, top, width, height):
    with mss.mss() as sct:
        # 定义截图区域
        monitor = {"left": left, "top": top, "width": width, "height": height}
        # 截图
        screenshot = sct.grab(monitor)
        # 转换为PIL图像
        img = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")
        return img

if __name__ == "__main__":
    left = 800
    right = 1760
    top = 240
    bottom = 1200
    width = right - left
    height = bottom - top
    itemwidth = 106
    outputpath = ".\\output"
    for i in range(0, 9):
        for j in range(0, 9):
            img = capture_screen_area(left + i * itemwidth, top + j * itemwidth, itemwidth, itemwidth)
            #img.show()  # 显示图像
            img.save(os.path.join(outputpath, str(i) + str(j) + ".png"))  # 保存图像

