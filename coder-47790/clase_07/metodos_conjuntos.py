# xx = set([1, 2, 3])

# yy =  xx
# zz =  xx.copy()
# print("xx -> ", xx)
# print("yy -> ", yy)
# print("zz -> ", zz)
# xx.add(999999)
# print("xx -> ", xx)
# print("yy -> ", yy)
# print("zz -> ", zz)

# print("-" * 90)
# xx = {1, 2, 3}
# yy = {4, 5, 6}
# zz = {1, 2}
# print("xx, yy son disjuntos: ", xx.isdisjoint(yy))
# print("xx, zz son disjuntos: ", xx.isdisjoint(zz))

# print("-" * 90)
# xx = {1, 2, 3, 6}
# yy = {4, 5, 6}
# zz = {1, 2}
# print("zz es subconjunto de xx: ", zz.issubset(xx))
# print("yy es subconjunto de xx: ", yy.issubset(xx))

# print("-" * 90)
# xx = {1, 2, 3, 6}
# yy = {4, 5, 6}
# zz = {1, 2}
# print("xx contiene a xx: ", xx.issuperset(xx))
# print("xx contiene a yy: ", xx.issuperset(yy))
# print("xx contiene a zz: ", xx.issuperset(zz))

# print("-" * 90)
# xx = {1, 2, 3, 6}
# yy = {4, 5, 6}
# zz = {1, 2}
# print("xx union xx: ", xx.union(xx))
# print("xx union yy: ", xx.union(yy))
# print("xx union zz: ", xx.union(zz))

# print("-" * 90)
# xx = {1, 2, 3, 6}
# yy = {4, 5, 6}
# zz = {1, 2}
# print("xx diferencia con xx: ", xx.difference(xx))
# print("xx diferencia con yy: ", xx.difference(yy))
# print("xx diferencia con zz: ", xx - zz)


print("-" * 90)
xx = {1, 2, 3, 6}
yy = {4, 5, 6}
zz = {1, 2}
print("xx diferencia con xx: ", xx.difference_update(xx))
print(xx)
xx = {1, 2, 3, 6}
print("xx diferencia con yy: ", xx.difference_update(yy))
print(xx)
xx = {1, 2, 3, 6}
print("xx diferencia con zz: ", xx.difference_update(zz))
print(xx)

# print("-" * 90)
# xx = {1, 2, 3, 6}
# yy = {4, 5, 6}
# zz = {1, 2}
# print("xx interseccion con xx: ", xx.intersection(xx))
# print("xx no cambió: ",xx)
# print("\n")
# print("xx interseccion con yy: ", xx.intersection(yy))
# print("xx no cambió: ",xx)
# print("\n")
# print("xx interseccion con zz: ", xx.intersection(zz))
# print("xx no cambió: ",xx)
# print("\n")

# print("-" * 90)
# xx = {1, 2, 3, 6}
# yy = {4, 5, 6}
# zz = {1, 2}
# print("xx interseccion con xx: ", xx.intersection_update(xx))
# print("xx cambió: ",xx)
# print("\n")
# xx = {1, 2, 3, 6}
# print("xx interseccion con yy: ", xx.intersection_update(yy))
# print("xx cambió: ",xx)
# print("\n")
# xx = {1, 2, 3, 6}
# print("xx interseccion con zz: ", xx.intersection_update(zz))
# print("xx cambió: ",xx)
# print("\n")