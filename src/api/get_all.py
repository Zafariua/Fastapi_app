import json
from fastapi import APIRouter



router = APIRouter(tags=['for the last 5 days'])
@router.get('/get-all')
def get_all():
    path = "src\\api\\cve.json"
    with open(path,"r") as file:
        cve_dict = json.load(file)
        cve_dict_parsed = {}
        count = 0
        dates = ["2024-11-27", "2024-11-26", "2024-11-25", "2024-11-24", "2024-11-23"]
        for i in cve_dict["vulnerabilities"]:
            if i["dateAdded"] not in dates or count >= 40:
                break
            else:
                cve_dict_parsed[count] = {"CVEID": i["cveID"], "vulnerabilityName":i["vulnerabilityName"]}
                count += 1
    return cve_dict_parsed
            