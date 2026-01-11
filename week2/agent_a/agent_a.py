import os
import time
import uuid
import requests

# 과제 설명과 동일
PROMPT = os.getenv("PROMPT", "echo hello")
AGENT_B_URL = os.getenv("AGENT_B_URL", "http://agent-b:8001/tool")

def main():
    # agent-b 서버가 준비될 때까지 대기
    time.sleep(3)
    
    trace_id = str(uuid.uuid4())

    payload = {
        "trace_id": trace_id,
        "stage": "prompt",
        "prompt": PROMPT,
    }

    r = requests.post(
        AGENT_B_URL,
        json=payload,
        timeout=3
    )

    print("서버 응답: ", r.json(), flush=True)


if __name__ == "__main__":
    main()
