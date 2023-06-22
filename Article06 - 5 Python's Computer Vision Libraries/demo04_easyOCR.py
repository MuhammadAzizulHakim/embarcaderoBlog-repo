import os
os.system('cmd /k "chcp 936"')
import easyocr
 
reader = easyocr.Reader(['ch_sim','en'])
result = reader.readtext('C:/Users/YOUR_USERNAME/chinese2.jpg')
print(result)