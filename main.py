from typing import Annotated
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/items/{id}")
async def read_item(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="item.html", context={"id": id}
    )

@app.get("/homepage")
async def homepage(request: Request):
    return templates.TemplateResponse(
        request=request, name="homepage.html", context={}
    )

def pretvori_uporabnisko_ime(abcdefg):
    rezultat = ""
    for crka in abcdefg:
        rezultat += crka + " - "
    return rezultat[:-3]

@app.post("/prijava/")
async def login(request: Request, fname: Annotated[str, Form()], lname: Annotated[str, Form()]):
    print(fname)
    print(lname)
    if fname == "admin" and lname == "admin":
        return templates.TemplateResponse(
        request=request, name="name_check.html", context={"pretvori": pretvori_uporabnisko_ime, "nečrkovano_ime": fname, "geslo": lname}
    )
    else:
        return RedirectResponse("https://www.rtvslo.si/")