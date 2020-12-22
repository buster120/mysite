from peewee import *

db = MySQLDatabase("spider",host="127.0.0.1",port=3306,user="root",password="123456")
class BaseModel(Model):
    class Meta:
        database=db


#设计数据表的时候有几个重要的点一定要注意!!!!
"""
char类型，要设置最大长度
对于无法设置最大长度的字段，可以设置为Text（但是效率没有charfield高）
设计表的时候 采集到的数据要尽量先做格式化处理
default和null=True。 默认null不能为true（即数据不能为空，也符合大部分内容标准，如作者，日期等）但也有数据可能为空，比如回复，此时就可以给它专门
                    标注default=0.他就允许有null值了
"""


class Good(BaseModel):
    id=IntegerField(primary_key=True,verbose_name="商品id") #verbose表示标注作用，跟#没啥区别
    name=CharField(max_length=500,verbose_name="商品名称")
    content=TextField(default="",verbose_name="商品描述")
    supplier=CharField(max_length=500) #供应商
    ggbz=TextField(default="",verbose_name="规格和包装")
    image_list=TextField(default="",verbose_name="商品的轮播图")
    comments_nums = IntegerField(default=0, verbose_name="评论数")
    has_image_comments_nums = IntegerField(default=0, verbose_name="晒图数")
    has_video_comments_nums = IntegerField(default=0, verbose_name="视频晒单数")
    has_add_comments_nums = IntegerField(default=0, verbose_name="追评数")
    well_comment_nums = IntegerField(default=0, verbose_name="好评数")
    middle_comments_nums = IntegerField(default=0, verbose_name="中评数")
    bad_comments_nums = IntegerField(default=0, verbose_name="差评数")



if __name__=="__main__":
    db.create_tables([Good])







