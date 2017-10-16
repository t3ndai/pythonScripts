#!/usr/bin/env python3

from lxml import etree
from urllib.request import urlretrieve, urlopen
import time


parser = etree.HTMLParser()
team_url ='http://www.uefa.com/uefaeuro/season={}/teams/team={}/index.html'
season = 2016
teams = 57166,


def team_data(team):
    with urlopen(team_url.format(season, team)) as src:
        html_tree = etree.parse(src, parser)

    team_name = html_tree.find('.//h1[@class="team-name"]').text
    return team_name, html_tree.findall('.//li[@class="squad--team-player"]')


def player_data(p):
    pos = p.find('./span[@class="squad--player-role"]').text
    num = int(p.find('./span[@class="squad--player-num"]').text)
    name = p.find('.//span[@class="squad--player-name-name"]').text.strip()
    surname = p.find('.//span[@class="squad--player-name-surname"]').text.strip()
    pic_url = p.find('.//img[@class="picture"]').attrib['src']
    return name, surname, pos, num, pic_url


def save_image(url, file_name):
    urlretrieve(url, file_name)



if __name__ == '__main__':
    for team in teams:
        team_name, team_players = team_data(team)
        print('*** {} ***'.format(team_name))
        for player in team_players:
            name, surname, pos, num, pic = player_data(player)
            print('{:2}\t{} {}, {}\n\t{}'.format(num, name, surname, pos, pic))
            file_name = '{}_{}.jpg'.format(team_name, num)
            save_image(pic, file_name)
            time.sleep(0.3)