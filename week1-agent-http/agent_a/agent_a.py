from fastapi import FastAPI
import requests
import uvicorn

app = FastAPI()

@app.get("/send")
async def send():
    tool_call = {
        "tool": "read_file",
        "args": {
            'path': '/hello.txt'
        }
    }

    r = requests.post(
        "http://agent-b:8001/tool",
        json=tool_call,
        timeout=3
    )

    print("서버 응답: ", r.json(), flush=True)

    return {
        "agent": "A",
        "sent": tool_call,
        "response_from_B": r.json()
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
