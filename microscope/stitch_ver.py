import numpy as np
import cv2
import os

image_path = "images/"
path = "lines/"
list_dir = sorted(os.listdir(image_path))
list_dir.sort(key=len)
pointer1 = 0
pointer2 = 1
# step 300 - 848 # step 600 - 618 step 900 - 386
y_offset = 618
y_offset2 = 1075 - y_offset
manual = True
horizontal = False
img_count = len(os.listdir(os.path.join(image_path, list_dir[0])))
if not horizontal:
    for y in range(img_count):
        images = []
        for dir in list_dir:
            current_dir = os.path.join(image_path, dir)
            image_list = sorted(os.listdir(current_dir))
            image_list.sort(key=len)
            if int(dir) % 2 == 1:
                image_list = image_list[::-1]
            filename = os.path.join(current_dir, image_list[y])
            img = cv2.imread(filename)
            images.append(img)
        if manual:
            while True:
                res = images[pointer1][(y_offset // 2):-(y_offset // 2), :]
                image2 = images[pointer2][(y_offset // 2):-(y_offset // 2),:]
                res = cv2.vconcat([res, image2])
                cv2.imshow("result", res)
                key = cv2.waitKey(0) & 0xFF
                if key == ord('q'):
                    break
                elif key == ord('a'):
                    y_offset += 1
                elif key == ord('d'):
                    if y_offset > 0:
                        y_offset -= 1
                elif key == ord('w'):
                    cv2.imwrite("y_offset_" + str(y_offset) + ".jpg", res)
                    print("y_offset:", y_offset)
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
            height, _,_= images[0].shape
            res = images[0][:(height + y_offset2) // 2,:]
            for i in range(1, len(images) - 1):
                image2 = images[i][(height - y_offset2) // 2:(height + y_offset2) // 2,:]
                res = cv2.vconcat([res, image2])
            image2 = images[i + 1][(height - y_offset2) // 2:,:]
            res = cv2.vconcat([res, image2])
            cv2.imwrite(str(y) + ".jpg", res)
            # break
else:
    image_list = sorted(os.listdir(path))
    image_list.sort(key=len)
    images = []
    for image in image_list:
        filename = os.path.join(path, image)
        img = cv2.imread(filename)
        images.append(img)
    height, _, _ = images[0].shape
    res = images[0][:(height + y_offset2) // 2, :]
    for i in range(1, len(images) - 1):
        image2 = images[i][(height - y_offset2) // 2:(height + y_offset2) // 2, :]
        res = cv2.vconcat([res, image2])
    image2 = images[i + 1][(height - y_offset2) // 2:, :]
    res = cv2.vconcat([res, image2])
    cv2.imwrite("full_image(horizontal_first).jpg", res)