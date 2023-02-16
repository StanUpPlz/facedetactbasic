import random 

# กำหนด Seed 
random.seed(10)

# กำหนดจำนวนผู้รับบริการ
size = 10

# กำหนดลำดับผู้รับบริการ
customer = [i for i in range(1,size+1)]

# ระยะห่างของการมาถึงของผู้รับบริการแต่ละคน 
inter_arrival_time = [random.randrange(1,10) for i in range(size)]

# เวลาในการให้บริการแต่ละคน
service_time = [random.randrange(1,10) for i in range(size)]

print(len(inter_arrival_time),len(service_time))

# เวลาของการมาถึงของแต่ละคน
arrival_time = [0 for i in range(size)]

# กำหนดเวลาเริ่มต้นระบบ
arrival_time[0] = inter_arrival_time[0]

for i in range(1,size):
  arrival_time[i] = inter_arrival_time[i]+arrival_time[i-1]
 

Time_Service_Begin = [0 for i in range(size)]
Time_Customer_Waiting_in_Queue = [0 for i in range(size)]
Time_Service_Ends = [0 for i in range(size)]
Time_Customer_Spend_in_System = [0 for i in range(size)]
System_ideal = [0 for i in range(size)]

Time_Service_Begin[0] = arrival_time[0]
Time_Service_Ends[0] = service_time[0]
Time_Customer_Spend_in_System[0] = service_time[0]
for i in range(1,size):

  # เริ่มรับบริการ 
  Time_Service_Begin[i] = max(arrival_time[i],Time_Service_Ends[i-1])

  # เวลาที่ต้องคอย   
  Time_Customer_Waiting_in_Queue[i] = Time_Service_Begin[i]-arrival_time[i]

  # การบริการแล้วเสร็จ
  Time_Service_Ends[i] = Time_Service_Begin[i] + service_time[i]  

  # เวลาที่ต้องใช่ในระบบ คอย + รับบริการ
  Time_Customer_Spend_in_System[i] = Time_Service_Ends[i] - arrival_time[i]

  # เวลาที่ผู้ให้บริการว่างงาน
  if (arrival_time[i]>Time_Service_Ends[i-1]):
    System_ideal[i] = arrival_time[i]-Time_Service_Ends[i-1]
  else:
    System_ideal[i] = 0 

print(Time_Service_Begin)
print(Time_Customer_Waiting_in_Queue)
print(Time_Service_Ends)
print(Time_Customer_Spend_in_System)



