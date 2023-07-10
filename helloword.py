import ddddocr




if __name__ == '__main__':
    # ocr = ddddocr.DdddOcr()
    ocr = ddddocr.DdddOcr(old=True)
    with open("./test.jpg", 'rb') as f:
        image = f.read()
    res = ocr.classification(image)
    print(res)
