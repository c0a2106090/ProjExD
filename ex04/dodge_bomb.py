import pygame as pg
import sys
       
def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen=pg.display.set_mode((1600,900))
    bg=pg.image.load("C:/Users/admin/Downloads/プロジェクト演習/ProjExD2022/ex04/pg_bg.jpg")
    rect_bg=bg.get_rect()
    clock=pg.time.Clock()
    clock.tick(1000)

    tori_img=pg.image.load("C:/Users/admin/Downloads/プロジェクト演習/ProjExD2022/ex03/fig/8.png")
    tori_img=pg.transform.rotozoom(tori_img,0,2.0)
    tori_rect=tori_img.get_rect()

    while True:
        screen.blit(bg,rect_bg)
        screen.blit(tori_img,tori_rect)
        pg.display.update() 

        for event in pg.event.get():#イベントキューからキーボードやマウスの動きを取得
            if event.type == pg.QUIT:      # 閉じるボタンが押されたら終了
                return

if __name__ == "__main__":
    pg.init() 
    main()
    pg.quit()           # Pygameの終了(ないと終われない)
    sys.exit()