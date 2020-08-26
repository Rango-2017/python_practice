
#实现最简单，图片效果稍差


import gvcode
s,v = gvcode.generate()
s.save('./%s.jpg' % v)