from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.wine_router import router as wrouter
from fastapi_mcp import FastApiMCP
from routes.yolo_router import router as yrouter

app = FastAPI(title='Wines MCP API')
app.include_router(wrouter)
app.include_router(yrouter)

""" class ImageData(BaseModel):
    image: str  # base64 """

    #a

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True, 
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def read_root():
    return {"message": "Wine classifier API is running"}

""" @app.post("/predict")
def predict_image(data: ImageData):
    decoded = base64.b64decode(data.image.split(",")[-1]) """

if __name__ == '__main__':
    import uvicorn
    mcp = FastApiMCP(app,include_operations=['get_wine_class', 'get_marsupial'])
    mcp.mount()
    uvicorn.run(app, host='0.0.0.0', port=8000)