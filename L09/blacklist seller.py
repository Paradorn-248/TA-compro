import json

def read_json(filename):
    with open(filename) as f:
        data = f.read()
        data = json.loads(data)
    print(data)
    return data

def check(datas, data):
    for i in range(len(datas)):
        if data in datas[i].values():
            print("Found in blacklist")
            for j in datas[i].keys():
                print(f'{j} : {datas[i][j]}')
            return
    print('Not found in blacklist')

filename = input("Filename : ")
datas = read_json(filename)
data = input("Data : ")
check(datas,data)
