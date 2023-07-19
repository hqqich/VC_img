import unittest
from base64 import b64decode

import ddddocr


class MyTestCase(unittest.TestCase):
    # base64  转    成图片
    def test_something3(self):
        strs = "".split(',')[1]
        imgdata = b64decode(strs)
        file = open("b.jpg", 'wb')
        file.write(imgdata)
        file.close()


    def test_something(self):

        slide = ddddocr.DdddOcr(det=False, ocr=False)
        with open('./b.jpg', 'rb') as f:
            target_bytes = f.read()
        with open('./a.jpg', 'rb') as f:
            background_bytes = f.read()
        res = slide.slide_match(target_bytes, background_bytes, simple_target=True)
        print(res)
        # det = ddddocr.DdddOcr(det=False, ocr=False)
        #
        # with open('b.jpg', 'rb') as f:
        #     target_bytes = f.read()
        #
        # with open('a.jpg', 'rb') as f:
        #     background_bytes = f.read()
        #
        # res = det.slide_match(target_bytes, background_bytes)
        #
        # print(res)
        # print("test")
        # self.assertEqual(True, False)  # add assertion here

if __name__ == '__main__':
    unittest.main()
