import json

def toy():
    slackdeets = {"slackUsername": "string", "backend": "Boolean", "age": "INTEGER", "bio":"String"}
    json_slackdeet = json.dumps(slackdeets)
    print(json_slackdeet)
    print('na wa')



