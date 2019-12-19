import os
import random
from utils import *

DATA_ROOT = r'/data1/scusenyang/shentao/competitions/FaceAntiSpoofing/data/CASIA-CeFA/phase1'
TRN_IMGS_DIR = DATA_ROOT + '/Training/'
TST_IMGS_DIR = DATA_ROOT + '/Val/'

RESIZE_SIZE = 112

def load_train_valid_list(e_index = 1):
    train_list = []
    valid_list = []

    f = open(DATA_ROOT + '/4@'+str(e_index)+'_train.txt')
    lines = f.readlines()

    for line in lines:
        line = line.strip().split(' ')
        folder = line[0].split('/')[1]
        id = int(folder.split('_')[1])

        info = [line[0],line[0].replace('profile','ir'),line[0].replace('profile','depth'),line[1]]

        if id <180 and id >=0:
            train_list.append(info)
        else:
            valid_list.append(info)

    return train_list, valid_list

def load_all_train_valid_list():
    train_list_1, valid_list_1 = load_train_valid_list(e_index=1)
    train_list_2, valid_list_2 = load_train_valid_list(e_index=2)
    train_list_3, valid_list_3 = load_train_valid_list(e_index=3)

    train_list = train_list_1 + train_list_2 + train_list_3
    valid_list = valid_list_1 + valid_list_2 + valid_list_3

    # print(len(train_list))
    # print(len(valid_list))
    return train_list, valid_list

def load_test_list():
    list = []
    f = open(DATA_ROOT + '/test_public_list.txt')
    lines = f.readlines()

    for line in lines:
        line = line.strip().split(' ')
        list.append(line)

    return list

def transform_balance(train_list):
    print('balance!!!!!!!!')
    pos_list = []
    neg_list = []
    for tmp in train_list:
        if tmp[3]=='1':
            pos_list.append(tmp)
        else:
            neg_list.append(tmp)

    print(len(pos_list))
    print(len(neg_list))
    return [pos_list,neg_list]

if __name__ == '__main__':
    load_all_train_valid_list()






