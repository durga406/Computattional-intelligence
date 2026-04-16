import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, f1_score, recall_score

print("--- Ensemble Classifier ---")
n_est = int(input("Enter n_estimators (e.g., 100): "))
crit = input("Enter criterion (gini/entropy): ")

data = load_breast_cancer()
X, y = data.data, data.target

split_ratios = [0.30, 0.40, 0.25]
split_names = ["70-30", "60-40", "75-25"]
final_results = []

for i in range(len(split_ratios)):
    print("\n" + "="*40)
    print(f"Scenario: {split_names[i]}")

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=split_ratios[i], random_state=42)

    print(f"Train Samples: {len(X_train)}")
    print(f"Test Samples:  {len(X_test)}")
    print("-" * 30)

    rf = RandomForestClassifier(n_estimators=n_est, criterion=crit, random_state=42)

    rf.fit(X_train, y_train)
    y_pred = rf.predict(X_test)

    cm = confusion_matrix(y_test, y_pred)
    acc = round(accuracy_score(y_test, y_pred), 4)
    pre = round(precision_score(y_test, y_pred), 4)
    rec = round(recall_score(y_test, y_pred), 4)
    f1  = round(f1_score(y_test, y_pred), 4)


    print(f"{'':<15} Predicted 0    Predicted 1")
    print(f"Actual 0 {'':<5} {cm[0][0]:<14} {cm[0][1]:<14}")
    print(f"Actual 1 {'':<5} {cm[1][0]:<14} {cm[1][1]:<14}")

    final_results.append([split_names[i], acc, pre, rec, f1, cm[1][1], cm[0][0], cm[0][1], cm[1][0]])

cols = ["Split", "Accuracy", "Precision", "Recall", "F1", "TP", "TN", "FP", "FN"]
print("\n" + "="*95)
print("                       FINAL PERFORMANCE SUMMARY")
print("="*95)
summary_df = pd.DataFrame(final_results, columns=cols)
print(summary_df.to_string(index=False))

