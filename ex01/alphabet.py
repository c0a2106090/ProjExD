import random
import time
misslen=3
cholen=8
start=time.time()

def alphagame():
    global misslis
    cholis=random.sample(lis,cholen)
    dislis=random.sample(cholis,cholen-misslen)
    choset=set(cholis)
    disset=set(dislis)
    missset=choset ^ disset
    misslis=list(missset)
    print("対象文字")
    print(' '.join(cholis))
    print("表示文字")
    print(' '.join(dislis))
    #print(misslis)
    kaito1()

def kaito1():
    word=int(input("欠損文字はいくつあるでしょうか"))
    if word==misslen:
        print("正解です。それでは、具体的に欠損文字を1つずつ入力してください")
        kaito2()
    else:
        print("不正解です。またチャレンジしてください")

def kaito2():
    global Fin
    Fin=False
    clear=0
    while clear<misslen:
        word2=input(f"{clear+1}つ目の文字を入力してください:")
        if word2 in misslis:
            misslis.remove(word2)
            clear+=1
        else:
            print("不正解です。またチャレンジしてください")
            break
        if clear==misslen:
            Fin=True
            print("正解！")
            

while True:
    lis=[]
    for i in range(65, 91):
        lis.append(chr(i))
    alphagame()
    if Fin==True:
        break

end=time.time()
anstime=round(end-start,1)
print(f"経過時間:{anstime}秒")