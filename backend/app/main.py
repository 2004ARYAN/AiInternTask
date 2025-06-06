from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Wasserstoff AI Intern Task – FastAPI is running!"}