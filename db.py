import os
import sqlite3

base_dir=os.path.dirname(__file__)
database=os.path.join(base_dir,'data.sqlite')

conn=sqlite3.connect(database)
print('****connection****')
print()
cursor=conn.cursor()
drop_sql='''
drop table if exists items;
'''

cursor.execute(drop_sql)
print('****drop table if exists items****')

create_sql='''--sql begin
    create table items(
    item_id integer primary key autoincrement,
    item_name string unique not null,
    price integer not null)
    '''
cursor.execute(create_sql)
print('****create table items****')

insert_sql='''--sql begin
    insert into items(item_name,price)
    values(?,?)
    '''

insert_data_list=[('dango',100),('nikuman',150),('udon',200)]
cursor.executemany(insert_sql,insert_data_list)
print('****insert data****')
conn.commit()

select_all_sql='''--sql begin
    select *from items
'''
cursor.execute(select_all_sql)
print('****get all data****')

data=cursor.fetchall()
print(data)

select_one_sql='''--sql begin
    select *from items where item_id=?
'''
id=3
cursor.execute(select_one_sql,(id,))
print('****get one data****')
data=cursor.fetchone()
print(data)

updata_sql='''--sql begin
    update items set price=? where item_id=?
    '''
price=500
id=1
cursor.execute(updata_sql,(price,id))
print('****update data****')

conn.commit()
cursor.execute(select_one_sql,(id,))
data=cursor.fetchone()
print('for confirm:',data)

delete_sql='''--sql begin
    delete from items where item_id=?
'''
id=3
cursor.execute(delete_sql,(id,))
print('****delete data****')
conn.commit()

cursor.execute(select_all_sql)
data=cursor.fetchall()
print('for confirm get all data:',data)

cursor.close()
conn.close()
print('finished')