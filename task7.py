list = [False,True]
for x in list:
   for y in list:
    for z in list:
        print ('x,y,z', x,y,z) 
        Left = not (x or y or z)
        Right = not x and not y and not z
        print ('Left', Left)
        print ('Right', Right)
        print ('Итог', Left==Right)