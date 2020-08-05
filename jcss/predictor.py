from io import BytesIO

import numpy as np
import onnxruntime as rt
from PIL import Image, UnidentifiedImageError


class FileFormatException(Exception):
    pass


class Predictor:
    def __init__(self, model_file: str = "nn_model.onnx"):
        self._table = [0] * 156 + [1] * 100
        self._sess = rt.InferenceSession(model_file)

    @staticmethod
    def _tensor_to_captcha(tensors):
        captcha = ""
        for tensor in tensors:
            asc = int(np.argmax(tensor, 1))
            if asc < 26:
                captcha += chr(ord("a") + asc)
        return captcha

    def predict(self, img: bytes):
        try:
            img_rec = Image.open(BytesIO(img))
        except UnidentifiedImageError:
            raise FileFormatException
        img_rec = img_rec.convert("L")
        img_rec = img_rec.point(self._table, "1")
        img_np = np.array(img_rec, dtype=np.float32)
        img_np = np.expand_dims(img_np, 0)
        img_np = np.expand_dims(img_np, 0)

        out_tensor = self._sess.run(None, {self._sess.get_inputs()[0].name: img_np})
        output = self._tensor_to_captcha(out_tensor)
        return output
