#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from pytesseract import *
from PIL import Image
import time
import urllib2

#https://a.asean-go.com/common-platform/doLogin


def requests_code_img(codeUrl):
    #保存验证码图片
    t = int(time.time() * 1000)
    page = urllib2.build_opener().open(codeUrl,str(t))
    pic = page.read()
    img = open('code.png', "wb")
    img.write(pic)
    img.close()

def change_background(imgFilepath):
    #更换图片背景颜色
    try:
        img = Image.open(imgFilepath)
        x,y = img.size
        new_img = Image.new('RGBA', img.size, (255,255,255))
        new_img.paste(img,(0,0,x,y),img)
        return new_img
    except:
        return u'更换图片背景失败'

def picture_ocr(imgFilepath):
    #识别更改背景的图片的字符
    tesseract_cmd = '/usr/local/Cellar/tesseract/3.05.01/tesseract'    #须指定tesseract
    #requests_code_img('https://a.asean-go.com/common-platform/code')   #获取验证码图片
    return str(image_to_string(change_background(imgFilepath)))




if __name__ == '__main__':
    print picture_ocr('./code.png')



