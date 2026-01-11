from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)
TOOL_URL = os.getenv("TOOL_URL", "http://tool-server:8001/tool")

@app.route("/tool", methods=["POST"])
def handle():
    data = request.json

    print("\n[B] 받은 prompt:", data, flush=True)

    prompt = data.get("prompt", "")
    trace_id = data.get("trace_id", "no-trace")

    if "file" in prompt.lower(): # 프롬프트에 "file"이 있으면
        tool_name = "read_file"
        args = {"path": "/data/hello.txt"}
    else: 
        tool_name = "echo"
        args = {"text": prompt}

    # 받은 prompt로 tool-call 생성
    tool_call = {
        "trace_id": trace_id,
        "stage": "tool-call",
        "tool": tool_name,
        "args": args
    }

    print("[B] 생성된 tool-call:", tool_call, flush=True)

    r = requests.post(TOOL_URL, json=tool_call)

    tool_result = r.json()

    response = {
        "trace_id": trace_id,
        "stage": "response",
        "tool_result": tool_result
    }

    print("[B] 최종 response:", response, flush=True)

    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
