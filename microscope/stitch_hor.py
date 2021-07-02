import numpy as np
import cv2
import os

image_path = "images/"
path = "lines/"
list_dir = sorted(os.listdir(image_path))
pointer1 = 0
pointer2 = 1
# step 300 - 594, step 600 - 366, step 900 - 138
x_offset = 594
x_offset2 = 1650 - x_offset
manual = True
vertical = False
if not vertical:
    for dir in list_dir:
        images = []
        currenr_dir = os.path.join(image_path, dir)
        image_list = sorted(os.listdir(currenr_dir))
        image_list.sort(key=len)
        # if int(dir) % 2 == 1:
        #     image_list = image_list[::-1]
        for image in image_list:
            filename = os.path.join(currenr_dir, image)
            img = cv2.imread(filename)
            images.append(img)
        if manual:
            while True:
                _, width, _= images[pointer1].shape
                # odl algo
                # res = images[pointer1][:, (x_offset2 // 2):-(x_offset // 2)]
                res = images[pointer1][:, :int((width // 4) * 3) + 1]
                image2 = images[pointer2][:,int(width // 4) + x_offset:int((width // 4) * 3) + 1]
                res = cv2.hconcat([res, image2])
                cv2.imshow("result", res)
                key = cv2.waitKey(0) & 0xFF
                if key == ord('q'):
                    break
                elif key == ord('a'):
                    x_offset += 1
                elif key == ord('d'):
                    if x_offset > 0:
                        x_offset -= 1
                elif key == ord('w'):
                    cv2.imwrite("x_offset_" + str(x_offset) + ".jpg", res)
                    print("x_offset:", x_offset)
                elif key == ord('n'):
                    if pointer2 < (len(images) - 1):
                        pointer1 += 1
                        pointer2 += 1
                elif key == ord('p'):
                    if pointer1 > 0:
                        pointer1 -= 1
                        pointer2 -= 1
            # break
        else:
            _, width, _= images[0].shape
            res = images[0][:, :int((width // 4) * 3) + 1]
            for i in range(1, len(images) - 1):
                image2 = images[i][:,int(width // 4) + x_offset:int((width // 4) * 3) + 1]
                res = cv2.hconcat([res, image2])
            image2 = images[i + 1][:, int(width // 4) + x_offset:]
            res = cv2.hconcat([res, image2])
            cv2.imwrite(str(dir) + ".jpg", res)
            # break
else:
    image_list = sorted(os.listdir(path))
    image_list.sort(key=len)
    images = []
    for image in image_list:
        filename = os.path.join(path, image)
        img = cv2.imread(filename)
        images.append(img)
    _, width, _ = images[0].shape
    res = images[0][:, :(width + x_offset2) // 2]
    for i in range(1, len(images) - 1):
        image2 = images[i][:, (width - x_offset2) // 2:(width + x_offset2) // 2]
        res = cv2.hconcat([res, image2])
    image2 = images[i + 1][:, (width - x_offset2) // 2:]
    res = cv2.hconcat([res, image2])
    cv2.imwrite("full_image(vertical_first).jpg" + ".jpg", res)
