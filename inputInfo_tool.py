#!/usr/bin/python2
# -*- coding:UTF-8 -*-
from yaml import dump
from yaml import load
from yaml import warnings
from os import getcwd
from os import listdir
from os import mkdir
from os import path
from json import dumps
from binascii import b2a_hex


def WriterFile():
    YamlDict = {}
    i = 0
    j = 1
    while i >= 0:
        YamlDict['VC{0}'.format(i)] = {'name': str(input('请输入VC相应的Name地址:')),
                                       'host': str(input('请输入VC相应的Host地址:')),
                                       'user': str(input('请输入VC相应的User名称:')),
                                       'pass': b2a_hex(input('请输入VC相应的Pass密码:').encode()),
                                       }
        ESXi_Input = input('是否需要输入ESXi的账户信息(y|n):')
        if ESXi_Input == 'y':
            while j >= i:
                YamlDict['VC{0}'.format(i)]['ESXi{0}'.format(j)] = {'host': str(input('请输入ESXi相应的Host地址:')),
                                                                    'user': str(input('请输入ESXi相应的User名称:')),
                                                                    'pass': b2a_hex(input('请输入ESXi相应的Pass密码:').encode())
                                                                    }
                ESXi_Str = input('是否继续输入ESXi账户信息(y|n):')
                j += 1
                if ESXi_Str == 'n':
                    break
                else:
                    continue
        strIf = input('记录是否完成输入(y|n):')
        i += 1
        if strIf == 'y':
            break
        else:
            continue
    with open('Conf\Account.yml', 'w') as f:
        dump(YamlDict, f)


def main():
    path_str = getcwd()
    if 'Conf' in listdir(getcwd()):
        WriterFile()
    else:
        mkdir(path_str + 'Conf/')
        WriterFile()
    if len(listdir('Conf/')) == 1 and listdir('Conf/')[0] == 'Account.yml':
        configName = 'Conf/Account.yml'
        configFile = path.join(path.dirname(path.abspath(__file__)), configName)
        warnings({'YAMLLoadWarning': False})
        config = load(open(configFile))
        print(dumps(config, indent=len(config.keys())))


if __name__ == '__main__':
    main()
