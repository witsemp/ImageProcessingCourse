import cv2


def ex_0():
    cap = cv2.VideoCapture(0) #"_data/s01e01/Wildlife.mp4"

    key = ord('a')

    while key != ord('q'):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        img_filtered = cv2.GaussianBlur(img_gray, (7, 7), 1.5)
        img_edges = cv2.Canny(img_filtered, 0, 30, 3)

        # Display the resulting frame
        cv2.imshow('result', img_edges)
        # Waiting for the key pressed
        key = cv2.waitKey(50)

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


def ex_1():
    img_from_file = cv2.imread("_data/no_idea.jpg", cv2.IMREAD_GRAYSCALE)
    cv2.imshow("img_from_file", img_from_file)
    cv2.waitKey(0)
    cv2.imwrite("_data/no_idea_grayscale.png", img_from_file)
    cv2.destroyAllWindows()


def ex_2():
    img_color = cv2.imread("_data/no_idea.jpg", cv2.IMREAD_COLOR)
    img_grayscale = cv2.imread("_data/no_idea.jpg", cv2.IMREAD_GRAYSCALE)

    print("Pixel (220, 270) value color: " +
          str(img_color[220, 270]) +
          ", greyscale: " +
          str(img_grayscale[220, 270])
          )

    print("Color image parameters: " + str(img_color.shape))
    print("Grayscale image parameters: " + str(img_grayscale.shape))

    head = img_color[10:120, 250:420]
    img_with_head = img_color.copy()
    img_with_head[60:170, 50:220] = head

    img_bgr_test = cv2.imread("_data/s01e01/AdditiveColor.png", cv2.IMREAD_COLOR)

    b, g, r = cv2.split(img_bgr_test)

    cv2.imshow('img_color', img_color)
    cv2.imshow('img_grayscale', img_grayscale)
    cv2.imshow('head', head)
    cv2.imshow('img_with_head', img_with_head)
    cv2.imshow('b', b)
    cv2.imshow('g', g)
    cv2.imshow('r', r)

    key = cv2.waitKey(0)


def ex_3():
    cap = cv2.VideoCapture("_data/s01e01/Wildlife.mp4")

    key = ord(' ')
    ret = True

    while key != ord('q') and ret:

        if key == ord(' '):
            ret, frame = cap.read()
            if ret:
                cv2.imshow('video_frame', frame)
            else:
                print("End of video file!")
        key = cv2.waitKey(10)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    ex_0()
    # ex_1()
    # ex_2()
    # ex_3()
