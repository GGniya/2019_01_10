# 1. 分析网址  岗位名称 页码
# https://search.51job.com/list/000000,000000,0000,00,9,99,岗位名称,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=
# https://search.51job.com/list/000000,000000,0000,00,9,99,岗位名称,2,2.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=
# 2. 获取所有页页码（字符串替换、正则）   字符串 -> 数字
# 共732页，到第
# str(数字)   int(字符串)
# 3. 采集数据
# 薪资：有可能不存在，则默认为"面议"
# 统一单位   8000-1000元/月   300元/天    300元/时
# 4. 数据存储   csv
# 5. 发邮件（选做）
# 6. 统计每天的工作数量  参考"统计单词数量"逻辑
# 7. 图表展示  pyecharts
# 汉字编码  gbk gb18030 gb2312