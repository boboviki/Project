import requests

res = requests.get("https://video.pearvideo.com/mp4/adshort/20180613/cont-1365496-12251302_adpkg-ad_hd.mp4")

with open("梨视频.mp4", "wb") as f:
    for item in res.iter_content():
        f.write(item)
