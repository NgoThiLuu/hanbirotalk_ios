import time, json, random
import logging
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from random import choice
from random import randint
import re
from sys import exit
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
import pathlib
from pathlib import Path
import os
from sys import platform
import ios_hanbiro_talk_python_luungo
from ios_hanbiro_talk_python_luungo import execution_log, fail_log, error_log, Logging

def Luu_hanbiro_talk_android_linux_Execution():
    error_menu = []
    ios_hanbiro_talk_python_luungo.log_in_hanbiro_talk_android()
    
    #error_screenshot = []
    try:
        ios_hanbiro_talk_python_luungo.log_in_hanbiro_talk_android()
    except:
        Logging("Cannot continue execution")
        error_menu.append("android_hanbiro_talk_python_luungo.log_in_hanbiro_talk_android()")
    
    
    try:
        ios_hanbiro_talk_python_luungo.hanbiro_talk_android_organization()
    except:
        Logging("Cannot continue execution")
        error_menu.append("android_hanbiro_talk_python_luungo.hanbiro_talk_android_organization()")
    '''
    try: 
        ios_hanbiro_talk_python_luungo.hanbiro_talk_android_board()
    except:
        Logging("Cannot continue execution")
        error_menu.append("android_hanbiro_talk_python_luungo.hanbiro_talk_android_board()")

    try:
        ios_hanbiro_talk_python_luungo.whisper_hanbiro_talk_android()
    except:
        Logging("Cannot continue execution")
        error_menu.append("android_hanbiro_talk_python_luungo.whisper_hanbiro_talk_android()")


    luu_log = {
        "execution_log": execution_log,
        "fail_log": fail_log,
        "error_log": error_log,
        "error_menu": error_menu
    }

    return luu_log
'''
def Luu_hanbiro_talk_android_Execution():
    
    ios_hanbiro_talk_python_luungo.log_in_hanbiro_talk_ios()
    ios_hanbiro_talk_python_luungo.hanbiro_talk_ios_organization()
    ios_hanbiro_talk_python_luungo.hanbiro_talk_ios_board()
    ios_hanbiro_talk_python_luungo.whisper_hanbiro_talk_ios()
    


    luu_log = {
        "execution_log": execution_log,
        "fail_log": fail_log,
        "error_log": error_log
    }

    return luu_log
    

Luu_hanbiro_talk_android_Execution()

