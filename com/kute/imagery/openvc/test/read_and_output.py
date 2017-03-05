#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/2/27 21:58'

"""

"""

import cv2


def read_and_output():
    frame = 'frame'
    cv2.namedWindow(frame, cv2.WINDOW_AUTOSIZE)
    im = cv2.imread('stinkbug.png')
    cv2.imshow(frame, im)
    if cv2.waitKey(0) == ord('s'):
        cv2.imwrite('stinkbug2.png', im)
    cv2.destroyAllWindows()


def vedio_test():
    """
    通过按键捕获每一帧并显示图片
    """
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        cap.open()
    while True:
        _, frame = cap.read()

        res = cv2.resize(frame, (800, 600), interpolation=cv2.INTER_CUBIC)
        cv2.imshow('image', res)
        # 转为灰度
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # HSVf
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        if cv2.waitKey(0) & 0xFF == ord('s'):
            cv2.imwrite('frame.png', frame)
            cv2.imwrite('gray.png', gray)
            cv2.imwrite('hsv.png', hsv)
            break
    cap.release()
    cv2.destroyAllWindows()


def main():
    # read_and_output()
    vedio_test()


if __name__ == '__main__':
    main()
