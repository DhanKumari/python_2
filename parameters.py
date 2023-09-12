def func(p1, p2,*args, k ,**kwargs):
    print("positional-or- keywords   {}, {}".format(p1, p2))
    print(" var positional-or-     {}".format(args))
    print(" keywords .....  {}".format(k))
    print("var keywords    {}".format(kwargs))

func(1, 2, 3, 4, 5, k=6, key1=7, key2=8)