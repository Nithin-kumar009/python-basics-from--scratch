from random import choice,choices
enames=["nithin","ravi","ramu","santosh"]
luck_ename=choice(enames)
print(luck_ename)

luck_draw_list=choices(enames,k=2)
print(luck_draw_list)