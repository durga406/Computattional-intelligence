import csv
import math
import random
def load_data(filename, sample_size=150):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader, None) 
        for row in reader:
            if len(row) == 0: continue
            features = list(map(float, row[:-1]))
            label = row[-1]
            data.append((features, label))
    return random.sample(data, min(len(data), sample_size))
def normalize_dataset(data):
    dim = len(data[0][0])
    mins = [min(row[0][i] for row in data) for i in range(dim)]
    maxs = [max(row[0][i] for row in data) for i in range(dim)]
    norm_data = []
    for features, label in data:
        norm_feat = []
        for i in range(dim):
            if maxs[i] == mins[i]: norm_feat.append(0)
            else: norm_feat.append((features[i] - mins[i]) / (maxs[i] - mins[i]))
        norm_data.append((features, norm_feat, label))
    return norm_data, mins, maxs
def normalize_query(query, mins, maxs):
    return [(query[i] - mins[i]) / (maxs[i] - mins[i]) if maxs[i] != mins[i] else 0 for i in range(len(query))]
def distance_metrics(train, query, method):
    results = []
    for orig, norm_feat, label in train:
        if method == "euclidean":
            d = math.sqrt(sum((a - b)**2 for a, b in zip(norm_feat, query)))
        else:
            d = sum(abs(a - b) for a, b in zip(norm_feat, query))
        results.append({'features': orig, 'dist': d, 'label': label})
    return results
def voting(neighbors, vote_type):
    count, weight = {}, {}
    for item in neighbors:
        label, dist = item['label'], item['dist']
        count[label] = count.get(label, 0) + 1
        weight[label] = weight.get(label, 0) + 1 / (dist + 1e-9)
    print("\nMajority Count:", count)
    print("Weighted Scores:", {k: round(v, 4) for k, v in weight.items()})
    return max(weight, key=weight.get) if vote_type == "weighted" else max(count, key=count.get)
print("NEAREST NEIGHBOR MODEL - TRANSFUSION DATASET")
print("---DATASET DESCRIPTION---")
print("F1:RECENCY  (months since last donation)")
print("F2:FREQUNCY (total number of donations)")
print("F3:MONETARY (total blood donated)")
print("F4:TIME (months since first donation)")
data = load_data("transfusion.data")
norm_data, mins, maxs = normalize_dataset(data)
dim = len(data[0][0])
print("\nEnter Test Features:")
test = [float(input(f"f{i+1}: ")) for i in range(dim)]
norm_test = normalize_query(test, mins, maxs)
method = input("\nMethod (euclideiian/manhattan): ").lower()
if method not in ["euclidean", "manhattan"]: method = "euclidean"
results = distance_metrics(norm_data, norm_test, method)
sorted_by_dist = sorted(results, key=lambda x: x['dist'])
for rank, item in enumerate(sorted_by_dist, start=1):
    item['rank'] = rank 
print(f"\n{'Features':<35} | {'Class':<5} | {'Distance':<10} | {'Rank'}")
print("-" * 70)
for item in results:
    print(f"{str(item['features']):<35} | {item['label']:<5} | {round(item['dist'], 4):<10} | {item['rank']}")
k = int(input("\nEnter K value: "))
top_k = sorted_by_dist[:k]
print(f"\nTop {k} Neighbors (Sorted for Voting):")
print(f"{'Features':<35} | {'Class':<5} | {'Distance':<10} | {'Rank'}")
print("-" * 70)
for item in top_k:
    print(f"{str(item['features']):<35} | {item['label']:<5} | {round(item['dist'], 4):<10} | {item['rank']}")
vote_type = input("\nVoting (majority/weighted): ").lower()
prediction = voting(top_k, vote_type)
print("\nFinal Prediction:", prediction)


