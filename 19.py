# -*- coding: utf-8 -*-
# @Time     : 2016/11/25 17:32
# @Author   : Span
# @Site     : 
# @File     : 19.py
# @Function : http://www.pythonchallenge.com/pc/hex/bin.html
# @Software : PyCharm
# @Solution : http://kwangka.github.io/2015/02/02/pc19/
import wave
import base64
f = open(r"19.txt","rb")
open('indian.wav','wb').write(base64.decodestring(f.read()))
##音频中只有一个sorry  将链接更新之后 并没有成功过关 只出现提示  - "what are you apologizing for?"
##继续看源码中的注释部分提示
##有个提示说out of order 和顺序有关
##不难想到 音频信号的存储方式 数据已连续帧的方式存放 帧是一个声音单元，其长度为样本长度（采样位数）和通道数的乘积
##本关中的音频是单通道，采样位数为2字节 所以每一个声音单元有兩帧
##此外地图上的显示 海洋和陆地的颜色标反了 将音乐单元中的兩帧颠倒 write到新的wav文件 查看结果
wavf = wave.open(r'indian.wav','rb')
india_frames = wavf.readframes(wavf.getnframes())
india_swap = wave.open('indian_swap.wav','wb')
india_swap.setparams(wavf.getparams())   ##声道数, 量化位数（byte单位）, 采样频率, 采样点数, 压缩类型, 压缩类型的描述
india_swap_frames = []
for i in range(0,len(india_frames),2):
    india_swap_frames.append(india_frames[i+1])
    india_swap_frames.append(india_frames[i])
india_swap_frames = ''.join(india_swap_frames)
india_swap.writeframes(india_swap_frames)
india_swap.close()
wavf.close()
##音频内容: You are a idiot