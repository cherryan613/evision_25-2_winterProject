## 1. Burp Suite, Proxy 개념 학습
velog 정리 제출
https://velog.io/@cherry613/EVIION%EA%B2%A8%EC%9A%B8-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-3%EC%A3%BC%EC%B0%A8-%ED%99%9C%EB%8F%99

## 2. HTTP History
<img width="2880" height="1704" alt="image" src="https://github.com/user-attachments/assets/d272f8ed-d7c1-4fd4-8897-2aea13f1dbc1" />
Agent A <-> Agent B
<img width="2880" height="1704" alt="image" src="https://github.com/user-attachments/assets/f2baa461-6d62-45e8-ad89-ce5c04dee27e" />
Agent B <-> tool-server 

## 3. prompt, tool-call, response 변조
<img width="1517" height="127" alt="image" src="https://github.com/user-attachments/assets/5f5ad3c6-4d85-4d5c-bc4f-5a84d75602a7" />
Burp Suite에서 intercept on 하고, 코드에서는 prompt를 read_file로 작성하여 요청을 보낸다. 
콘솔 창에서 결과를 확인하면 POST 이후 동작에서 멈춰있는 것을 확인할 수 있다.

<img width="2880" height="1704" alt="image" src="https://github.com/user-attachments/assets/2658781c-3541-42ea-a767-a906e1ade7e4" />
Burp Suite에서 prompt를 read_file이 아닌 echo hello로 변경하고 forward 한다.

<img width="2196" height="1292" alt="image" src="https://github.com/user-attachments/assets/03a6c6f2-f59b-4c84-b3cb-b6d97ee01cd2" />
read_file을 echo hello로 변조하여, request는 read_file이지만 이에 대한 response result가 echo hello인 것을 확인할 수 있다.

<img width="1939" height="239" alt="image" src="https://github.com/user-attachments/assets/f7755a95-2800-4d2c-9c7a-880188641c94" />
콘솔 창에서도 B가 받은 prompt가 echo hello이다.

<img width="2030" height="338" alt="image" src="https://github.com/user-attachments/assets/ce8850cb-6bea-40f0-9157-58f94a7f10cf" />
tool-server가 받은 요청과 최종 result 또한 read_file이 아닌 echo hello임을 확인할 수 있다.
