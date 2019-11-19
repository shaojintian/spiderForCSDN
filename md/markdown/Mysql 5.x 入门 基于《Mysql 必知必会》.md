mysql 入门
虽然加黑字体在mysql命令行中大小写均可，但应该**大写**，这样更符合规范。

## 一：入门及检索语句

1：创建数据库  -> **create database**  database_name;

2:  加信息源 -> **source**  文件的绝对路径;

3：使用数据库 -> **use database** database_name ;

4: 展示选中库的所有表 -> **show tables;**

5: 展示所有表的其中一个 -> **describe table_name;**

6:选择某表中的某一列 -> **select**  column_name  **from** ** table_name**

7选择某表中的多列 -> **select**  column_name1 ,  column_name2 **from** ** 
table_name**

8:选择某表中的所有列 -> **select *  from** table_name ;


## 二：排序检索数据

使用子句**order by**
1: 按照某一列升序排序（默认为升序）：
	**select** column_name 
	**from** table_name 
	**order by**column_name;
	
2:降序排列：
	**select** column_name 
	**from** table_name 
	**order by** column_name **DESC**;
	
3:按某一列选中最大的item：
	**select** column_name 
	**from** table_name 
	**order by** column_name **DESC**
	**LIMIT** 1；//注释：mysql中也是第0个为第一个 LIMIT 1 等价于 LIMIT 0,1




