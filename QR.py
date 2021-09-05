import qrcode

kod = qrcode.QRCode(box_size=10, border=5)

kod.add_data("virtual env turli loyihalar uchun Python paketlarini boshqarish uchun ishlatiladi. Virtualenv -dan foydalanish butun dunyo bo'ylab Python paketlarini o'rnatish, saqlash imkonini beradi.")

img = kod.make_image(fill_color="#C21554")

img.save("qrcode.png")

