from random import randrange
lst = [100,1000,10000]
for experiment in range(len(lst)):
    heads = tails = 0 
    for i in range(experiment):
        if (randrange(2)==0):
            heads = heads+1
        else:
            tails = tails+1
    print("experiment number = " , experiment)
    print("heads = ", heads ,"tails = " , tails)
    print( "the ratio of #heads,#tails is : " ,round(heads/tails,4))
    
            
    