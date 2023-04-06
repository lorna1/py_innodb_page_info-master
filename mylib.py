# encoding=utf-8
import os
import include
import page.btree
from include import *
from page.btree import btree

VARIABLE_FIELD_COUNT = 1
NULL_FIELD_COUNT = 0


class myargv(object):
    def __init__(self, argv):
        self.argv = argv
        self.parms = {}
        self.tablespace = ''

    def parse_cmdline(self):
        argv = self.argv

        # 校验参数长度
        if len(argv) == 1:
            print(
                "Usage: python py_innodb_page_info.py [OPTIONS] tablespace_file")
            print("For more options, use python py_innodb_page_info.py -h")
            return 0
        while argv:
            if argv[0][0] == '-':
                if argv[0][1] == 'h':
                    self.parms[argv[0]] = ''
                    argv = argv[1:]
                    break
                if argv[0][1] == 'v':
                    self.parms[argv[0]] = ''
                    argv = argv[1:]
                else:
                    self.parms[argv[0]] = argv[1]
                    argv = argv[2:]
            else:
                self.tablespace = argv[0]
                argv = argv[1:]
        if '-h' in self.parms:
            print('Get InnoDB Page Info')
            print(
                'Usage: python py_innodb_page_info.py [OPTIONS] tablespace_file\n')
            print('The following options may be given as the first argument:')
            print('-h        help ')
            print('-o output put the result to file')
            print('-t number thread to anayle the tablespace file')
            print('-v        verbose mode')
            return 0
        return 1


def get_innodb_page_type(myargv):
    # r 从文件读取数据  b 读取二进制数据
    f = open(myargv.tablespace, 'rb')
    fsize = int(os.path.getsize(f.name)/INNODB_PAGE_SIZE)
    ret = {}
    for i in range(fsize):
        # 读取一个页的长度
        page = f.read(INNODB_PAGE_SIZE)
        # 数据页偏移量，取出数据页下标4 ~ 7数组
        page_offset = mach_read_from_n(page, FIL_PAGE_OFFSET, 4)
        # 数据页类型，取出数据页下标4 ~ 6数组
        page_type = mach_read_from_n(page, FIL_PAGE_TYPE, 2)
        if '-v' in myargv.parms:
            print("页偏移量 %s, page type <%s>" %
                  (page_offset, innodb_page_type[page_type]))

            # 深入拆解下B+ tree
            if page_type == '45bf':
                btree.parseBtree(page)

        if not page_type in ret:
            ret[page_type] = 1
        else:
            ret[page_type] = ret[page_type] + 1
    print("总页数: %d:" % fsize)
    for type in ret:
        print("%s: %s" % (innodb_page_type[type], ret[type]))
