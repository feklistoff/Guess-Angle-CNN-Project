import cv2
import random
import numpy as np
import matplotlib.image as mpimg


class DataSet:
    def __init__(self, angles, samples, phase='train', batch_size=64, size=64):
        self.angles = angles
        self.sample_paths = samples
        self.phase = phase
        self.batch_size = batch_size
        self.size = size
        # self.labels = np.unique(angles)

    def resize(self, img):
        return cv2.resize(img, (self.size, self.size))

    def random_shift(self, img):
        if random.randint(0, 1) == 0:
            return img
        h, w, c = img.shape
        shape = (w, h)
        M = np.float32([[1, 0, random.randint(-self.size // 7, self.size // 7)],
                        [0, 1, random.randint(-self.size // 9, self.size // 9)]])
        return cv2.warpAffine(img, M, shape)

    def flip(self, img, angle):
        if random.randint(0, 1) == 0:
            return img, angle
        img = np.fliplr(img)
        angle = -angle
        return img, angle

    def normalize(self, img):
        image = np.copy(img)
        image = image / 255.
        return image

    def random_shadow(self, img):
        if random.randint(0, 1) == 0:
            return img
        x_top = random.randint(0, img.shape[1])
        x_bot = random.randint(0, img.shape[1])
        if x_top >= img.shape[1] // 2:
            x_bot = random.randint(0, img.shape[1] // 2)
        if x_top > img.shape[1] // 2:
            x_bot = random.randint(img.shape[1] // 2, img.shape[1])
        x3 = x4 = random.choice([0, img.shape[1]])
        y1 = 0
        y2 = img.shape[0]
        overlay = np.copy(img)
        pts = np.array([[x_top, y1], [x3, y1], [x4, y2], [x_bot, y2]], np.int32)
        shadow = cv2.fillPoly(overlay, [pts], (0, 0, 0))
        alfa = random.uniform(0.2, 0.8)
        return cv2.addWeighted(shadow, alfa, img, 1 - alfa, 0)

    def get_next_batch(self):
        batch_imgs = []
        batch_angles = []
        if self.phase == 'train':
            for i in range(self.batch_size):
                rnd_idx = random.randint(0, len(self.sample_paths) - 1)
                angle = self.angles[rnd_idx]
                img = mpimg.imread(self.sample_paths[rnd_idx])
                # img = self.random_shift(img)
                # img = self.random_shadow(img)
                # img, angle = self.flip(img, angle)
                # img = self.resize(img)
                img = self.normalize(img)
                batch_imgs.append(img)
                batch_angles.append(angle)
        if self.phase == 'valid' or self.phase == 'test':
           for i in range(self.batch_size):
                rnd_idx = random.randint(0, len(self.sample_paths) - 1)
                angle = self.angles[rnd_idx]
                img = mpimg.imread(self.sample_paths[rnd_idx])
                # img = self.resize(img)
                img = self.normalize(img)
                batch_imgs.append(img)
                batch_angles.append(angle)
        # if self.phase == 'test':
        #     for i in range(self.batch_size):
        #         rnd_idx = random.randint(0, len(self.sample_paths) - 1)
        #         angle = self.angles[rnd_idx]
        #         img = mpimg.imread(self.sample_paths[rnd_idx])
        #         batch_imgs.append(img)
        #         batch_angles.append(angle)
        return np.asarray(batch_imgs), np.asarray(batch_angles)
