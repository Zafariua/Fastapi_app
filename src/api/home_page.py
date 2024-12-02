from fastapi import APIRouter, status
from fastapi.responses import RedirectResponse



router = APIRouter(tags=['Home page'])
@router.get('/')
def redirect():
    return RedirectResponse("http://127.0.0.1:8000/home.html",status_code=status.HTTP_303_SEE_OTHER)