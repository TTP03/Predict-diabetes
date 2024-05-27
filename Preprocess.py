import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dataset.csv')

pd.set_option('display.max_columns', None)


# Xem thông tin tổng quát về dữ liệu
print(df.info())

# Xem 5 dòng đầu tiên của dữ liệu
print(df.head())

# Phân tích thống kê mô tả
print(df.describe())

# Vẽ histogram cho các biến số
df.hist(figsize=(15, 10))
plt.tight_layout()
plt.show()

# # Vẽ từng histogram của các cột
# for i in range(0,21):
#     plt.figure(figsize=(8, 6))
#     sns.countplot(x=df.columns[i], data=df)
#     plt.show()

# Vẽ ma trận tương quan
corr_matrix = df.corr()
plt.figure(figsize=(15, 10))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()

# Histogram của người bệnh và không bệnh là không cân bằng
plt.figure(figsize=(8, 6))
sns.countplot(x=df.columns[0], data=df)
plt.title('Trước khi cân bằng')
plt.show()

# Cân bằng mẫu bằng cách random oversampling
class_0 = df[df['Diabetes_binary'] == 0]
class_1 = df[df['Diabetes_binary'] == 1]

# Over sampling của nhóm thiểu số
class_1_over = class_1.sample(len(class_0), replace=True)

# Dataframe mới
df_new = pd.concat([class_1_over, class_0], axis=0)

# Sau khi Oversampling
plt.figure(figsize=(8, 6))
sns.countplot(x=df_new.columns[0], data=df_new)
plt.title('Sau khi cân bằng')
plt.show()

df_new.hist(figsize=(15, 10))
plt.tight_layout()
plt.show()

# Xuất dataset mới
df_new.to_csv('dataset_new.csv', index=False)

# Phân tích mối quan hệ giữa các biến
sns.pairplot(df, hue='Outcome')
plt.show()

