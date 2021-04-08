import re
pat_timu2 = ['2020年底前，各级人力资源社会保障部门全面开展线上线下人社政务服务"好差评"工作，实现（   ）全覆盖、（   ）全覆盖、（   ）全覆盖。\n']
pat_daan2 =['服务事项、评价对象、服务渠道']
len_kuohao = 0
for j in pat_timu2:
    pat_kuohao = "（   ）"
    pat_kuohao = re.compile(pat_kuohao, re.S).findall(j)
    len_kuohao = len(pat_kuohao)


print(len_kuohao)


for i in pat_daan2:
    if "；" in i:
        k = re.split(";", i)
    else:
        k = re.split("、|  | |；", i)
