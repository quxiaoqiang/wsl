# -*- coding: utf-8 -*-
import requests,sys
from PIL import Image
from pytesseract import image_to_string

# 指定tesseract_cmd本地地址，否则无法实现ocr
tesseract_cmd = '/usr/local/Cellar/tesseract/3.05.01/tesseract'

# url
base_url = 'https://test-a.asean-go.com'
code_url = base_url + '/common-platform/code'
do_login_url = base_url + '/common-platform/doLogin'


# 通过session请求接口，可以自动传入上个接口的cookie
requests.packages.urllib3.disable_warnings() # 不显示https warning
session = requests.Session()

def getCodeImg():
    # 获取验证码图片、保存图片、更改背景、ocr图片验证码
    code_resp = session.request(method='GET', url=code_url, verify=False)
    with open('code.png', 'wb') as f:
        f.write(code_resp.content)
    code = str(image_to_string(changeBackground('code.png')))
    #code = ocrImg(changeBackground('code.png'))
    #print '验证码为：', code
    return code

def changeBackground(img_fp):
    # 更换图片背景颜色
    try:
        img = Image.open(img_fp)
        x, y = img.size
        new_img = Image.new('RGBA', img.size, (255, 255, 255))
        new_img.paste(img, (0, 0, x, y), img)
        return new_img
    except:
        print u'更换图片背景失败'

do_login_data = {
# 初始化登陆账号数据
    'userName':'',
    'password':'',
    'verificationCode': ''
}

def loginData(userName,password):
    do_login_data['userName'] = userName
    do_login_data['password'] = password
    do_login_data['verificationCode'] = getCodeImg()
    print '登陆账号信息：', do_login_data

def doLogin():
    #登陆账号，判断登陆是否成功
    do_login_resp = session.request(method='POST', url=do_login_url, data=do_login_data, verify=False)
    #print 'errorCode:', do_login_resp.json()['errorCode'], 'errorMsg:', do_login_resp.json()['errorMsg']
    if do_login_resp.json()['errorCode'] == 0:
        print '恭喜, ' + do_login_data['userName'] + ' 登陆成功'
        print '------------------------------------------------------------------'
        return session
    else:
        print '哎呀, ' + do_login_data['userName'] + ' 登陆失败'
        print '------------------------------------------------------------------'
        sys.exit()


if __name__ == '__main__':
    loginData('manager','Wsl123456')
    doLogin()
    # demo，获取api数据
    caigouyuanqu = 'https://test-o.asean-go.com/platform-oss/api/backups/account/queryAccountPage?pageNo=1&pageCount=10&accountRole=1'
    url = 'https://test-e.asean-go.com/sys-platform/api/sys/perm/drn/queryByDrnPre?drn=/&page=1&total=291&pageSize=1000000'
    get_menu_resp = session.request(method='GET', url=url, verify=False)
    print get_menu_resp.json()  # 返回dict
    print get_menu_resp.text
