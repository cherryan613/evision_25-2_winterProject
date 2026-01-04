from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class ToolRequest(BaseModel):
    tool: str
    args: dict

@app.post("/tool")
async def tool(request: ToolRequest):
    print(f"받은 요청: tool='{request.tool}' args={request.args}", flush=True)
    
    return {
        "status": "ok",
        "tool": request.tool,
        "args": request.args
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
