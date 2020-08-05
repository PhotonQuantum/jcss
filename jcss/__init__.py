import time
import traceback
from os import path

from starlette.applications import Starlette
from starlette.datastructures import UploadFile
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR

from .model import Result, Status
from .predictor import FileFormatException, Predictor

model_fn = path.join(path.dirname(__file__), 'nn_model.onnx')
predictor = Predictor(model_file=model_fn)


async def predict(request: Request):
    try:
        form = await request.form()
        # noinspection PyTypeChecker
        file: UploadFile = form.get("image", None)
        if not file:
            resp = Result(Status.fail, data={"image": "An captcha image is required."})
            return JSONResponse(resp.dict(), status_code=HTTP_400_BAD_REQUEST)
        contents = await file.read(5120)

        try:
            time_begin = time.time()
            result = predictor.predict(contents)
            time_consumed = time.time() - time_begin
        except FileFormatException:
            resp = Result(Status.fail, data={"image": "Invalid image format."})
            return JSONResponse(resp.dict(), status_code=HTTP_400_BAD_REQUEST)

        resp = Result(Status.success, data={"prediction": result, "elapsed_time": time_consumed})
        return JSONResponse(resp.dict())
    except Exception as e:
        resp = Result(Status.error, message=str(e), data={"traceback": traceback.format_exc()})
        return JSONResponse(resp.dict(), status_code=HTTP_500_INTERNAL_SERVER_ERROR)


app = Starlette(routes=[Route("/", predict, methods=["post"])])
