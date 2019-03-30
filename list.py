#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pygame.locals import *
import pygame
import sys

pygame.init()    # Pygameを初期化
screen = pygame.display.set_mode((300, 300))    # 画面を作成
pygame.display.set_caption("speeeeeeeeeeeece")    # タイトルを作成
img = pygame.image.load("neko.png").convert_alpha()
img_rect = img.get_rect()
img_rect.center = (100, 100)

vx = vy = 10  # キーを押したときの移動距離

while True:
    pygame.display.update()
    screen.fill((255, 255, 255))  # screenの色指定
    screen.blit(img, img_rect)  # 画像描写
    pygame.time.wait(30)        # 更新時間間隔

    for event in pygame.event.get():
        if event.type == QUIT: sys.exit(0)
        if event.type == KEYDOWN:  # キーを押したとき
            # ESCキーならスクリプトを終了
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit(0)
            else:
                print("押されたキー = " + pygame.key.name(event.key))
            
            # 矢印キーなら画像を移動
            if pressed_key == K_LEFT:
                img_rect.move_ip(-vx, 0)  
            if event.key == K_RIGHT:
                img_rect.move_ip(vx, 0)  
            if event.key == K_UP:
                img_rect.move_ip(0, -vy)  
            if event.key == K_DOWN:
                img_rect.move_ip(0, vy)  
        pygame.display.update()