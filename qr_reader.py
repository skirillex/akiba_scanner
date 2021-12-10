import cv2
import os
from PIL import Image



def pick_up_images():
    path = r"images"
    image_list = os.listdir(path)
    print(f"image list: {image_list}")
    for image_file in image_list:
        qr_text = decode_qr(image_file)
        if qr_text:
            print(f"{image_file}")
            print(f"QR Value: {qr_text}")


def decode_qr(image_filename):

    img = cv2.imread(fr"images/{image_filename}", flags=cv2.IMREAD_REDUCED_GRAYSCALE_8) #flags=cv2.IMREAD_GRAYSCALE)
    #cv2.imshow('image',img)
    #cv2.waitKey(0)
    #img2 = Image.open(r"images/DSC04890.jpg")
    #width, height = Image.open(r"images/DSC04890.jpg").size

    #print(width*height)
    #img2.show()
    detector = cv2.QRCodeDetector()

    val, pts, st_code = detector.detectAndDecode(img)

    #print(f"value: {val}")
    #print(f"Coordinates: {pts}")
    #print(f"{st_code}")

    if val:
        return val

pick_up_images()
#decode_qr(f"DSC04898.jpg")

