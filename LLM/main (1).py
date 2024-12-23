from fastapi import FastAPI, Form, Request
from typing_extensions import Annotated
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn
from sqlalchemy import create_engine


app = FastAPI()

# Static 파일 경로 설정 (배경 이미지 등)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Jinja2 템플릿 설정
templates = Jinja2Templates(directory="templates")

#db연결
db_connection = create_engine("mysql://root:root@127.0.0.1:3306/test?charset=utf8mb4")

# 환자 데이터 예시
query = 'SELECT * FROM `patient`'
patient_list = db_connection.execute(query)
print(patient_list,'1')
patient_list = patient_list.fetchall()
print(patient_list,'2')

@app.get("/")
def main_page(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})

# 환자 목록 라우트
@app.get("/patient/list")
def patient_list(request: Request):
    # return templates.TemplateResponse("index.html", {"request": request, "patients": patients})
    return templates.TemplateResponse("patient_list.html", {"request": request})

#환자 상세정보 페이지(좌측의 3d모델링, 우측은 정보/reference/소견서)
@app.get("/patient")
def patient_detail(request:Request,id:str):
    return templates.TemaplateResponse("patient.html",{"request":request, 'id':id})

@app.get("/reference")
def reference_list(request:Request):
    query = "SELECT * FROM `reference`"
    data = db_connection.execute(query)
    data = data.fetchall()
    result = []
    print(data)
    # for d in data:
    #     # temp = {'title':data[1], 'author': data[2], 'image_path': data[3], ''}
    #     print(d)
    #     #temp변수에 playerid, playername을 저장하는데, 0,1인 이유는 db선언할때 첫번째 두번째로해서
    #     # result.append(temp)
    #     #result변수에 id, name저장
    return templates.TemplateResponse("reference_list.html",{"request":request})



# 서버 실행 (uvicorn 실행 포함)
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
