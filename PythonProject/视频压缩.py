import subprocess
import imageio_ffmpeg


compress = "{} -i vedio.mp4 -r 24 -vcodec h264 vedionew.mp4".format(imageio_ffmpeg.get_ffmpeg_exe())
compress2 = "{} -i 'F:\\01 录屏\\02 CSS选择器1.flv' -r 24 -vcodec h264 'F:\\01 录屏\\02 CSS选择器1压缩.mp4'".format(imageio_ffmpeg.get_ffmpeg_exe())

f = subprocess.Popen(compress2).wait()

print("ok")