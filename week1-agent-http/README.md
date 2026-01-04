## 간단한 코드 구조 설명
0. 디렉터리 구조
   <img width="357" height="339" alt="image" src="https://github.com/user-attachments/assets/570ba83d-6b3c-4a3e-84ac-c34cebfe2745" />
   디렉터리 구조는 과제 조건과 일치하게 설정한다.
   
1. agent_a.py
   <img width="1606" height="205" alt="image" src="https://github.com/user-attachments/assets/91a40c4f-31a9-448c-b3f5-8a19bd591f98" />
   agent_a의 역할은 agent_b로 tool_call을 보내는 것이다.
   마찬가지로, 과제 설명에서 확인할 수 있는 tool과 args를 포함하여 tool_call을 작성한다.
   <img width="1631" height="241" alt="image" src="https://github.com/user-attachments/assets/da9b268a-5f22-4f4e-b407-d3d85310403c" />
   agent_b로 post 요청을 보내고 서버 응답을 출력한다.

2. tool_server.py
   <img width="1715" height="314" alt="image" src="https://github.com/user-attachments/assets/24b778b7-8d8c-4b37-9c17-8255d6b3dbe4" />
   tool_server.py는 agent_a로부터 요청을 받아 그 요청을 출력하고 리턴한다. 

## 필수 스크린샷
1. Agent 로그 기반 json 확인
   <img width="1172" height="354" alt="image" src="https://github.com/user-attachments/assets/7f129ff5-ca92-46bf-ab42-59ca0468d422" />
2. 네트워크 패킷 증거
   <img width="2094" height="275" alt="image" src="https://github.com/user-attachments/assets/ef4c9d9f-4989-4057-8ee3-c188eeeca27d" />
