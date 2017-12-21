#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/21 13:09
 
'''
import pymysql.cursors

connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='root',
                             port=3306,
                             db='51job',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


def insert_artist(artist_id, artist_name):
    with connection.cursor() as cursor:
        sql = "INSERT INTO artists (ARTIST_ID, ARTIST_NAME) VALUES (%s, %s)"
        cursor.execute(sql, (artist_id, artist_name))
    connection.commit()


def insert_album(album_id, artist_id, album_name):
    with connection.cursor() as cursor:
        sql = "INSERT INTO albums (ALBUM_ID, ARTIST_ID,ALBUM_NAME) VALUES (%s, %s, %s)"
        cursor.execute(sql, (album_id, artist_id, album_name))
    connection.commit()


# 获取所有歌手的 ID
def get_all_artist():
    with connection.cursor() as cursor:
        sql = "SELECT ARTIST_ID FROM artists ORDER BY ARTIST_ID"
        cursor.execute(sql, ())
        return cursor.fetchall()


def dis_connect():
    connection.close()
