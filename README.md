基于python，用pyechart绘制简单的dashboard。

一个简单的例子

```python
import dashboard_pyechart as dp
from pyecharts import Bar

ds = dp.Dashboard(title='myfst',logo_img=r'C:\Users\Administrator\Desktop\logo.png',background_img=r'C:\Users\Administrator\Desktop\background.png')

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
bar = Bar("柱状图数据堆叠示例")
bar.add("商家A", attr, v1, is_stack=True)
bar.add("商家B", attr, v2, is_stack=True)

bar1 = Bar("柱状图数据堆叠示例")
bar1.add("商家A", attr, v1, is_stack=True)
bar1.add("商家B", attr, v2, is_stack=True)
bar2 = Bar("柱状图数据堆叠示例")
bar2.add("商家A", attr, v1, is_stack=True)
bar2.add("商家B", attr, v2, is_stack=True)

bar3 = Bar("柱状图数据堆叠示例")
bar3.add("商家A", attr, v1, is_stack=True)
bar3.add("商家B", attr, v2, is_stack=True)
bar4 = Bar("柱状图数据堆叠示例")
bar4.add("商家A", attr, v1, is_stack=True)
bar4.add("商家B", attr, v2, is_stack=True)

ds.add_chart(bar,'wodediyige chart')
ds.add_chart(bar1,'wodediyige chart')
ds.add_chart(bar2,'wodediyige chart')
ds.add_chart(bar3,'wodediyige chart')
ds.add_chart(bar4,'wodediyige chart')

ds.save()

```

