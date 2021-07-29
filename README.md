# nmap2db
将nmap -oG扫描结果存入sqlite数据库

## 用法

1. 运行`python initdb.py`创建数据库
2. 将`nmap -oG`生成的结果保存为scanresult.txt
3. 运行`python nmap2db.py`将结果导入数据库
4. 使用sqlite查询