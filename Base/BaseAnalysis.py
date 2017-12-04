# -*- coding: utf-8 -*-
import math


# total 是rom容量
def avgMen(men, total):
    if len(men):
        _men = [math.ceil(((men[i]) / total) * 1024) for i in range(len(men))]
        print(_men)
        return str(math.ceil(sum(_men) / len(_men))) + "M"
    return "0"


def avgCpu(cpu):
    if len(cpu):
        resutl = "%.1f" % (sum(cpu) / len(cpu))
        return str(math.ceil(float(resutl)*10)) + "%"
    return "0%"


def avgFps(fps):
    if len(fps):
        return '%.2f' % float(str(math.ceil(sum(fps) / len(fps))))
    return 0.00


def maxMen(men):
    if len(men):
        print("men=" + str(men))
        return str(math.ceil((max(men)) / 1024)) + "M"
    return "0M"


def maxCpu(cpu):
    print("maxCpu="+str(cpu))
    if len(cpu):
        result = "%.1f" % max(cpu)
        return str(math.ceil(float(result)*10)) + "%"
    return "0%"


def maxFps(fps):
    return str(max(fps))


def maxFlow(flow):
    print("---maxFlow111----------")
    print(flow)
    _flowUp = []
    _flowDown = []
    print("---maxFlow2----------2")
    print "len flow:",len(flow[0])
    for i in range(len(flow[0])):
        print("---_flowUp---------")
        print(_flowUp)
        print "i:",i
        if i + 1 == len(flow[0]):
            _flowUp.append(math.ceil((flow[0]) / 1024))
            break
        print "flow[0]:",flow[0]
        _flowUp.append(math.ceil((flow[0][i + 1] - flow[0][i]) / 1024))

    print("---_flowUp---------")
    print(_flowUp)
    for i in range(len(flow[1])):

        print("---maxFlow3333---------")
        print(_flowDown)
        if i + 1 == len(flow[1]):
            _flowDown.append(math.ceil((flow[1]) / 1024))
            break
        _flowDown.append(math.ceil((flow[1][i + 1] - flow[1][i]) / 1024))
    if _flowUp:
        maxFpsUp = str(max(_flowUp)) + "KB"  # 上行流量
    else:
        maxFpsUp = "0"
    if _flowDown:
        maxFpsDown = str(max(_flowDown)) + "KB"  # 下行流量
    else:
        maxFpsDown = "0"
    return maxFpsUp, maxFpsDown

def avgFlow(flow):
    _flowUp = []
    _flowDown = []
    for i in range(len(flow[0])):
        _flowUp.append((flow[0][i + 1] - flow[0][i]) / 1024)
        if i + 1 == len(flow[0]):
            break
    print "_flowUp:",_flowUp
    for i in range(len(flow[1])):
        _flowDown.append((flow[1][i + 1] - flow[1][i]) / 1024)
        print "_flowDown:",_flowDown
        if i + 1 == len(flow[1]):
            break

    print  "11111111111-------------"
    print _flowUp
    avgFpsUp = str(math.ceil(sum(_flowUp) / len(_flowUp))) + "KB"   #不能为0
    print  "22222222222-------------"
    avgFpsDown = str(math.ceil(sum(_flowDown) / len(_flowDown))) + "KB"
    return avgFpsUp, avgFpsDown

if __name__ == '__main__':
    flow = [[93919172, 94987124, 96309507], [14250800, 14285269, 14331153]]
    cpu  = [1.9164759725400458, 0.40045766590389015, 0.8493771234428086, 1.8407534246575343]
    men = [310171, 323267, 321179, 317913, 316569, 335277, 323853, 315837, 333765, 333829, 337433, 337473, 339877, 328953, 328881, 328909, 334029, 329873, 334645, 338649, 332541, 329273, 333581]

    print(avgMen(men, 3014000))
    # print(maxFlow(flow))
