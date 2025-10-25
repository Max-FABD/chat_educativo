from fastapi import FastAPI

app = FastAPI(title="chat educativo con IA")

@app.get("/")
def read_root():
    return {"message": "Bienvenido al chat educativo con IA"}
