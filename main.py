from fastapi import FastAPI, File, Form, UploadFile

app = FastAPI()

# @app.get("/items/{item_id}")
# async def read_user_item(item_id: str, needy: str):


@app.post("/files/")
async def create_file(
                      file: bytes = File(), fileb: UploadFile = File(),token: str | None = None
                      ):
    return {
        "file_size": len(file),
        # "token": token,
        "fileb_content_type": fileb.content_type,
    }


# curl -X 'POST' \
#   'http://127.0.0.1:8000/files/?token=123' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: multipart/form-data' \
#   -F 'file=@scheme.txt;type=text/plain' \
#   -F 'fileb=@001.wav;type=audio/x-wav'
