from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from login_register import app as auth_app

# Create FastAPI app first
app = FastAPI()

# Apply CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include authentication and car routes
app.include_router(auth_app.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
