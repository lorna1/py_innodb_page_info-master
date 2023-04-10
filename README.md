# py_innodb_page_info Python 分析 idb 文件工具

> python tool for innodb page info

- 兼容 mysql 8
- 添加中文标注
- v 显示帮助

```
> py_innodb_page_info.py varchar_length_test.ibd -v

页偏移量 00000000, page type <【文件头】File Space Header>
页偏移量 00000001, page type <【Insert Buffer位图】Insert Buffer Bitmap>
页偏移量 00000002, page type <【索引节点】File Segment inode>
页偏移量 00000003, page type <【表结构元数据信息】Tablespace SDI Index page>
页偏移量 00000004, page type <【B+树叶子节点】B-tree Node>
     ==== PAGE HEADER ====
     [  0-2  ]页目录(稀疏索引) slots个数:<2>
     [  2-4  ]第一个记录的指针:<00b1>
     [  4-6  ]堆中的记录个数:<32772>
     [  6-8  ]指向可重用记录指针:<0000>
     [  8-10 ]已删除的记录的字节数:<0>
     [ 10-12 ]最后插入记录的位置:<009c>
     [ 12-14 ]最后插入记录的方向:<0002>
     [ 14-16 ]一个方向连续插入记录的数量:<0>
     [ 16-18 ]该页中记录的数量:<2>
     [ 18-26 ]当前页最大事务ID:<0000000000000000>
     [ 26-28 ]页level:<0>
     [ 28-36 ]索引ID(当前页属于哪个索引):<00000000000000ad>
     [ 36-46 ]b+树非叶节点所在段的segment header:<0000000c0000000201b2>
     [ 46-56 ]b+树，叶节点所在段的segment header:<0000000c0000000201b2>
     ==== INF SUPRE ====
     [  0-13  ]:<b'\x01\x00\x02\x00\x1cinfimum\x00'>
页偏移量 00000005, page type <【B+树叶子节点】B-tree Node>
     ==== PAGE HEADER ====
     [  0-2  ]页目录(稀疏索引) slots个数:<2>
     [  2-4  ]第一个记录的指针:<00b1>
     [  4-6  ]堆中的记录个数:<32772>
     [  6-8  ]指向可重用记录指针:<0000>
     [  8-10 ]已删除的记录的字节数:<0>
     [ 10-12 ]最后插入记录的位置:<009c>
     [ 12-14 ]最后插入记录的方向:<0002>
     [ 14-16 ]一个方向连续插入记录的数量:<0>
     [ 16-18 ]该页中记录的数量:<2>
     [ 18-26 ]当前页最大事务ID:<0000000000000000>
     [ 26-28 ]页level:<0>
     [ 28-36 ]索引ID(当前页属于哪个索引):<00000000000000ad>
     [ 36-46 ]b+树非叶节点所在段的segment header:<00000000000000000000>
     [ 46-56 ]b+树，叶节点所在段的segment header:<00000000000000000000>
     ==== INF SUPRE ====
     [  0-13  ]:<b'\x01\x00\x02\x00\x1cinfimum\x00'>
页偏移量 00000000, page type <【新分配页】Freshly Allocated Page>
总页数: 7:
【文件头】File Space Header: 1
【Insert Buffer位图】Insert Buffer Bitmap: 1
【索引节点】File Segment inode: 1
【表结构元数据信息】Tablespace SDI Index page: 1
【B+树叶子节点】B-tree Node: 2
【新分配页】Freshly Allocated Page: 1
```
