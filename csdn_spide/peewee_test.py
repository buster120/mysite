from peewee import *

db = MySQLDatabase("spider",host="127.0.0.1",port=3306,user="root",password="123456")

class Person(Model):
    name = CharField(max_length=20)
    birthday = DateField()

    class Meta:
        database = db # This model uses the "people.db" database.
        # table_name="users"


if __name__== "__main__":
    # db.create_tables([Person])
    from datetime import date

    # #生成数据
    # uncle_bob=Person(name='Bob',birthday=date(1960,1,16))
    # uncle_bob.save()

    #查询数据(只能获取一条数据，即符合条件的第一条数据）
    # grandma=Person.get(Person.name=='Bob')  #取不到数据会抛异常
    # print(grandma.birthday)
    name=Person.select().where(Person.name=='Bob')  #从第二个符合条件的开始显示，取不到数据不会抛异常
    for i in name:
        # print(i.name,i.id,i.birthday)  #显示表的数据
        # i.birthday=date(1960,1,17)
        # i.save()    #在没有数据存在的时候新增数据，存在的时候修改表的数据
        i.delete_instance()
