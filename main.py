import capture_screen_area
import os
import recognize_digits
import suduku
import mousekey

left = 800
right = 1760
top = 240
bottom = 1200
itemwidth = 106
width = right - left
height = bottom - top
outputpath = ".\\output"
binary_array = [[0 for _ in range(9)] for _ in range(9)]
for i in range(0, 9):
    for j in range(0, 9):
        img = capture_screen_area.capture_screen_area(left + i * itemwidth, top + j * itemwidth, itemwidth, itemwidth)
        #img.show()  # 显示图像
        image_path = os.path.join(outputpath, str(i) + str(j) + ".png")
        img.save(image_path)  # 保存图像
        digits = recognize_digits.recognize_digits(image_path)
        if digits != "":
            binary_array[j][i] = int(digits)
for row in binary_array:
    print(row)

if suduku.solve_sudoku(binary_array):
    print("Solved Sudoku:")
    suduku.print_board(binary_array)
else:
    print("No solution exists")


for i in range(0, 9):
    for j in range(0, 9):
        mousekey.move_mouse_and_press_key(left + 50 + i * itemwidth, top + 50 + j * itemwidth, key=str(binary_array[j][i]))
        