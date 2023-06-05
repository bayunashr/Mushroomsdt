import pandas as pd
import category_encoders as ce
import warnings
# import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
# from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

warnings.filterwarnings('ignore')

data = 'mushrooms.csv'
df = pd.read_csv(data)

col_names = ['class', 'cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor', 'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color', 'stalk-shape', 'stalk-root', 'stalk-surface-above-ring', 'stalk-surface-below-ring', 'stalk-color-above-ring', 'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number', 'ring-type', 'spore-print-color', 'population', 'habitat']
df.columns = col_names

X = df.drop(['class'], axis=1)
y = df['class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 42)

encoder = ce.OrdinalEncoder(cols=['cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor', 'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color', 'stalk-shape', 'stalk-root', 'stalk-surface-above-ring', 'stalk-surface-below-ring', 'stalk-color-above-ring', 'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number', 'ring-type', 'spore-print-color', 'population', 'habitat'])
X_train = encoder.fit_transform(X_train)
X_test = encoder.transform(X_test)

clf_gini = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=0)
clf_gini.fit(X_train, y_train)

y_pred_gini = clf_gini.predict(X_test)

# accuracy = accuracy_score(y_test, y_pred_gini)
# precision = precision_score(y_test, y_pred_gini, pos_label='p')
# recall = recall_score(y_test, y_pred_gini, pos_label='p')
# f1 = f1_score(y_test, y_pred_gini, pos_label='p')
# cm = confusion_matrix(y_test, y_pred_gini)

# print("Akurasi: " + str(accuracy))
# print("Presisi: " + str(precision))
# print("Recall: " + str(recall))
# print("F1: " + str(f1))
# print("CM: " + str(cm))
# print(classification_report(y_test, y_pred_gini))

# plt.figure(figsize=(10, 10))
# tree.plot_tree(clf_gini, filled=True, feature_names=X.columns, class_names=['e', 'p'])
# plt.savefig('tree.png')

#             true pos        false neg
# true  pos   1355            37
# false neg   41              1248