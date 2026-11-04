from fastapi import FastAPI, Response

from .api.routers import all_routers


app = FastAPI(
    title="To Do List analog Jira/Asana"
)


for router in all_routers:
    app.include_router(router)


@app.get("/")
async def root():
    return Response("Server is runing!")

