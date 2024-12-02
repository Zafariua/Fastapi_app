import json
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse


router = APIRouter(tags=['Search by keyword'])
@router.get('/get', response_class=HTMLResponse)
def get_page(query: str = None):
    if query:
        path = "src\\api\\cve.json"
        with open(path,"r") as file:
            cve_dict = json.load(file)
            cve_dict_parsed = {}
            count = 0
            for i in cve_dict["vulnerabilities"]:
                
                if query in i["shortDescription"]:
                    
                    cve_dict_parsed[count] = {"CVEID": i["cveID"], "vulnerabilityName":i["vulnerabilityName"]}
                    count += 1       
        return JSONResponse(content=cve_dict_parsed)
            
        
    return '''
    <html>

        <head>
        <title> Fastapiapp </title> 
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
        <h1><p align="center"> Available pages </p>
        <p> Links: </p></h1>
        <p><a href="http://127.0.0.1:8000/get-all"> CVE for the last 5 days </a></p>
        <p><a href="http://127.0.0.1:8000/get-new"> 10 most recent CVE </a></p>
        <p><a href="http://127.0.0.1:8000/get-known"> Known CVE </a></p>
        <p><a href="http://127.0.0.1:8000/get?query=CHANGE_IT"> Search CVE with keywords </a></p>
        </head>
        <body>
                
        </body>


    </html>
    '''