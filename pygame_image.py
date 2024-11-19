import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")  # 背景画像Surfaceを作成する
    bg_img2 = pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("fig/3.png")  # こうかとん画像Surafaceを作成する
    kk_img = pg.transform.flip(kk_img, True, False)  # こうかとんを左右反転させる
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed()
        print(key_lst[pg.K_UP], key_lst[pg.K_DOWN],
              key_lst[pg.K_LEFT], key_lst[pg.K_RIGHT])
    
        dx, dy = 0, 0
        
        if key_lst[pg.K_UP]:
            dy -= 1
            dx -= 1
        if key_lst[pg.K_DOWN]:
            dy += 1
            dx -= 1
        if key_lst[pg.K_LEFT]:
            dx -= 1
        if key_lst[pg.K_RIGHT]:
            dx += 1
        if dx == 0 and dy == 0:
            dx = -1
        kk_rct.move_ip(dx, dy)

        x = -(tmr%3200)
        screen.blit(bg_img,  [x, 0])
        screen.blit(bg_img2, [x+1600, 0])
        screen.blit(bg_img,  [x+3200, 0])
        screen.blit(bg_img2, [x+4800, 0])
        screen.blit(kk_img, kk_rct)  # screen Surfaceにこうかとん画像Surfaceを貼り付ける
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()