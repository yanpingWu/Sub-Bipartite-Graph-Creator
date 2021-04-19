# -*- coding: utf-8 -*-
# https://blog.csdn.net/luoye7422/article/details/41950937
from tarfile import open
# import bz2


def unpacker(data):
    archive = open(
        './datas_tar/download.tsv.{}.tar.bz2'.format(data), 'r:bz2')
    archive.debug = 0
    for tarinfo in archive:
        archive.extract(tarinfo, r'./datas_origin/')
    archive.close()
