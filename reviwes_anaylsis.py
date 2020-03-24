data = []
count = 0
with open('reviews.txt','r') as f:
    for line in f:
        data.append(line) #將每一行存進data裡面
        count += 1 #count = count + 1
        if count % 1000 == 0: #count 每1000筆印一次，也就是整除1000餘數是0，%是求餘數
            print(len(data)) #讀取進度
print('檔案讀取完了，總共讀取了', len(data),'筆資料')

sum_len = 0
for datas in data:
    sum_len += len(datas) #sum_lene = sum_len +len(datas)
avg = sum_len / len(data) #平均長度
print(avg)
