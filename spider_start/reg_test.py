import re

#提取字符串
#替换
#搜索
#
# info='姓名:bobby 生日:1987年10月1日 本科:2005年9月1日'
# #
# # # print(re.findall('\d{4}',info))
# # match_result=re.match('.*生日.*?(\d{4}).*(\d{4})',info)
# # print(match_result.group(1))
# # print(match_result.group(2))
# # # print(re.search('生日.*?\d{4}',info))
#
# result=re.sub('\d{4}','2019',info)
# print(result)

name='my naem is bobby'
print(re.search('bobby',name).group())