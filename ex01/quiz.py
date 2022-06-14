import random
import time

def shutudai():
    d={}
    d["サザエの旦那の名前は？"]=["マスオ","ますお"]
    d["カツオの妹の名前は？"]=["ワカメ","わかめ"]
    d["タラオはカツオから見てどんな関係？"]=["甥","おい","甥っ子","おいっこ"]
    quiz=random.choice(list(d.items()))
    ans=kaito(quiz)
    if ans in quiz[1]:
        print("正解！")
    else:
        print("出直してこい")

def kaito(a):
    print(a[0])
    start=time.time()
    word=input("回答:")
    end=time.time()
    anstime=round(end-start,1)
    print(f"経過時間:{anstime}秒")
    return word

if __name__ == "__main__":
    shutudai()