from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import yt_dlp
import os
import uuid
import subprocess
from fastapi.responses import FileResponse
import imageio_ffmpeg
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
    job_id = str(uuid.uuid4())

    input_file = f"/tmp/{job_id}.mp4"
    output_file = f"/tmp/{job_id}_short.mp4"

    ydl_opts = {
        "format": "mp4/best",
        "outtmpl": input_file,
        "quiet": True,
        "extractor_args": {
    "youtube": {
        "pot_bgutil_base_url": [os.getenv("POT_PROVIDER_URL")]
    }
        }
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video.url])

        ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()

        command = [
            ffmpeg,
            "-y",
            "-i", input_file,
            "-t", "30",
            "-vf", "scale=1080:-2,crop=1080:1920",
            "-c:v", "libx264",
            "-c:a", "aac",
            output_file
        ]

        subprocess.run(command, check=True)

        return FileResponse(
            output_file,
            media_type="video/mp4",
            filename="shortforge-short.mp4"
        )

    except Exception as e:
        return {
            "success": False,
            "message": str(e)
        }

    
        
        
    

    

            

        
            
        
        
            
            
    

    
        
        
        

