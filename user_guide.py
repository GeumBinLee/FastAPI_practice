from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel

"""
FastAPI는 Starlette을 상속한다.
Starlette는 비동기 웹 서비스를 구현하기 좋은 가벼운 ASGI framework/toolkit이다.
따라서 FastAPI는 Starlette의 기능도 사용할 수 있다.
"""
test = FastAPI()  # FastAPI 클래스의 인스턴스를 생성한다. 해당 인스턴스는 uviconr으로 서버를 켤 때 참고한다.


@test.get("/test")  # @FastAPi의인스턴스이름.메소드이름("/경로") 형식
# 아래 작성된 함수를 데코레이터의 인자로 받는다.
# 기본적인 GET / POST / DELETE / PUT 말고도 OPTIONS / HEAD / PATCH / TRACE 등이 존재한다.
async def root():  # 따로 await을 쓸 일이 없기 때문에 async 안 써도 된다.
    return {
        "message": "Hello World"
    }  # dict, list, str, int은 물론이고 Pydantic models도 반환할 수 있다.


"""
uvicorn user_guide:test --reload로 로컬 서버 접속
http://127.0.0.1:8000/test 경로로 들어가면 해당 반환값 {"message": "Hello World"} 확인 가능
http://127.0.0.1:8000/docs 스웨거 확인 가능
http://127.0.0.1:8000/redoc도 존재
"""
"""
요약
1. from fastapi import FastAPI
2. FastAPI 클래스의 인스턴스 생성하기
3. Write a path operation decorator (like @app.get("/")).
4. Write a path operation function (like def root(): ... above).
5. 서버 돌리기 (like uvicorn main:app --reload).
"""


# 미리 정의된(predefined) value를 사용하고 싶을 때는 Enum 클래스를 사용한다.
from enum import Enum


class ModelName(str, Enum):  # value의 타입은 string으로 고정
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None

#     class Config:
#         schema_extra = {
#             "example": {
#                 "name": "Foo",
#                 "description": "A very nice Item",
#                 "price": 35.4,
#                 "tax": 3.2,
#             }
#         }


# @test.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results


class Item2(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@test.put("/items/{item_id}")
async def update_item2(
    *,
    item_id: int,
    item: Annotated[
        Item2,
        Body(
            examples={
                "normal": {
                    "summary": "A normal example",
                    "description": "A **normal** item works correctly.",
                    "value": {
                        "name": "Foo",
                        "description": "A very nice Item",
                        "price": 35.4,
                        "tax": 3.2,
                    },
                },
                "converted": {
                    "summary": "An example with converted data",
                    "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                    "value": {
                        "name": "Bar",
                        "price": "35.4",
                    },
                },
                "invalid": {
                    "summary": "Invalid data is rejected with an error",
                    "value": {
                        "name": "Baz",
                        "price": "thirty five point four",
                    },
                },
            },
        ),
    ],
):
    results = {"item_id": item_id, "item": item}
    return results
