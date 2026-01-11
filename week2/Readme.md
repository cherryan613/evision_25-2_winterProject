## 1. 간단한 코드 구조 설명
해당 주차에서는 Agent A, Agent B, Tool Server로 구성된 멀티 에이전트 구조를 구현하였다. 
Agent A가 prompt를 생성하여 Agent B로 전달하고, Agent B는 A로부터 받은 prompt로부터 tool-call을 생성하여 Tool Server에 전달한다. Tool Server는 B로부터 전달받은 요청에 따라 tool을 실행하고 그 결과를 반환한다.

### 1.1 prompt
<img width="1688" height="691" alt="image" src="https://github.com/user-attachments/assets/72d39384-ba07-45fd-8734-af0e37bc10ee" />
Agent A의 코드을 확인해보면, read_file 프롬프트를 포함한 payload를 Agent B의 url로 POST 하고 있다.
이 단계에서 에이전트의 prompt는 네트워크 메시지에 JSON 형태로 포함된다. 

### 1.2 tool-call
<img width="1620" height="685" alt="image" src="https://github.com/user-attachments/assets/2014195d-f541-487e-8ef0-2ccf6aa1e2cf" />
Agent B의 코드를 확인해보면, A로부터 전달받은 prompt를 기반으로 tool-call을 생성하고 있다. 이 때, prompt에 "file"이 포함되어 있는 경우와 그렇지 않은 경우를 구분하며 규칙 기반으로 제어한다.

### 1.3 response
<img width="1843" height="1052" alt="image" src="https://github.com/user-attachments/assets/04aefff0-917b-4e8d-b6da-efdad52db336" />
Tool Server는 B로부터 받은 tool-call 요청에 따라 작업을 수행하고 반환한다.

## 2. 필수 스크린샷
### 2.1 Wireshark로 네트워크 http 패킷 캡쳐
<img width="2879" height="1022" alt="image" src="https://github.com/user-attachments/assets/42d451c4-b030-4143-8252-777662df250b" />
Agent A, Agent B, Tool Server간 HTTP 통신을 확인할 수 있다. 

### 2.2 캡쳐된 패킷에서 HTTP payload 내 JSON 필드 사진
<img width="2879" height="929" alt="image" src="https://github.com/user-attachments/assets/a15ae8da-d73e-45ca-af90-d675b587ba7a" />
HTTP payload를 확인해보면 hello.txt의 내용이 tool_result의 result로 포함되어있는 것을 확인할 수 있다. tool_result에는 Tool Server의 응답이 그대로 포함되어있는 것을 확인할 수 있으며, hello.txt 내용 뿐만 아니라 호출된 툴(read_file) 정보도 확인할 수 있다.

### 2.3 prompt 값 변경 후 tool-call의 변화 사진
<img width="1439" height="914" alt="image" src="https://github.com/user-attachments/assets/3cbb3884-49de-47be-b12e-d91367b92f4e" />
agnet_a.py에서 prompt 값을 read_file이 아닌 echo hello로 변경해주면 위 사진과 같이 prompt가 echo hello로 확인된다. 

## 3. 1주차 학습과의 정리
Week1에서는 단일 에이전트(Agent A) 내부에서 prompt 처리와 도구 호출이 함수 단위로 이루어졌다. 즉, 에이전트 내부 처리 과정은 네트워크 외부에서 직접 관찰할 수 없었다.
Week2에서는 이를 멀티 에이전트로 분리하여 각 과정을 HTTP 메시지를 통해 상호작용하도록 구성하였다. 
따라서 Agent의 prompt -> tool-call -> response 처리 흐름이 네트워크 패킷 형태로 관찰이 가능해졌다. 
