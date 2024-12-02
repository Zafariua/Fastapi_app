import json
from fastapi import APIRouter



router = APIRouter(tags=['Last 10 cve'])
@router.get('/get-new')
def get_new():
    path = "src\\api\\cve.json"
    with open(path,"r") as file:
        cve_dict = json.load(file)
        cve_dict_parsed = {}
        count = 0
        for i in range(10):
                cve_dict_parsed[count] = {"CVEID": cve_dict["vulnerabilities"][i]["cveID"], "vulnerabilityName":cve_dict["vulnerabilities"][i]["vulnerabilityName"]}
                count += 1
        
    return cve_dict_parsed
            