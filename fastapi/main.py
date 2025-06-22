from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.wine_router import router

app = FastAPI()
app.title = 'Wines API'
app.include_router(router)

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

