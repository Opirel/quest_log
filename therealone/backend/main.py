from fastapi import FastAPI
from database import init_db  # Adjust import as necessary
from routes import router as quests_router
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app= FastAPI()

app.include_router(quests_router)
@app.on_event("startup")
async def startup_event():
    await init_db()


# Add CORS middleware to allow all origins, methods, and headers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

#checks for special signs/invalid characters for added security
@app.middleware("http")
async def check_path(request: Request, call_next):
    # Check if the request path contains invalid characters
    path = request.url.path
    if any(char in path for char in "`@$#%^*=<>[]|\\~"):
        return JSONResponse({"error": "format error"}, status_code=400)

    response = await call_next(request)
    return response 