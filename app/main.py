import uvicorn
from fastapi import FastAPI

from routes.student import router as StudentRouter
from routes.admin import router as AdminRouter

from fastapi_pagination import add_pagination


app = FastAPI()


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app."}


app.include_router(AdminRouter, tags=["Administrator"], prefix="/admin")
app.include_router(StudentRouter, tags=["Students"], prefix="/student")

add_pagination(app)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8889, reload=True)