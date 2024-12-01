from fastapi import FastAPI
from planner.routes.users import user_router
from planner.routes.events import event_router
import uvicorn

app = FastAPI()

app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")


if __name__ == "__main__":
    uvicorn.run("planner.app:app", host="0.0.0.0", port=8080, reload=True)
    