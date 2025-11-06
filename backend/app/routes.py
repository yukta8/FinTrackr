from fastapi import APIRouter,UploadFile, File , Depends, HTTPException
from sqlmodel import Session
import pandas as pd
from app.db import get_session
from app.models import Transaction
from datetime import datetime

router=APIRouter()

@router.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...), session: Session=Depends(get_session)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="File extension not supported, Please upload a csv file!")

    contents = await file.read()
    df = pd.read_csv(pd.io.common.BytesIO(contents))

    

