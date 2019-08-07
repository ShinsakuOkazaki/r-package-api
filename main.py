from fastapi import FastAPI
from pydantic import BaseModel
# from couchbase import LOCKMODE_WAIT
# from couchbase.bucket import Bucket
# from couchbase.cluster import Cluster, PasswordAuthenticator

USERPROFILE_DOC_TYPE = "userprofile"

class Submit(BaseModel):
    studentEmail: str
    hash: int
    assignmentID: str
    osType: str
    taskID: int
    answer: float
    grade: float

app = FastAPI()

@app.post("/submits")
async def create_submit(submit: Submit):
    return submit

    