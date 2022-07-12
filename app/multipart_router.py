from fastapi import FastAPI, APIRouter, Form,UploadFile,File
from typing import Optional
from pydantic import BaseModel
from typing import List

multipart_router = APIRouter()


@multipart_router.post("/language")
async def language(name: str = Form(...), type: str = Form(...)):
    return {'name': name, 'type': type}


@multipart_router.post("/singleupload")
async def upload(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        with open(file.filename, 'wb') as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        await file.close()

    return {"message": f"Successfuly uploaded {file.filename}"}



@multipart_router.post("/multiupload")
async def upload(files: List[UploadFile] = File(...)):
    for file in files:
        try:
            contents = await file.read()
            with open(file.filename, 'wb') as f:
                f.write(contents)
        except Exception:
            return {"message": "There was an error uploading the file(s)"}
        finally:
            await file.close()
    return {"message": f"Successfuly uploaded {[file.filename for file in files]}"}