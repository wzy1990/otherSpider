#pip install baidu-aip 安装百度ai包
from aip import AipSpeech

def saveAudio(text):
    APP_ID = '16447976'
    API_KEY = '1QhBhs2hNzqExQmAeoqfsmGT'
    SECRET_KEY = 'eauwMxQtNhR6wcfnnC8Ts6CNhecDaKO0'
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    result = client.synthesis(text, 'zh', 1, {  # text 不超过1000个字节，不然会失败
        'vol': 5,  # 音量，取值0-15，默认为5中音量
        'spd': 4,  # 语速，取值0-15，默认为5中语速
        'pit': 5,  # 音调，取值0-15，默认为5中语调
        'per': 0,  # 发音人选择, 0为女声，1为男声，3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女
    })

    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open('auido.mp3', 'wb') as f:
            f.write(result)
    else:
        print(result)
        print(result['err_msg'])

def formated(content):
    lines = content.split("\n")
    res = ""
    for line in lines:
        res += line.strip()
    return res

# 打开文本文件
with open(r'novel/海贼王之天天挂机/第一章 天天挂机系统！.txt', encoding="utf-8",errors='ignore') as f:
    content = f.read()
    text = formated(content)
    print(len(text), text)

    # 将读取的文本转换成语音保存
    saveAudio(text[1:1000])

    # 关闭文件
    f.close()

