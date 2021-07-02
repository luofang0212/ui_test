
#python自带包
import random  #随机数
import os   #路径和文件处理
import configparser  #读取配置文件信息
import logging  #日志模块
import time  # 时间


# 第三方库
import requests   #处理请求
import openpyxl   #处理.xlsx 结尾的excel
from clickhouse_driver import Client    #clickhouse数据库
import psycopg2   #pl数据库
import pymysql  #mysql数据库
from ddt import ddt, data, unpack, file_data  #ddt 数据驱动管理 一般结合unittest使用
import xlrd  #处理Excel的xlrd模块
import pandas  #高效处理数据 excel,主要用来做数据分析的
import selenium # web页面相关的操作 web自动化


# 邮件模块
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication