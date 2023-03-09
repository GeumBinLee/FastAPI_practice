# pip install fastapi
# pip install "uvicorn[standard]"

from typing import Union

from fastapi import FastAPI
app = FastAPI()


@app.get("/") # "/" 경로로 HTTP requests(GET)를 받는다.
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}") # "/items/{item_id}" 경로로 HTTP requests(GET)를 받는다.
def read_item(item_id: int, q: Union[str, None] = None): # 그떄 int 타입인 item_id가 매개변수로 필요하다. q는 optional.
    return {"item_id": item_id, "q": q}

'''
1. 서버 가동 : uvicorn main:app --reload
2. 페이지 접속 : http://127.0.0.1:8000/items/5?q=somequery
3. 확인 가능 : {"item_id":5,"q":"somequery"}
4. 쿼리스트링으로 아무것도 안 날리면 (-> http://127.0.0.1:8000/items/5)
5. 그냥 {"item_id":5,"q":null}이라고 null로 뜸.
'''

'''
http://127.0.0.1:8000/docs 가면 swagger가 자동으로 만들어져 있다.
http://127.0.0.1:8000/redoc -> ReDoc
'''