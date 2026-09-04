from fastapi import FastAPI

app = FastAPI(
    title="Warehouse & Smart Inventory Management API",
    version="0.1.0",
)


@app.get("/health", tags=["technical"])
def health() -> dict[str, str]:
    return {"status": "ok"}
