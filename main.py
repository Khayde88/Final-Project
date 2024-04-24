import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse

app = FastAPI()

# Enable CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],  # Adjust as needed for your frontend URL
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

@app.get("/")
async def read_index():
    return FileResponse("./Frontend/Home.html")

app.mount("/", StaticFiles(directory="Frontend"), name="static")

# Start the FastAPI application
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)