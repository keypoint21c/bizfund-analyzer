import re

def parse_business_info(text):

    company = re.search(r"상호[: ]*(.*)", text)
    owner = re.search(r"성명[: ]*(.*)", text)
    business_type = re.search(r"업태[: ]*(.*)", text)
    item = re.search(r"종목[: ]*(.*)", text)

    result = {
        "company": company.group(1) if company else "",
        "owner": owner.group(1) if owner else "",
        "type": business_type.group(1) if business_type else "",
        "item": item.group(1) if item else ""
    }

    return result
def recommend_funds(info):

    industry = info["item"]

    funds = []

    if "재생" in industry or "재활용" in industry:
        funds.append({
            "name":"환경부 자원순환 사업",
            "site":"https://www.bizinfo.go.kr"
        })

    if "제조" in info["type"]:
        funds.append({
            "name":"중진공 정책자금",
            "site":"https://www.kosmes.or.kr"
        })

    funds.append({
        "name":"지자체 중소기업 육성자금",
        "site":"https://www.bizinfo.go.kr"
    })

    return funds
