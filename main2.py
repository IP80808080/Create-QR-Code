import qrcode

qc = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=5, border=2, )

qc.add_data("https://9anime.vc/home")
qc.make(fit=True)
img = qc.make_image(fill_color = "Aqua", back_color="white")
img.save("9anime2.png")