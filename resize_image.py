### resize image to 1920x1080 pixels ###

import cv2, math, os, glob, shutil

folder_fish = ['pod', 'ku_lare', 'see_kun', 'too', 
                'khang_pan', 'hang_lueang', 'sai_dang', 'sai_dum']

for name_image in folder_fish:   

    # create folder resized for add image resize here
    name_dir = f"resized/{name_image}"
    if not os.path.isdir(name_dir):
        os.makedirs(name_dir)
    
    images =[]
    images_path = glob.glob(f"{name_image}/*.jpg")

    for img_path in images_path:
        name_im = img_path.split("\\")[1]
        im = cv2.imread(img_path)
        
        height_img, width_img, channel = im.shape
        
        # resize to 1920, 1080
        if height_img < width_img and height_img > 1920 and width_img > 1080:
            div = width_img / 1920
            new_height = math.ceil(height_img / div)
            new_width = math.ceil(width_img /div)
            reimg = cv2.resize(im, (new_width, new_height))
            cv2.imwrite(f"resized/{name_image}/{name_im}",reimg)
            
        # image vertical    
        elif height_img > width_img and height_img > 1920 and width_img > 1080:
            a = height_img / 1920
            new_width = math.ceil(width_img /a)
            new_height = math.ceil(height_img / a)
            shutil.copy2(f"augmented/{name_image}/{name_im}", f"resized/{name_image}")

        # image size small
        elif height_img <= 1920 or width_img <= 1920:
            shutil.copy2(f"augmented/{name_image}/{name_im}", f"resized/{name_image}")