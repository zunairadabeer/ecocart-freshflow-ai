from fastapi import FastAPI

app = FastAPI(
    title="EcoCart FreshFlow"
)


@app.get("/")
def home():

    return {
        "project": "EcoCart FreshFlow",
        "status": "active development"
    }
