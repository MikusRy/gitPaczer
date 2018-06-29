
def DictBuilder(JSON: dict):
    temp = {}
    temp["fullName"] = JSON["full_name"]
    temp["description"] = JSON["description"]
    temp["cloneUrl"] = JSON["clone_url"]
    temp["stars"] = JSON["stargazers_count"]
    temp["createdAt"] = JSON["created_at"]

    return temp
