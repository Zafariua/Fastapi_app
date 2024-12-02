from api import info
from api import get
from api import get_all
from api import get_new
from api import get_known
from api import home_page
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()



app.include_router(info.router)
app.include_router(get.router)
app.include_router(get_all.router)
app.include_router(get_new.router)
app.include_router(get_known.router)
app.include_router(home_page.router)
app.mount("/", StaticFiles(directory="templates", html=True), name="templates")