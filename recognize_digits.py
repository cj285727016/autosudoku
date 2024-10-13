from PIL import Image
from PIL import Image, ImageOps
import cv2
import numpy as np
import pytesseract

# 设置 Tesseract 可执行文件的路径（仅在 Windows 上需要）
pytesseract.pytesseract.tesseract_cmd = r'D:\TesseractOCR\tesseract.exe'
def preprocess_image(image_path):
    # 加载图像
    image = Image.open(image_path)
    
    # 灰度化
    image_gray = ImageOps.grayscale(image)
    
    # 二值化
    threshold = 128
    image_binary = image_gray.point(lambda x: 0 if x < threshold else 255, '1')
    
    # 将处理后的图像转换为 NumPy 数组
    image_array = np.array(image_binary)
    
    # 确保图像数组的类型为 uint8
    image_array = image_array.astype(np.uint8)
    
    # 去噪
    image_blur = cv2.GaussianBlur(image_array, (3, 3), 0)
    _, image_cleaned = cv2.threshold(image_blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # 将处理后的图像转换回 PIL 格式
    image_processed = Image.fromarray(image_cleaned)
    
    return image_processed

def recognize_digits(image_path):
    # 打开图像
    image = preprocess_image(image_path)
    
    # 使用 pytesseract 进行 OCR 识别
    text = pytesseract.image_to_string(image, config='--psm 10 --oem 3 -c tessedit_char_whitelist=123456789')
    
    # 返回识别到的数字
    return text.strip()

if __name__ == "__main__":
    # 示例：识别图片中的数字
    image_path = 'digits.png'
    digits = recognize_digits(image_path)
    print(f"Recognized digits: {digits}")