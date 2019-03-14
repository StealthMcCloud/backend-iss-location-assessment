#!/usr/bin/env python

import requests
import json
import time
import turtle


__author__ = 'Clinton Johnson'

def get_astronauts():
    r = requests.get('http://api.open-notify.org/astros.json')
    r = r.json()
    for people in r['people']:
        print people['name'] + ' inhabits spaceship ' + people['craft']
    print 'Total number of astronauts:', r['number']

def get_coordinates():
    r = requests.get('http://api.open-notify.org/iss-now.json')
    r = r.json()
    cur_time = r['timestamp']
    lat = r['iss_position']['latitude']
    lon = r['iss_position']['longitude']
    convert_time = time.strftime(
        "%D %H:%M", time.localtime((int(cur_time))))
    print ('Date & Time: {}, Latitude: {}, Longitude: {}'.format(
        convert_time, lat, lon))
    return (lon, lat)

def show_iss_location():
    lon, lat = get_coordinates()
    screen = turtle.Screen()
    screen.register_shape('./iss.gif')
    screen.setup(width=720, height=360, startx=0, starty=0)
    screen.bgpic('./map.gif')
    screen.setworldcoordinates(-180, -90, 180, 90)
    iss = turtle.Turtle()

    iss.shape('./iss.gif')
    iss.penup()
    print(lon, lat)
    iss.goto(float(lon), float(lat))
    draw_indy()
    turtle.done()

def draw_indy():
    indy_lat = 39.9784
    indy_lon = -89.1581
    data = {'lon': indy_lon, 'lat': indy_lat}
    r = requests.get('http://api.open-notify.org/iss-pass.json', params=data)
    r = r.json()
    timestamp = r['response'][0]['risetime']
    timestamp = time.strftime(
        "%D %H:%M", time.localtime((int(timestamp))))
    print(timestamp)
    indy = turtle.Turtle()
    indy.shape('circle')
    indy.color('yellow')
    indy.turtlesize(.5, .5, .5)
    indy.penup()
    indy.goto(indy_lon, indy_lat)
    indy.write(timestamp, move=False, align='left',
               font=('Arial', 8, 'normal'))
    indy.pendown()


def main():
    get_astronauts()
    get_coordinates()
    show_iss_location()


if __name__ == '__main__':
    main()
