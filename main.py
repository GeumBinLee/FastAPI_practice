# pip install fastapi
# pip install "uvicorn[standard]"
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

"""
pydantic은 type annotation을 사용해서 데이터를 검증하고 설정들을 관리하는 라이브러리다.
runtime에서 type을 강제하고, type이 유효하지 않을 때 에러를 발생시킨다.

validation 라이브러기 아니라 parsing 라이브러리이다.
유효성 검사는 제공된 유형 및 제약 조건을 준수하는 모델을 구축하는 목적을 달성하기 위한 수단이다.
즉 pydantic은 입력 데이터가 아닌 출력모델의 유형과 제약 조건을 보장한다.
가령 float형으로 들어와야 할 데이터가 str으로 들어와도 float으로 parsing해준다.
하지만 parsing이 불가능한 데이터가 들어왔을 경우에는 error를 발생시킨다.
"""
app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")  # "/" 경로로 HTTP requests(GET)를 받는다.
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")  # "/items/{item_id}" 경로로 HTTP requests(GET)를 받는다.
def read_item(
    item_id: int, q: Union[str, None] = None
):  # 그떄 int 타입인 item_id가 매개변수로 필요하다.
    # q는 optional. optional은 =None으로 선언된다.
    return {"item_id": item_id, "q": q}


"""
1. 서버 가동 : uvicorn main:app --reload
2. 페이지 접속 : http://127.0.0.1:8000/items/5?q=somequery
3. 확인 가능 : {"item_id":5,"q":"somequery"}
4. 쿼리스트링으로 아무것도 안 날리면 (-> http://127.0.0.1:8000/items/5)
5. 그냥 {"item_id":5,"q":null}이라고 null로 뜸.
"""

"""
http://127.0.0.1:8000/docs 가면 swagger가 자동으로 만들어져 있다.
http://127.0.0.1:8000/redoc -> ReDoc
"""


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):  # 걍 타입 힌팅인데 더 복잡한 모델을 쓰려면 class를 활용한다.
    return {"item_name": item.name, "item_id": item_id}
