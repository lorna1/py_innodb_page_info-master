# encoding=utf-8
INNODB_PAGE_SIZE = 16*1024*1024

# Start of the data on the page
FIL_PAGE_DATA = 38
FIL_PAGE_HEADER = 56

FIL_PAGE_OFFSET = 4  # page offset inside space
FIL_PAGE_TYPE = 24  # File page type

# Types of an undo log segment */
TRX_UNDO_INSERT = 1
TRX_UNDO_UPDATE = 2

# On a page of any file segment, data may be put starting from this offset
FSEG_PAGE_DATA = FIL_PAGE_DATA

# The offset of the undo log page header on pages of the undo log
TRX_UNDO_PAGE_HDR = FSEG_PAGE_DATA

PAGE_LEVEL = 26  # level of the node in an index tree; the leaf level is the level 0 */

innodb_page_type = {
    '0000': u'【新分配页】Freshly Allocated Page',
    '0002': u'【Undo页】Undo Log Page',
    '0003': u'【索引节点】File Segment inode',
    '0004': u'【Insert Buffer空闲列表】Insert Buffer Free List',
    '0005': u'【Insert Buffer位图】Insert Buffer Bitmap',
    '0006': u'【系统页】System Page',
    '0007': u'【事务系统数据】Transaction system Page',
    '0008': u'【文件头】File Space Header',
    '0009': u'【扩展描述页】extend description page',
    '000a': u'【Blob页】Uncompressed BLOB Page',
    '000b': u'【第一个压缩Blob页】1st compressed BLOB Page',
    '000c': u'【后续压缩的 BLOB 页】Subsequent compressed BLOB Page',
    '45bf': u'【B+树叶子节点】B-tree Node',
    '45bd': u'【表结构元数据信息】Tablespace SDI Index page',
    '45be': u'【R树节点】 R-tree node',
}

innodb_page_direction = {
    '0000': 'Unknown(0x0000)',
    '0001': 'Page Left',
    '0002': 'Page Right',
    '0003': 'Page Same Rec',
    '0004': 'Page Same Page',
    '0005': 'Page No Direction',
    'ffff': 'Unkown2(0xffff)'
}


INNODB_PAGE_SIZE = 1024*16  # InnoDB Page 16K


def mach_read_from_n(page, start_offset, length):
    # 从页中复制一份数据出来
    ret = page[start_offset:start_offset+length]
    return ret.hex()


def array_split(page, start_offset, length):
    # 从页中复制一份数据出来
    ret = page[start_offset:start_offset+length]
    return ret


def mach_read_convert_int(page, start_offset, length):
    # 拷贝数组并转换int
    ret = array_split(page, start_offset, length)
    return (int.from_bytes(ret, byteorder='big'))
