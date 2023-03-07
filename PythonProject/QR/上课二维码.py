from MyQR import myqr
import zxing
wenzi='昌浩是帅哥'.encode('utf-8')
myqr.run(words="changhao is a handsome boy",
         picture="bj2.jpg",
         colorized=True,
         save_name="changhao.png")

reader=zxing.BarCodeReader()
barcode=reader.decode("changhao.png")
barcode.parsed