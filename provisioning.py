"""
Author1: Girisha Daggula
Author2: Lalitha Sri Chennapragada
Date: 27/09/2024
Description: The following program imitates a cloud resource provisioning system. 
The number of CPU cores and the amount of memory required in GB will be provided by the user.
The below program will determine whether there are sufficient resources available or not. 
Displays the result either as remaining resources available or as provisioning failed and provisioning successfully.
"""
#Declarations
Total_CPU_Cores = 12
Total_Memory_GB = 32.0
Selected_CPU_Cores = 0
Selected_Memory_GB = 0
while True:
 Selected_CPU_Cores = int(input("Enter the number of CPU Cores required: "))
 Selected_Memory_GB = float(input("Enter the amount of memory required in GB: "))
 print(f"cpu cores: {Selected_CPU_Cores}, Memory: {Selected_Memory_GB}")
 if(Selected_CPU_Cores <= 0 or Selected_Memory_GB <= 0):
    print("Invalid input. Please Enter a positive integer:")
 else:
    break
      
# condition
if(Selected_CPU_Cores <= 12 and Selected_Memory_GB <= 32):
     print(" Resources Provisioned Successfully")
     Remaining_CPU_Cores = Total_CPU_Cores - Selected_CPU_Cores
     Remaining_Memory_GB = Total_Memory_GB - Selected_Memory_GB
     
else:
     print(" Resource request exceeds capacity. Provisioning failed")
     Remaining_CPU_Cores = Total_CPU_Cores 
     Remaining_Memory_GB = Total_Memory_GB 
     
    
print(f"Remaining CPU Cores: {Remaining_CPU_Cores}")
print(f"Remaining Memory GB: {Remaining_Memory_GB}")   


    
