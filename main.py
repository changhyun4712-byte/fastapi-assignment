from fastapi import FastAPI
from pydantic import BaseModel  
import json

app = FastAPI()

JSON_FILENAME = "courses.json"

class Course(BaseModel):
    course_name: str
    year: str
    semester: str
    grade: str

@app.get("/")
def read_root():
    return {"message": "수강기록 API 서버가 준비되었습니다."}

@app.get("/courses")
def get_courses():
    with open(JSON_FILENAME, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

@app.post("/courses")
def add_course(course: Course):
    
    with open(JSON_FILENAME, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    data.append(course.dict())
    
    with open(JSON_FILENAME, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    return {"message": "성공적으로 추가되었습니다."}