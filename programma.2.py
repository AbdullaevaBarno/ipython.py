import pygame
import random
import sys

# Pygame 
pygame.init()
ayna_kenligi, ayna_biyikligi = 800, 600
ayna = pygame.display.set_mode((ayna_kenligi, ayna_biyikligi))
pygame.display.set_caption("Tabiyatti asraw missiyasi")

# Renlar
aq = (255, 255, 255)
qara = (0, 0, 0)
jasil = (0, 255, 0)
qizil = (255, 0, 0)
kok = (0, 0, 255)

# Textler ham font
font = pygame.font.Font(None, 36)

# Shigindilar ham qutilar
shigindi_turi = ["Plastik", "Qagaz", "Shiyshe"]
qutilar = {"Plastik": jasil, "Qagaz": qara, "Shiyshe": kok}

# Shigindi obyekti
class Shigindi:
    def __init__(self):
        self.tur = random.choice(shigindi_turi)  # Shigindi turi
        self.x = random.randint(100, ayna_kenligi - 100)  # Chiqindining boshlang'ich x koordinatasi
        self.y = -50  # Shigindining baslangish y koordinatasi
        self.tezlik = random.randint(3, 7)  # Shigindining tusiw tezligi

    def siz(self):
        text = font.render(self.tur, True, qara)
        ayna.blit(text, (self.x, self.y))

    def hareket(self):
        self.y += self.tezlik

# Oyinshi algan ballari
ball = 0
shigindi = Shigindi()  # Shigindi obyektin jaratiw

# Oyin baslaniwi
islewi = True
while islewi:
    ayna.fill(aq)

    # Qutilarni chizish
    pygame.draw.rect(ayna, jasil, (100, ayna_biyikligi - 100, 150, 100))
    pygame.draw.rect(ayna, qara, (300, ayna_biyikligi - 100, 150, 100))
    pygame.draw.rect(ayna, kok, (500, ayna_biyikligi - 100, 150, 100))

    # Quti nomlari
    ayna.blit(font.render("Plastik", True, aq), (120, ayna_biyikligi - 70))
    ayna.blit(font.render("Qagaz", True, aq), (320, ayna_biyikligi - 70))
    ayna.blit(font.render("Shiyshe", True, aq), (520, ayna_biyikligi - 70))

    # Shigindi siziw ham hareketleniw
    shigindi.siz()
    shigindi.hareket()

    # Shigindi tomenge barganda
    if shigindi.y > ayna_biyikligi:
        shigindi = Shigindi()  # Taza shigindi jaratiw

    # Klaviatura boshqaruvi
    knopkalar = pygame.key.get_pressed()
    if knopkalar[pygame.K_LEFT] and chiqindi.y > ayna_biyikligi - 150:
        if shigindi.tur == "Plastik" and 100 <= shigindi.x <= 250:
            ball += 10
            shigindi = Shigindi()  # Taza shigindi jaratiw
        else:
            ball -= 5
    elif knopkalar[pygame.K_DOWN] and shigindi.y > ayna_biyikligi - 150:
        if shigindi.tur == "Qagaz" and 300 <= shigindi.x <= 450:
            ball += 10
            shigindi = Shigindi()  # Taza shigindi jaratisw
        else:
            ball -= 5
    elif knopkalar[pygame.K_RIGHT] and shigindi.y > ayna_biyikligi - 150:
        if shigindi.tur == "Shiyshe" and 500 <= shigindi.x <= 650:
            ball += 10
            shigindi = Shigindi()  # Yangi chiqindi yaratish
        else:
            ball -= 5

    # Ballni ko'rsatish
    ball_text = font.render(f"Ball: {ball}", True, qara)
    ayna.blit(ball_text, (10, 10))

    # Oyindi janalaw
    pygame.display.flip()

    # Oyindi jabiw
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            islewi = False

pygame.quit()
sys.exit()