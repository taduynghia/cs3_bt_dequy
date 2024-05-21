def extract_ids(lst):
    result = []
    
    def recurse(items):
        for item in items:
            result.append({"id": item["id"]})
            if item["value"]:
                recurse(item["value"])

    recurse(lst)
    return result
lstDemo = [
    {
        "id": 1,
        "value": [
            {
                "id": 2,
                "value": [
                    {
                        "id": 3,
                        "value": [
                            {
                                "id": 4,
                                "value": []
                            }
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": 5,
        "value": []
    }
]

#lstResult = [{"id": 1}, {"id": 2}, {"id": 3}, {"id": 4}, {"id": 5}]
# [1,2,3] + [4,5,6] => [1,2,3,4,5,6]
# extend()

# Kết quả mong muốn
lstResult = extract_ids(lstDemo)
print(lstResult)