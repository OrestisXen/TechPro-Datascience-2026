import random

def getListWithRandoms(N=100000, mu=170, s=10):
   my_list=[]
   
   for i in range(N):
      # n = random.uniform(0,10)
      n = random.gauss(mu,s)
      my_list.append(n) 
   return my_list


if __name__=='__main__':
   list_of_randoms = getListWithRandoms()
   print(list_of_randoms)



