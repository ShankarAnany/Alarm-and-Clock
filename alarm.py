# Timer & Clock
# By ShankarAnany
import pygame as pg
import sys
from datetime import datetime

pg.init()

# Beep Time
single_beep_time = int(input('Input Single Beep Interval(in sec): '))
triple_beep_time = int(input('Input Triple Beep Interval(in min): '))

# Display Settings
display = pg.display.set_mode((600, 300))
pg.display.set_caption('Timer & Clock')

font = pg.font.Font('JosefinSans-BoldItalic.ttf', 80)
font_small = pg.font.Font('JosefinSans-BoldItalic.ttf', 30)
single_beep = pg.mixer.Sound('zapsplat_single_beep.mp3')
triple_beep = pg.mixer.Sound('zapsplat_triple_beep.mp3')

# Start Time
start = datetime.now()

# lap Settings
lap_time = 0
laps = []


def lap():
    global hr, min, sec
    # hr: Timer hr, min: Timer min, sec: Timer sec
    prev_laps = 0
    for lap in laps:  # Time Of all prev laps added
        prev_laps += lap
    lap_time = ((hr * 3600) + (min * 60) + sec) - prev_laps  # Current lap time
    # Turn in to 60 base number
    lap_hr = lap_time // 3600
    lap_min = (lap_time % 3600) // 60
    lap_sec = (lap_time % 3600) % 60
    # add current lap to laps list
    laps.append(lap_time)
    print(f'Lap {len(laps)} - {lap_hr}:{lap_min}:{lap_sec}')


def timer_update():
    global now
    # Number of seconds in current time
    hr = int(now.strftime('%H'))
    min = (hr * 60) + int(now.strftime('%M'))
    sec = (min * 60) + int(now.strftime('%S'))

    # Single Beep or Triple beep
    if (sec - s_sec) != 0 and (sec - s_sec) % single_beep_time == 0:
        if (min - s_min) != 0 and (sec - s_sec) % (triple_beep_time * 60) == 0:
            triple_beep.play()
        else:
            single_beep.play()

    return (sec - s_sec)  # return number of seconds in timer


while True:
    display.fill((0, 0, 0))
    # Settings --------------------------------------
    s_hr = int(start.strftime('%H'))
    s_min = (s_hr * 60) + int(start.strftime('%M'))
    s_sec = (s_min * 60) + int(start.strftime('%S'))
    # Clock -----------------------------------------
    now = datetime.now()
    time = now.strftime('%H:%M:%S')

    time_surf = font.render(str(time), True, (255, 255, 255))
    time_rect = time_surf.get_rect(center=(180, 100))

    display.blit(time_surf, time_rect)
    # Timer -----------------------------------------
    timer_sec = timer_update()

    # Turn (timer_sec) into 60 Base Number
    hr = timer_sec // 3600 % 24
    min = (timer_sec % 3600) // 60
    sec = (timer_sec % 3600) % 60

    timer = f'{hr}:{min}:{sec}'

    timer_surf = font.render(str(timer), True, (10, 87, 201))
    timer_rect = timer_surf.get_rect(center=(180, 200))

    display.blit(timer_surf, timer_rect)
    # End Time --------------------------------------
    end_time = s_sec + (triple_beep_time * 60)
    e_hr = (end_time // 3600) % 24
    e_min = (end_time % 3600) // 60
    e_sec = (end_time % 3600) % 60
    end_time = f'{e_hr}:{e_min}:{e_sec}'

    end_time_surf = font_small.render(f'End: {end_time}', True, (170, 179, 13))
    end_rect = end_time_surf.get_rect(center=(450, 200))

    display.blit(end_time_surf, end_rect)
    # Start Time ------------------------------------
    s_hr = int(start.strftime('%H'))
    s_min = int(start.strftime('%M'))
    s_sec = int(start.strftime('%S'))
    start_time = f'{s_hr}:{s_min}:{s_sec}'

    start_time_surf = font_small.render(f'Start: {start_time}', True, (10, 87, 201))
    start_rect = start_time_surf.get_rect(center=(450, 100))

    display.blit(start_time_surf, start_rect)
    # Display Update --------------------------------
    pg.display.flip()
    # Events ----------------------------------------
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            lap()
# End -----------------------------------------------
