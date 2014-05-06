# -*- coding: utf8 -*-
#!/usr/bin/env python
import os
import shutil
import base64
from qrtools import QR
cedula=raw_input("Cedula del profesor para generar el QR: ")
nombre=cedula
for i in range(1,10):
    cedula=base64.b64encode(cedula)
code = QR(data=cedula, pixel_size=10)
code.encode()
src = code.get_tmp_file()
dst = '%s/qr/%s.png'%(os.getcwd(),nombre)
shutil.copy(src, dst)
