# -*- coding: utf-8 -*-
# @Time     : 2016/11/17 12:41
# @Author   : Span
# @Site     : 
# @File     : 14.py
# @Function : http://www.pythonchallenge.com/pc/return/italy.html
# @Software : PyCharm

from PIL import Image

def moveForward(startPos,direction,nStep):
    """返回从startPos开始，按照direction前进nStep依次得到的坐标，包含startPos
    :type startPos:(int,int）
    :param startPos:开始坐标，（x,y）

    :type direction:(int,int)
    :param direction:前进方向，每个方向的取值只能为-1，0,1
    分别表示坐标减小 不变 增加
    不同的组合可以得到上下左右四个方向，例如（0,1）表示右

    :type nStep： int
    :param nStep: 前进步数， >=0
    """
    pos = [None,None]
    for i in range(len(startPos)):
        if direction[i]==0:
            pos[i] = [startPos[i]] * nStep
        elif direction[i]<0:
            pos[i] = range(startPos[i],startPos[i] - nStep,direction[i])
        else:
            pos[i] = range(startPos[i],startPos[i] + nStep,direction[i])
    return zip(pos[0],pos[1])   #将两个相同长度的列表zip为一个成对的列表

def getPos(allSteps):
    """给定以4个整数为一组的多组步数，返回从（0,0）开始，
    以此按下，右，上，左前进得到的所有坐标
    :type allSteps: 2D int array, the second dimension is 4[[int,int,int,int].....[int,int,int,int]]
    :param allSteps: 多组步数，每一组都包含上下左右四个方向的步数
    """
    start_pos = (0,0)
    pos = []
    for steps in allSteps:
        #down
        if pos:
            start_pos = (pos[-1][0] + 1,pos[-1][1])
        else:
            start_pos = (0,0)
        pos += moveForward(start_pos,(1,0),steps[0])

        #right
        start_pos = (pos[-1][0],pos[-1][1]+1)
        pos += moveForward(start_pos,(0,1),steps[1])

        #up
        start_pos = (pos[-1][0] - 1,pos[-1][1])
        pos += moveForward(start_pos,(-1,0),steps[2])

        #left
        if steps[3] <= 0:
            break
        else:
            start_pos = (pos[-1][0],pos[-1][1] - 1)
            pos += moveForward(start_pos,(0,-1),steps[3])

    return pos

def main():
    im = Image.open('wire.png')
    imdata = list(im.getdata())
    allSteps = [[i,i-1,i-1,i-2] for i in range(100,0,-2)]
    print allSteps
    pos = getPos(allSteps)
    # print pos
    newIm = Image.new(im.mode,(100,100))
    for i in range(len(pos)):
        newIm.putpixel(pos[i],imdata[i])
    newIm.show()

# print moveForward((0,0),(1,0),100)
if __name__ == "__main__":main()
