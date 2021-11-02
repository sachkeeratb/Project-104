from collections import Counter
import csv

with open("HeightWeight.csv", newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
new_data = []
for i in range(len(file_data)):
    n_number = file_data[i][2]
    new_data.append(float(n_number))

data = Counter(new_data)
mode_data_range = {"75-85":0,"85-95":0,"95-105":0, "105-115": 0, "115-125": 0, "125-135": 0, "135-145": 0, "145-155": 0, "155-165": 0}
for weight,occurrence in data.items():
    if 75 < float(weight) < 85:
        mode_data_range["75-85"]+=occurrence
    elif 85 < float(weight) < 95:
        mode_data_range["85-95"]+=occurrence   
    elif 95 < float(weight) < 105:
        mode_data_range["95-105"]+=occurrence
    elif 105 < float(weight) < 115:
        mode_data_range["105-115"]+=occurrence
    elif 115 < float(weight) < 125:
        mode_data_range["115-125"]+=occurrence   
    elif 125 < float(weight) < 135:
        mode_data_range["125-135"]+=occurrence
    elif 135 < float(weight) < 145:
        mode_data_range["135-145"]+=occurrence
    elif 145 < float(weight) < 155:
        mode_data_range["145-155"]+=occurrence   
    elif 155 < float(weight) < 165:
        mode_data_range["155-165"]+=occurrence
    

mode_range,mode_occurrence = 0,0
for range,occurrence in mode_data_range.items():
    if occurrence > mode_occurrence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurrence

mode = float((mode_range[0]+mode_range[1])/2)

print(f"Mode is -> {mode:2f}")