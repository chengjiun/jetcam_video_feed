from video_feed.video_usb_reader import VideoUSBReader

video_reader = VideoUSBReader(deviceid=0)
num_frames = 0
show_preview = True

while True:
    img = video_reader.read_frame(show_preview=True)
    num_frames += 1
