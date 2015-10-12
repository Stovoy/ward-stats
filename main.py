from __future__ import unicode_literals

import os.path

import video
import stills
import preprocessing
import cutting
import processing

import gui


class Game(object):
    def __init__(self, blue_team, red_team, match_description, url):
        self.blue_team = blue_team
        self.red_team = red_team
        self.match_description = match_description
        self.video_url = url
        self.title = '%s vs %s - %s' % (self.blue_team, self.red_team, self.match_description)

    # Collection of methods to tell if a given step is done.
    # This allows a step to be redone if the folder is deleted.

    def video_done(self):
        return os.path.isfile('videos/%s.mkv' % self) or os.path.isfile('videos/%s.mp4' % self)

    def stills_done(self):
        return (os.path.isdir('stills/%s' % self) and
                os.path.isdir('stills/%s/raw' % self))

    def preprocessing_done(self):
        return (os.path.isdir('stills/%s' % self) and
                os.path.isdir('stills/%s/preprocessed' % self))

    def cutting_done(self):
        return (os.path.isdir('stills/%s' % self) and
                os.path.isdir('stills/%s/cut' % self))

    def processing_done(self):
        return os.path.isdir('processed/%s' % self)

    def __str__(self):
        return self.title

# Game information scraped from
# https://www.reddit.com/r/LoLeventVoDs/comments/3n2brl/season_5_world_championship_2015/
# Thanks to the LoL Event VOD team for curating such great data!
games = [
    # Day 1, Thursday - October 1st
    Game('FNC', 'iG', 'Group B - Day 1', 'https://www.youtube.com/watch?v=-3N4zhdmXpw'),
    Game('C9', 'AHQ', 'Group B - Day 1', 'https://www.youtube.com/watch?v=tZd4z-RkuOg'),
    Game('SKT', 'H2K', 'Group C - Day 1', 'https://www.youtube.com/watch?v=Ob-ay2KSMnc'),
    Game('EDG', 'BKT', 'Group C - Day 1', 'https://www.youtube.com/watch?v=vtQQQZGQA4k'),
    Game('CLG', 'FW', 'Group A - Day 1', 'https://www.youtube.com/watch?v=pOJPHFR4UyI'),
    Game('PNG', 'KOO', 'Group A - Day 1', 'https://www.youtube.com/watch?v=sVYmzGkwlxg'),

    # Day 2, Friday - October 2nd
    Game('KT', 'TSM', 'Group D - Day 2', 'https://www.youtube.com/watch?v=WyRThDMvnj8'),
    Game('LGD', 'OG', 'Group D - Day 2', 'https://www.youtube.com/watch?v=mH7cUnHs5II'),
    Game('BK2', 'SKT', 'Group C - Day 2', 'https://www.youtube.com/watch?v=zsudemCAfus'),
    Game('H2K', 'EDG', 'Group C - Day 2', 'https://www.youtube.com/watch?v=rdZetUueG7Q'),
    Game('FW', 'KOO', 'Group A - Day 2', 'https://www.youtube.com/watch?v=pScP7qfG6es'),
    Game('CLG', 'PNG', 'Group A - Day 2', 'https://www.youtube.com/watch?v=itBNufSBt0I'),

    # Day 3, Saturday - October 3rd
    Game('EDG', 'SKT', 'Group C - Day 3', 'https://www.youtube.com/watch?v=a1mpiTLE80c'),
    Game('H2K', 'BKT', 'Group C - Day 3', 'https://www.youtube.com/watch?v=CwqJ1KOM9bQ'),
    Game('LGD', 'KT', 'Group D - Day 3', 'https://www.youtube.com/watch?v=Va8Zr4BpSbk'),
    Game('OG', 'TSM', 'Group D - Day 3', 'https://www.youtube.com/watch?v=sgIZ-rnEAtE'),
    Game('iG', 'C9', 'Group B - Day 3', 'https://www.youtube.com/watch?v=b1H1aiaqvNM'),
    Game('AHQ', 'FNC', 'Group B - Day 3', 'https://www.youtube.com/watch?v=8cLIHt3USG4'),

    # Day 4, Sunday - October 4th
    Game('TSM', 'LGD', 'Group D - Day 4', 'https://www.youtube.com/watch?v=fDpLoTUwaK8'),
    Game('KT', 'OG', 'Group D - Day 4', 'https://www.youtube.com/watch?v=mIUGPTuhk-w'),
    Game('iG', 'AHQ', 'Group B - Day 4', 'https://www.youtube.com/watch?v=A6ats7nDums'),
    Game('C9', 'FNC', 'Group B - Day 4', 'https://www.youtube.com/watch?v=MSsiVsuzQMQ'),
    Game('KOO', 'CLG', 'Group A - Day 4', 'https://www.youtube.com/watch?v=8R6HZx8yUGE'),
    Game('PNG', 'FW', 'Group A - Day 4', 'https://www.youtube.com/watch?v=GXAlC4BQ5_E'),
]

# Extracting ward data from a game is a 5 step process.
# Step 1: Download the video.
# Step 2: Break it up into still images taken at 3 second intervals.
# Step 3: Remove all images that do not correspond to the game.
# Step 4: Cut out minimap & corresponding game timer images.
# Step 5: For each pair of images, find all wards for each team and the game time.
# These steps are named: video, stills, preprocessing, cutting, processing

if __name__ == '__main__':
    for game in games:
        print game

        print
        print 'Step 1 - Video...'
        if game.video_done():
            print 'Done'
        else:
            video.download(game.video_url, game.title)

        print
        print 'Step 2 - Stills...'
        if game.stills_done():
            print 'Done'
        else:
            stills.generate_stills(game.title)

        print
        print 'Step 3 - Preprocessing...'
        if game.preprocessing_done():
            print 'Done'

        print
        print 'Step 4 - Cutting...'
        if game.cutting_done():
            print 'Done'

        print
        print 'Step 5 - Processing...'
        if game.processing_done():
            print 'Done'

    # gui.launch()
