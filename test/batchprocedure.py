#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: longbai 
@ __file__: batchprocedure.py
@ __mtime__: 2016/9/9 17:42

"""


def main():
    myprocedure = """
DELIMITER //
CREATE PROCEDURE dsj_{}_{}()
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE userid VARCHAR(5);
    DECLARE file_exist CONDITION FOR 1086;
    DECLARE thread_null CONDITION FOR 1064;
    DECLARE userinfo CURSOR FOR SELECT distinct a.author_id from {}.{} a,user_temp.user_temp_0801 b where a.author_id=b.userid and a.is_del = 0;
    DECLARE CONTINUE HANDLER FOR SQLSTATE '02000' SET done = 1;
    DECLARE CONTINUE HANDLER FOR file_exist SET done = 1;
    DECLARE CONTINUE HANDLER FOR 1329 SET done=1;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done=1;
    DECLARE EXIT HANDLER FOR thread_null SET done = 1; -- file exists, continue next
    OPEN userinfo;
    REPEAT
        FETCH NEXT FROM userinfo INTO userid;
        IF(done <= 0) THEN
            SET @file = concat('/data/dsj/',userid,'{}','.html');
            SET @outsql = concat('SELECT create_time,title,content into outfile ','\\'',@file,'\\'',' from  {}.{} where is_del = 0 and author_id = ','\\'',userid,'\\'');
            PREPARE stmt FROM @outsql;
            EXECUTE stmt;
            DEALLOCATE PREPARE stmt;
            SET done = 0;
        END IF;
    UNTIL done = 1 END REPEAT;
    CLOSE userinfo;
END //
    """

    # mydb = ["money"]
    mydb = ["lady", "money", "news", "product", "spt"]
    for db in mydb:
        with open(db + ".txt", "r") as f:
            for line in f:
                boardid, dbname = line.strip().split("=")
                threadtable = boardid + "_thread"
                with open(db + ".sql", mode="a") as fq:
                    fq.writelines(myprocedure.format(dbname, boardid, dbname, threadtable, boardid, dbname, threadtable))
                with open(db + "_call.sql", mode="a") as fc:
                    fc.writelines("call dsj_{}.{}();".format(dbname, boardid))


if __name__ == "__main__":
    main()
