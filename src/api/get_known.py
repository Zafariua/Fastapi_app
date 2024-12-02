import json
from fastapi import APIRouter



router = APIRouter(tags=['Cve marked as known'])
@router.get('/get-known')
def get_knownl():
    path = "src\\api\\cve.json"
    with open(path,"r") as file:
        cve_dict = json.load(file)
        cve_dict_parsed = {}
        count = 0
        for i in cve_dict["vulnerabilities"]:
            if i["knownRansomwareCampaignUse"] == "Known" and count <=9:
                cve_dict_parsed[count] = {"CVEID": i["cveID"], "vulnerabilityName":i["vulnerabilityName"]}
                count += 1
    return cve_dict_parsed
            