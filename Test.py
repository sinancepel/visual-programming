from Blocks import *
import copy

# Collapse fully evaluable
x = PlusBlock()
a = IntBlock()
b = IntBlock()
y = PlusBlock()
a.add(3)
b.add(4)
x.add(a)
x.add(b)
y.add(a)
y.add(x)
n = y.collapse()
print n.evaluate()


# Collapse with only block missing args
g = PlusBlock()
h = PlusBlock()
w = IntBlock()
k = IntBlock()
w.add(9)
k.add(23)
g.add(h)
h.add(w)
h.add(k)
u = g.collapse()
c = IntBlock()
c.add(100)
u.add(c)
print u.evaluate()

# Collapse with only parents missing args
q2 = PlusBlock()
t2 = PlusBlock()
f2 = PlusBlock()
f2.add(q2)
f2.add(t2)
e2 = f2.collapse()
j1 = IntBlock()
j1.add(5)
j2 = IntBlock()
j2.add(6)
j3 = IntBlock()
j3.add(7)
j4 = IntBlock()
j4.add(8)
e2.add(j1)
e2.add(j2)
e2.add(j3)
e2.add(j4)
print e2.evaluate()


# Collapse with both parents and block missing args
q1 = PlusBlock()
f1 = PlusBlock()
f1.add(q1)
e1 = f1.collapse()
i1 = IntBlock()
i1.add(5)
i2 = IntBlock()
i2.add(6)
i3 = IntBlock()
i3.add(7)
e1.add(i1)
e1.add(i2)
e1.add(i3)
print e1.evaluate()