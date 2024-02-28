# -*- coding:utf-8 -*-
# Status: PASS
# Time:  2022-09-01

import pyttsx3

class Voice(object):

    def create_engine(self):
        #创建对象
        engine = pyttsx3.init()
        # 获取当前语音速率
        rate = engine.getProperty('rate')
        print(f'语音速率：{rate}')
        # 设置新的语音速率
        engine.setProperty('rate', 200)
        # 获取当前语音音量
        volume = engine.getProperty('volume')
        print(f'语音音量：{volume}')
        # 设置新的语音音量，音量最小为 0，最大为 1
        engine.setProperty('volume', 1.0)
        # 获取当前语音声音的详细信息
        voices = engine.getProperty('voices')
        print(f'语音声音详细信息：{voices}')
        # 设置当前语音声音为女性，当前声音不能读中文
        engine.setProperty('voice', voices[1].id)
        # 设置当前语音声音为男性，当前声音可以读中文
        engine.setProperty('voice', voices[0].id)
        # 获取当前语音声音
        voice = engine.getProperty('voice')
        print(f'语音声音：{voice}')
        path = 'test.txt'  # 或者直接导入一个文本文件
        return engine

    def machine_read(self,content):
        # 语音文本
        # 将语音文本说出来
        engine = self.create_engine()
        engine.say(content)
        engine.runAndWait()
        engine.stop()

if __name__ == '__main__':
    content = """金樽清酒斗十千，玉盘珍羞直万钱。
        欲渡黄河冰塞川，将登太行雪满山。
        闲来垂钓碧溪上，忽复乘舟梦日边。
        行路难，行路难，多歧路，今安在？
        长风破浪会有时，直挂云帆济沧海。"""
    vo = Voice()
    vo.machine_read(content)