from fastapi import FastAPI
from app.routers import predict

app = FastAPI()

# Inclure le router pour la prédiction
app.include_router(predict.router, prefix="/predict")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
