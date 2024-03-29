# -*- coding: utf-8 -*-
import base64
from io import BytesIO


def image_to_base64(image, format="JPEG"):
    # 将图像数据编码为 Base64 字符串
    buffered = BytesIO()
    image.save(buffered, format=format)  # 这里可以根据实际情况选择图像格式
    image_data = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return image_data
