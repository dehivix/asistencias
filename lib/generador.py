# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
import shutil
import base64
from lib.qrtools import QR

cedula = input("Cedula del profesor para generar el QR: ")
nombre = cedula
for _ in range(1, 10):
    cedula = base64.b64encode(cedula.encode("utf-8")).decode("utf-8")
code = QR(data=cedula, pixel_size=10)
code.encode()
src = code.get_tmp_file()
dst = os.path.join(os.getcwd(), "qr", "%s.png" % nombre)
os.makedirs(os.path.dirname(dst), exist_ok=True)
shutil.copy(src, dst)
print("QR generado en: %s" % dst)
