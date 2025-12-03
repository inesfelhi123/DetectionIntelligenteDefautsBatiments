from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from app.services.roboflow_client2 import predict_image

router = APIRouter()

@router.post("/")
async def predict(image: UploadFile = File(...)):
    try:
        image_bytes = await image.read()
        top_class, confidence = predict_image(image_bytes)
        return JSONResponse({"class": top_class, "confidence": confidence})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)
