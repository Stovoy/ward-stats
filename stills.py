from PIL import Image
import subprocess
import os
import numpy


def generate_stills(title):
    os.makedirs('stills/%s/raw' % title)
    file = 'videos/%s.mp4' % title
    if not os.path.isfile(file):
        file = 'videos/%s.mkv' % title

    command = ['ffmpeg',
               '-i', file,
               '-f', 'image2pipe',
               '-pix_fmt', 'rgb24',
               '-vcodec', 'rawvideo', '-']
    pipe = subprocess.Popen(command, stdout=subprocess.PIPE, bufsize=10 ** 8)

    # The videos are 1280x720.
    # 60 frames per second.
    # 1 screenshot every 3 seconds = skip 180 frames.

    width = 1280
    height = 720

    frame_bytes = width * height * 3
    frames_to_skip = 180

    frame = 0
    while True:
        pipe.stdout.read(frame_bytes * frames_to_skip)
        pipe.stdout.flush()

        raw_image = pipe.stdout.read(frame_bytes)

        try:
            image = numpy.fromstring(raw_image, dtype='uint8')
            image = image.reshape((height, width, 3))
        except ValueError:
            # End of video.
            break

        Image.fromarray(image).save('stills/%s/raw/%s.jpg' % (title, frame))
        frame += 1

        pipe.stdout.flush()
