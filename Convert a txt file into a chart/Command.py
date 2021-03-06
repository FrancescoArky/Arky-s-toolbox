#How to create a chart from a txt file

dataset_file = open('.......')  # open dataset

first = True
dataset = []
coulumn_index = []
for row in dataset_file:
    if first:
        coulumn_index = row.replace("\n", "").split("\t") 
        first = False #Through this command I will make sure that such command is only done for the first row
        continue

    dataset_row = row.split("\t")
    dataset_row[1:] = [float(i) for i in dataset_row[1:]] #I have converted in float terms all of the elements 
    # print(dataset_row)
    dataset.append(dataset_row)

dataset = pd.DataFrame(dataset)
dataset.columns = coulumn_index

X = dataset.iloc[:, 1:] #For the chart X I will take into consideration all of the columns and I will skip the first row
print(X)
