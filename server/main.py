from fastapi import FastAPI
<<<<<<< HEAD:server/main.py
from api.routes import router
from fastapi.middleware.cors import CORSMiddleware

=======
from fastapi.middleware.cors import CORSMiddleware

from api.routes import router

>>>>>>> origin/main:Dollar-exchange-rate/server/main.py

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
)
<<<<<<< HEAD:server/main.py
app.include_router(router)
print("Server is running...")
=======
app.include_router(router)
>>>>>>> origin/main:Dollar-exchange-rate/server/main.py
