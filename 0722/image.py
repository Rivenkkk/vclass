import cv2


def photochoose():
    a = int(input("please enter"))
    if a==1:
        img = cv2.imread("Lenna.jpg")
        cv2.imshow("lookyou",img)
        cv2.waitKey(0)
    elif a==2:
        img = cv2.imread("ditto.jpg")
        cv2.imshow("lookyou",img)
        cv2.waitKey(0)
    else:
        print("error")
        photochoose()

photochoose()
    


