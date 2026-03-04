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
