#############################
# Star Wars Spoilers
# by RestlessPuppet
# 12/24/19
#
# inspired by https://twitter.com/abt_programming/status/1207391893014925314
# original source: https://xkcd.com/2243/
#############################

import pygame
from pygame.locals import *
import random

pygame.init()
screen = pygame.display.set_mode([800, 600])

a = [
    "Kyle Ren,",
    "Malloc,",
    "Darth Sebelius,",
    "Theranos,",
    "Lord Juul,"
]
b = [
    "Kim Spacemeasurer.",
    "Teen Yoda.",
    "Dab Tweetdeck.",
    "Yaz Progestin.",
    "TI-83."
]
c = [
    " beige",
    "n ochre",
    " mauve",
    "n aquamarine",
    " taupe"
]
d = [
    "Sun Obliterator,",
    "Moonsquisher,",
    "World Eater,",
    "Planet Zester,",
    "Superconducting Superconductor,"
]
e = [
    "blowing up a planet with a bunch of\nbeams of energy that combine into one.",
    "blowing up a bunch of planets with\none beam of energy that splits into many.",
    "cutting a planet in half and smashing\nthe halves together like two cymbals.",
    "increasing the CO2 levels in a planet's\natmosphere, causing rapid heating.",
    "triggering the end credits\nbefore the movie is done."
]
f = [
    "Boba Fett,",
    "Salacious Crumb,",
    "the space slug,",
    "the bottom half of Darth Maul,",
    "Youtube commenters,"
]
g = [
    "a bow that shoots little\nlightsaber-headed arrows.",
    "X-Wings and Tie Fighters dodging\nthe giant letters of the opening crawl.",
    "a Sith educational display that uses\nforce lightning to demonstrate the dielectric breakdown of air.",
    "Kylo Ren putting on another\nhelmet over his smaller one.",
    "a Sith carwash where the bristles\non the brushes are little lightsabers."
]
h = [
    "Luke",
    "Leia",
    "Han",
    "Obi-Wan",
    "a random junk trader"
]
i = [
    "Poe.",
    "BB-8.",
    "Amilyn Holdo.",
    "Laura Dern.",
    "a random junk trader.",
    "that one droid from the jawa\nsandcrawler that says 'gonk'."]

static_txt1 = "In this Star Wars movie,\nour heroes return to take\non the First Order and\nnew villain,"
static_txt2 = "with the help from their\nnew friend,"
static_txt3 = "Rey builds a new lightsaber\nwith a"
static_txt4 = "blade,\nand they head out to confront\nthe First Order's new superweapon,\nthe"
static_txt5 = "a space station capable of"
static_txt6 = "They unexpectedly join forces\nwith their old enemy,"
static_txt7 = "and destroy the superweapon\nin a battle featurning"
static_txt8 = "P.S. Rey's parents are"
static_txt9 = "and"

block1 = static_txt1 + " " + random.choice(a) + "\n" + static_txt2 + " " + random.choice(b) + '\n\n'

block2 = static_txt3 + random.choice(c) + " " + static_txt4 + " " + random.choice(
    d) + "\n" + static_txt5 + "\n" + random.choice(e) + '\n\n'

block3 = static_txt6 + "\n" + random.choice(f) + "\n" + static_txt7 + "\n" + random.choice(g) + '\n\n'

block4 = static_txt8 + "\n" + random.choice(h) + " " + static_txt9 + "\n" + random.choice(i) + '\n'

center_x, center_y = screen.get_rect().centerx, screen.get_rect().centery
yellow = (155, 155, 0)
green = (0, 255, 0)
txt_y = center_y + 40
txt_dy = .3

txt_string = block1 + '\n' + block2 + '\n' + block3 + '\n' + block4

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill(0)

    txt_y -= txt_dy
    txt_list = []
    pos_list = []
    i = 0

    font = pygame.font.SysFont('Courier', 30)
    for line in txt_string.split('\n'):
        msg = font.render(line, True, yellow)
        txt_list.append(msg)
        pos = msg.get_rect(center=(center_x, center_y + int(txt_y) + i * 30))
        pos_list.append(pos)
        i += 1

    for j in range(i):
        screen.blit(txt_list[j], pos_list[j])

    pygame.display.update()

pygame.quit()
