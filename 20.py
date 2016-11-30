# -*- coding: utf-8 -*-
# @Time     : 2016/11/25 19:19
# @Author   : Span
# @Site     : 
# @File     : 20.py
# @Function : http://www.pythonchallenge.com/pc/hex/idiot2.html
# @Software : PyCharm
# @Solution : http://kwangka.github.io/2015/02/03/pc20/
import inspect
import  wave
wavf = wave.open(r'indian.wav','rb')
india_frames = wavf.readframes(wavf.getnframes())
india_append_frames = []
india_append_frames.append(india_frames[1])
india_append_frames.append(india_frames[0])
print inspect.isframe(india_append_frames)