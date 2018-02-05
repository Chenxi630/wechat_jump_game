# -*- coding: utf-8 -*-
import os
import sys
import subprocess


def get_PATH():
    global adb_PATH
    try:
        adb_PATH = 'adb'
        subprocess.Popen([adb_path], stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
        return adb_PATH
    except OSError:
        if os.name == 'nt':
            adb_PATH = os.path.join('Tools', "adb", 'adb.exe')
            try:
                subprocess.Popen(
                    [adb_PATH], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                return adb_PATH
            except OSError:
                pass
                return None
        print('请安装 ADB 及驱动并配置环境变量')
        sys.exit()
    return None


def run(command):
    adb_exec = get_PATH()
    command = '{} {}'.format(adb_exec, command)
    readObj = os.popen(command)
    output = readObj.read()
    readObj.close()
    return output
