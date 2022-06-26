import cv2
import numpy as np

class BackSubtraction(object):
    def blur_color_img(self, img, kernel_width=5, kernel_height=5, sigma_x=2, sigma_y=2):
        #increse brightness for foreground
        
        img = np.copy(img) # we don't modify the original image
        img[:,:,0] = cv2.GaussianBlur(img[:,:,0], ksize=(kernel_width, kernel_height), sigmaX=sigma_x, sigmaY=sigma_y)
        img[:,:,1] = cv2.GaussianBlur(img[:,:,1], ksize=(kernel_width, kernel_height), sigmaX=sigma_x, sigmaY=sigma_y)
        img[:,:,2] = cv2.GaussianBlur(img[:,:,2], ksize=(kernel_width, kernel_height), sigmaX=sigma_x, sigmaY=sigma_y)
        return img

    def preprocessing_backsubtraction(self, mask_test):
        kernel = np.ones((5,5), np.uint8)
        fgMask = cv2.erode(mask_test, kernel, iterations=1) 
        fgMask = cv2.dilate(fgMask, kernel, iterations=1)
        fgMask = cv2.GaussianBlur(fgMask, (3,3), 0)
        fgMask = cv2.morphologyEx(fgMask, cv2.MORPH_CLOSE, kernel)
        _,fgMask = cv2.threshold(fgMask,0,255,cv2.THRESH_BINARY)
        # cv2.imshow("image",fgMask)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        return fgMask

    def backSubtraction(self, image_background, image_foreground):
        fg_cropImageFill_hsl = cv2.cvtColor(image_foreground, cv2.COLOR_RGB2HLS)
        delta = cv2.cvtColor(image_foreground, cv2.COLOR_RGB2HLS)[:, :, 2].mean() - cv2.cvtColor(image_background, cv2.COLOR_RGB2HLS)[:, :, 2].mean()
        np.add(fg_cropImageFill_hsl[:, :, 2], delta, out=fg_cropImageFill_hsl[:, :, 2], casting="unsafe")
        fg_cropImageFill_hsl = cv2.cvtColor(fg_cropImageFill_hsl, cv2.COLOR_HLS2RGB)

        bg_cropImageFill_Blur = self.blur_color_img(image_background)
        fg_cropImageFill_Blur = self.blur_color_img(fg_cropImageFill_hsl)
        # display_image(fg_cropImageFill_Blur)
        #cần chuyển đổi ma trận ảnh về kiểu type trước khi thực hiện hiệu trừ
        mask = fg_cropImageFill_Blur - bg_cropImageFill_Blur #ma trận ảnh được biểu diễn dưới dạng uming8 do đó nó sẽ không lưu số âm
        mask = np.abs(mask)
        # blur_color_img(mask)
        mask_hsl = cv2.cvtColor(mask, cv2.COLOR_RGB2HLS)
        # chủ yếu thay đổi về cường độ sáng còn thay đổi về màu thì ít do đó, ta cần quan tâm sự thay đổi về độ màu
        self.lower_thread = np.array([8, 100, 50])
        self.upper_thread = np.array([180, 255, 255])
        self.mask_test = cv2.inRange(mask_hsl, self.lower_thread, self.upper_thread)
        res = cv2.bitwise_and(image_foreground, image_background, self.mask_test)
        return self.mask_test

