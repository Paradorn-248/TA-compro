dictionary = {'arm':['n','แขน'],'hello':['v','สวัสดี'],'beautiful':['adj','สวย'],'toilet':['n','ห้องน้ำ'],'kick':['v','เตะ'],'handsome':['adj','หล่อ']} #รับค่าว่าจะใส่dictionaryไรลงไปมั่ง แล้วแสดงว่าคำนั้นเปนn,v,adj

while 1:
    word = input("")
    if word == "0" :
        break
    if word not in dictionary.keys() :
        print("Word not in dictionary.")
        continue
    while 1 :
        op = input()
        if op == "1" : # ชนิดของคำนั้น
            print(dictionary[word][0])
            break
        elif op == "2" : #คำแปล
            print(dictionary[word][1])
            break
        else :
            print("Invalid option.")

# for i in dictionary.keys() :
#     print(i)
#     print(1)
#     print(i)
#     print(2)