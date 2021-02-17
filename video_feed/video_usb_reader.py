from .video_reader import VideoReader
from .usb_camera import USBCamera
import cv2
from PIL import Image
import time
import numpy as np

class VideoUSBReader(VideoReader):
    
    def __init__(self, deviceid=0):
        self._camera = USBCamera(deviceid=0, width=224, height=224) 
            
    def read_frame(self,  show_preview=False):
        img = self._camera.read()
        
        if img is None:
            return None
            
        if show_preview:
            cv2.imshow("preview", img)
            cv2.waitKey(1)
        
        return img
        
