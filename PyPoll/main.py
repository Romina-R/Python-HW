import os
import csv
import statistics

voterID = []
county = []
candidate = []

PyPollHW = os.path.join("Resources", "election_data.csv")

with open(PyPollHW, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        voterID.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
    totalvotes = len(voterID)

    khanvotes = 0
    for row in candidate:
        if row == "Khan":
            khanvotes += 1
    percentkhan = round(khanvotes/totalvotes*100, 3)

    correyvotes = 0
    for row in candidate:
        if row == "Correy":
            correyvotes += 1
    percentcorrey = round(correyvotes/totalvotes*100, 3)

    livotes = 0
    for row in candidate:
        if row == "Li":
            livotes += 1
    percentli = round(livotes/totalvotes*100, 3)

    otooleyvotes = 0
    for row in candidate:
        if row == "O'Tooley":
            otooleyvotes += 1
    percentotooley = round(otooleyvotes/totalvotes*100, 3)

allvotes = [khanvotes, correyvotes, livotes, otooleyvotes]
mostvotes = max(allvotes)
mostvotes_index = allvotes.index(mostvotes)



#--------------------PRINT-----------------------------
print("Election Results")
print("-----------------------------")
print(f"Total votes: {totalvotes}")
print("-----------------------------")
print(f"Khan: {percentkhan}% ({khanvotes})")
print(f"Correy: {percentcorrey}% ({correyvotes})")
print(f"Li: {percentli}% ({livotes})")
print(f"O'Tooley: {percentotooley}% ({otooleyvotes})")
print("-----------------------------")
print(f"Winner: {allvotes[mostvotes_index]}")
print("-----------------------------")

#-------------------WRITE--------------------------------

output_file = os.path.join("RR_Pypoll_output_file.txt")

with open(output_file, "w", newline="") as textfile:


    textfile.write("Election Results")
    textfile.write("-----------------------------")
    textfile.write(f"Total votes: {totalvotes}")
    textfile.write("-----------------------------")
    textfile.write(f"Khan: {percentkhan}% ({khanvotes})")
    textfile.write(f"Correy: {percentcorrey}% ({correyvotes})")
    textfile.write(f"Li: {percentli}% ({livotes})")
    textfile.write(f"O'Tooley: {percentotooley}% ({otooleyvotes})")
    textfile.write("-----------------------------")
    textfile.write(f"Winner: {allvotes[mostvotes_index]}")
    textfile.write("-----------------------------")
