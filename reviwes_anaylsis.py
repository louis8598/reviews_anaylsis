data = []
count = 0
with open('reviews.txt','r') as f:
    for line in f:
        data.append(line) #將每一行存進data裡面
        count += 1 #count = count + 1
        if count % 1000 == 0: #count 每1000筆印一次，也就是整除1000餘數是0，%是求餘數
            print(count) #讀取進度
