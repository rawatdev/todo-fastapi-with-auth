from urllib import response
from fastapi import FastAPI, Request, Depends
import models
from database import engine
from routers import auth, todos
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(auth.router)
app.include_router(todos.router)


@app.get("/", response_class=HTMLResponse)
def home_page(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.get("/register", response_class=HTMLResponse)
def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@app.get("/edit", response_class=HTMLResponse)
@app.get("/edit/{todo_id}", response_class=HTMLResponse)
def edit_page(request: Request, todo_id: int | None = None):
    return templates.TemplateResponse("edit-todo.html", {"request": request})


@app.get("/add", response_class=HTMLResponse)
def add_page(request: Request):
    return templates.TemplateResponse("add-todo.html", {"request": request})


@app.get("/password", response_class=HTMLResponse)
def password_page(request: Request):
    return templates.TemplateResponse("edit-user-password.html", {"request": request})
