# -*- coding: utf-8 -*-
"""
qrtools.py: Wrapper around the `qrcode` library for QR code generation.

Modernized from the original GPL-licensed qrtools.py by David Green and
Ramiro Algozino. The webcam/decode functionality has been removed; use
pyzbar directly if barcode reading is needed.
"""

import os
import io
import time
import shutil
import hashlib

import qrcode
from PIL import Image


class QR:
    """Simple QR code generator using the `qrcode` library."""

    def __init__(
        self,
        data="NULL",
        pixel_size=3,
        level="L",
        margin_size=4,
        data_type="text",
        filename=None,
    ):
        self.pixel_size = pixel_size
        self.level = level
        self.margin_size = margin_size
        self.data_type = data_type
        self.data = data
        self.directory = os.path.join("/tmp", "qr-%f" % time.time())
        self.filename = filename
        os.makedirs(self.directory, exist_ok=True)

    def get_tmp_file(self):
        data_bytes = (
            self.data.encode("utf-8") if isinstance(self.data, str) else self.data
        )
        return os.path.join(
            self.directory, hashlib.sha256(data_bytes).hexdigest() + ".png"
        )

    def encode(self, filename=None):
        self.filename = filename or self.get_tmp_file()
        if not self.filename.endswith(".png"):
            self.filename += ".png"

        error_levels = {
            "L": qrcode.constants.ERROR_CORRECT_L,
            "M": qrcode.constants.ERROR_CORRECT_M,
            "Q": qrcode.constants.ERROR_CORRECT_Q,
            "H": qrcode.constants.ERROR_CORRECT_H,
        }

        qr = qrcode.QRCode(
            version=1,
            error_correction=error_levels.get(
                self.level, qrcode.constants.ERROR_CORRECT_L
            ),
            box_size=self.pixel_size,
            border=self.margin_size,
        )
        qr.add_data(self.data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(self.filename)
        return 0

    def destroy(self):
        shutil.rmtree(self.directory, ignore_errors=True)
