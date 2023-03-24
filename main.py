import easyocr
# git hub
# https://github.com/JaidedAI/EasyOCR
image=('ocr.jpg')
reader = easyocr.Reader(['en'])
result = reader.readtext(image,  detail=0, paragraph=True)
print(result)
