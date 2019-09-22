#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python
# coding: utf-8

# 1.กำหนดให้ month = ["Jan","May","Jul","Aug","Oct","Dec"]
# 1.1ให้เขียนคำสั่งโปรแกรมเรียกใช้เมธอด แทรกเดือนที่ขาดหายไป
# 1.2ให้เขียนคำสั่งโปรแกรมเรียกใช้เมธอด ลบชื่อเดือนตำแหน่งที่ 2,5,9 ออกจากลิสต์
# 1.3ให้เขียนคำสั่งโปรแกรมเรียกใช้เมธอด แสดงชื่อเดือนที่เหลืออยู่ในลิสต์

# In[130]:


month=["Jan","May","Jul","Aug","Oct","Dec"]
month.insert(1,"Feb")
month.insert(2,"Mar")
month.insert(3,"Apr")
month.insert(5,"Jun")
month.insert(8,"Sep")
month.insert(10,"Nov")
print("แทรกเดือนที่ขาดหายไป =",month)
month.remove("Feb")
month.remove("May")
month.remove("Sep")
print("ลบชื่อเดือนตำแหน่งที่ 2,5,9 ออกจากลิสต์ =",month)
print("แสดงชื่อเดือนที่เหลืออยู่ในลิสต์ =",month)


# 2.กำหนดให้ days = ["Sun","Mon","Tuel","Wed","Thu","Fri","Sat"]
# 2.1ให้เขียนคำสั่งโปรแกรมเรียกใช้เมธอด เรียงชื่อวันจากท้ายสุด
# 2.2ให้เขียนคำสั่งโปรแกรมเรียกใช้เมธอด เรียงลำดับชื่อวันตามตัวอักษร
# 2.3ให้เขียนคำสั่งโปรแกรมแสดงชื่อวันในตำแหน่งที่ 3,5 และ 7

# In[132]:


days = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
days.reverse()
print("เรียงชื่อวันจากท้ายสุด =",days)
days.sort()
print("เรียงลำดับชื่อวันตามตัวอักษร =",days)
print("แสดงชื่อวันในตำแหน่งที่ 3,5 และ 7 =",days[2:7:2])


# In[ ]:




