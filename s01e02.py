import cv2
import numpy as np


def ex_0():
    def nothing(x):
        pass

    # Create a black image, a window
    img = np.zeros((300,512,3), np.uint8)
    cv2.namedWindow('image')

    # create trackbars for color change
    cv2.createTrackbar('R','image',0,255,nothing)
    cv2.createTrackbar('G','image',0,255,nothing)
    cv2.createTrackbar('B','image',0,255,nothing)

    # create switch for ON/OFF functionality
    switch = '0 : OFF \n1 : ON'
    cv2.createTrackbar(switch, 'image',0,1,nothing)

    while(1):
        cv2.imshow('image',img)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

        # get current positions of four trackbars
        r = cv2.getTrackbarPos('R','image')
        g = cv2.getTrackbarPos('G','image')
        b = cv2.getTrackbarPos('B','image')
        s = cv2.getTrackbarPos(switch,'image')

        if s == 0:
            img[:] = 0
        else:
            img[:] = [b,g,r]

    cv2.destroyAllWindows()


def ex_1():
    print("Function not implemented yet!")


def ex_2():
    img_from_file = cv2.imread("_data//qr.jpg", cv2.IMREAD_GRAYSCALE)
    cv2.imshow("img_from_file", img_from_file)

    fx = 1.75
    fy = 1.75

    img_scaled_1 = cv2.resize(img_from_file, (0, 0), fx=fx, fy=fy, interpolation=cv2.INTER_LINEAR)
    img_scaled_2 = cv2.resize(img_from_file, (0, 0), fx=fx, fy=fy, interpolation=cv2.INTER_NEAREST)
    img_scaled_3 = cv2.resize(img_from_file, (0, 0), fx=fx, fy=fy, interpolation=cv2.INTER_AREA)
    img_scaled_4 = cv2.resize(img_from_file, (0, 0), fx=fx, fy=fy, interpolation=cv2.INTER_LANCZOS4)
    cv2.imshow("INTER_LINEAR", img_scaled_1)
    cv2.imshow("INTER_NEAREST", img_scaled_2)
    cv2.imshow("INTER_AREA", img_scaled_3)
    cv2.imshow("INTER_LANCZOS4", img_scaled_4)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def ex_3():
    print("Function not implemented yet!")


if __name__ == "__main__":
    ex_0()
    # ex_1()
    # ex_2()
    # ex_3()
