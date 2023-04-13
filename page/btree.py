import include
from include import *


class btree():
    def parseBtree(page):
        # 解析页头信息
        btree.parsePageHeader(page)
        # 解析record信息
        first_record_offset = btree.parseInfimumAndSupreMumRecord(page)
        # 解析航记录
        btree.parseUserRecord(page,first_record_offset)
        return

    def parsePageHeader(page):
        # 页 header
        page_headers = array_split(page, FIL_PAGE_DATA, FIL_PAGE_HEADER)
        # 0~2 页目录 page directory slot槽个数
        page_directory_solts = mach_read_convert_int(page_headers, 0, 2)
        # 2~4 堆中第一个记录的指针
        page_heap_top = mach_read_from_n(page_headers, 2, 2)
        # 4~6 堆中的记录个数
        page_record_num = mach_read_convert_int(page_headers, 4, 2)
        # 6~8 指向可重用记录指针
        page_free = mach_read_from_n(page_headers, 6, 2)
        # 8~10 已删除的记录的字节数（delete flag=1的记录大小总数）
        page_grabage = mach_read_convert_int(page_headers, 8, 2)
        # 10-12 最后插入记录的位置
        page_last_insert = mach_read_from_n(page_headers, 10, 2)
        # 12-14 最后插入记录的方向
        page_direction = mach_read_from_n(page_headers, 12, 2)
        # 14-16 一个方向连续插入记录的数量
        page_n_direction = mach_read_convert_int(page_headers, 14, 2)
        # 16-18 该页中记录的数量
        page_n_recs = mach_read_convert_int(page_headers, 16, 2)
        # 18-26 当前页最大事务ID
        page_max_trx_id = mach_read_from_n(page_headers, 18, 8)
        # 26~28 页level
        page_level = mach_read_convert_int(page_headers, 26, 2)
        # 28~36 索引ID
        page_index_id = mach_read_from_n(page_headers, 28, 8)
        # 36~46 b+树非叶节点所在段的segment header
        page_btr_seg_leaf = mach_read_from_n(page_headers, 46, 10)
        # 46~56 b+树，叶节点所在段的segment header
        page_btr_seg_top = mach_read_from_n(page_headers, 46, 10)

        print("     ==== PAGE HEADER ==== ")
        print("     [  0-2  ]页目录(稀疏索引) slots个数:<%s>" % page_directory_solts)
        print("     [  2-4  ]第一个记录的指针:<%s>" % (page_heap_top))
        print("     [  4-6  ]堆中的记录个数:<%s>" % (page_record_num))
        print("     [  6-8  ]指向可重用记录指针:<%s>" % (page_free))
        print("     [  8-10 ]已删除的记录的字节数:<%s>" % (page_grabage))
        print("     [ 10-12 ]最后插入记录的位置:<%s>" % (page_last_insert))
        print("     [ 12-14 ]最后插入记录的方向:<%s>" % (page_direction))
        print("     [ 14-16 ]一个方向连续插入记录的数量:<%s>" % (page_n_direction))
        print("     [ 16-18 ]该页中记录的数量:<%s>" % (page_n_recs))
        print("     [ 18-26 ]当前页最大事务ID:<%s>" % (page_max_trx_id))
        print("     [ 26-28 ]页level:<%s>" % (page_level))
        print("     [ 28-36 ]索引ID(当前页属于哪个索引):<%s>" % (page_index_id))
        print("     [ 36-46 ]b+树非叶节点所在段的segment header:<%s>" %
              (page_btr_seg_leaf))
        print("     [ 46-56 ]b+树，叶节点所在段的segment header:<%s>" %
              (page_btr_seg_top))
        return

    def parseInfimumAndSupreMumRecord(page):
        # 页 header
        user_records = array_split(
            page, FIL_PAGE_DATA + FIL_PAGE_HEADER, len(page))

        # 第一条记录的位置
        # 第一个字节中包含
        # 预留位         1 bit
        # 预留位         1 bit
        # delete_flag   1 bit
        # min_rec_flag  1 bit
        # n_owned       4 bit

        # 第二三 字节
        # heap_no       13 bit 
        # record_type   3 bit
        page_no = array_split(user_records, 1, 2)
        # page_no_binary = bin(page_no.from_bytes(b'\x11', byteorder=sys.byteorder)) 
        for i in page_no:
            print(bin(i))
        # 第四五字节
        # next_record   16 bit
        page_next_record = mach_read_convert_int(user_records, 3, 2)
        # 69 6e 66 69 6d 75 6d 00 = infimum
        page_infimum = array_split(user_records, 0, 13)
        # 73 75 70 72 65 6d 75 6d = supremum
        page_supremum = array_split(user_records, 13, 13)
        print("     ==== INF SUPRE ==== ")
        # print("     [  1-3  ]头二进制:<%s>" % page_no_binary)
        print("     [  3-5  ]第一条记录的位置:<%s>" % page_next_record)
        print("     [  0-13  ]:<%s>" % page_infimum)
        print("     [  13-26  ]:<%s>" % page_supremum)
        return page_next_record
    
    
    def parseUserRecord(page,first_record_offset):
        # 页 header
        # 这里的 8  指的是infimum的单词的长度，记录的指针指向了header和record中间，所以这边是8而不是13。
        # 这里的 13 指的是supremum单词+header的长度。
        # infimum(8) + supremum(13) + n = 第一条记录的相对位置
        header_length = first_record_offset - 8 - 13

        # 记录头
        record_header = array_split(page, FIL_PAGE_DATA + FIL_PAGE_HEADER + 26, header_length)

        # 下一条记录的位置
        page_next_record = mach_read_convert_int(record_header, 3, 2)
        print("     ==== ROW RECORD ==== ")
        print("     [  -  ]下一条记录的偏移量位置:<%s>" % (page_next_record))
        print("     [  0-%s  ]记录头:<%s>" % (header_length,record_header))
        return