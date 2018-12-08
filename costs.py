import SimParameters as SP


infrastructure = 189190.15
equipment_donation = 327868.66
acquired_equipment = 39126.21
equipment_supplies = 288742.45
education_training = float(58175) + float(67961)

print(infrastructure)
print(equipment_donation)
print(acquired_equipment)
print(equipment_supplies)
print(education_training)


total = float(infrastructure) + float(equipment_donation) + float(acquired_equipment) + float(equipment_supplies) + float(education_training)

OpSmile_C = total                    # Cost of Operation Smile Project Implementation
OS_Surgery_C = 0                # Cost of Surgery with OpSmile
OS_NoSurgery_C = 0                  # Cost of No surgery with OpSmile
#NoOpSmile
NoOS_C = 0                         # Cost of No Operation Smile Project Implementation
NoOS_Surgery_C = 0                # Cost of NoOpSmile Surgery
NoOS_NoSurgery_C = 0               # Cost no surgery without OpSmile

print(total)
