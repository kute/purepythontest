Command Doc
===========

#### Database URL

    dialect+driver://username:password@host:port/database
    
#### Mysql(python3 不支持MySQLdb)

    sandman2ctl 'mysql+pymysql://root:root@localhost:3306/test'
    
    命令行参数:
    1. -d  debug
    2. -p  port, default 5000
    3. -s  read only
    
- 访问某表的单条记录

    http://localhost:5000/{table_in_low_case}/{id_primary_key}
    
- 某表的全部记录

    http://localhost:5000/{table_in_low_case}/
    
- 分页查询

    1. 查询第N页的数据
    http://localhost:5000/{table_in_low_case}/?page=1
    2. 返回limit条数据(当有page参数时会忽略limit 参数)
    http://localhost:5000/{table_in_low_case}/?limit=2
   
- 过滤数据

    http://localhost:5000/{table_in_low_case}/?field_name=field_value
    
- 排序

    http://localhost:5000/{table_in_low_case}/?sort=field_name
    
- 添加一条新记录

    curl -X POST -d '{"userid": "f", "content": "f-content"}' -H "Content-Type: application/json" http://127.0.0.1:5000/user_post/

    1. 对于主键自增的情况,添加时不需要传递.
    2. 返回值: 201 Created 或者 400 Bad Request
    
- 删除记录

    curl -X DELETE http://localhost:5000/{table_in_low_case}/{id_primary_key}
    
- 更新记录

    curl -X PATCH -d '{"content": "f-content"}' -H "Content-Type: application/json" http://127.0.0.1:5000/{table_in_low_case}/{id_primary_key}


- 导出表记录

    http://localhost:5000/{table_in_low_case}/?export=True





