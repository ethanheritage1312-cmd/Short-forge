from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class VideoRequest(BaseModel):
    url: str

@app.get("/")
def home():
    return {"message": "ShortForge backend is running"}

@app.post("/create-short")
def create_short(video: VideoRequest):
    return {
        "success": True,
        "message": "Video URL received successfully",
        "url": video.url
    }
