import time

def bmi(weight, height):
   return weight/((height/100)**2)

def bmi_list(weight_list, height_list):
   N = len(weight_list)
   result_list = []
   for i in range(N):
      x = bmi(weight_list[i], height_list[i])
      result_list.append(x)
   return result_list

def main(w,h):
   start_seconds = time.time()
   
   bmis = bmi_list(w,h)
   # print(bmis)

   end_seconds = time.time()

   elapsed_sec = end_seconds - start_seconds
   print(f"{elapsed_sec} seconds elapsed")

if __name__=='__main__':
   h = [170,180,160]
   w = [80,90,100]
   main(w,h)

