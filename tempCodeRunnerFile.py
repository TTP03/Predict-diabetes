
# # Cân bằng mẫu bằng cách random oversampling
# class_0 = df[df['Diabetes_binary'] == 0]
# class_1 = df[df['Diabetes_binary'] == 1]

# # Over sampling của nhóm thiểu số
# class_1_over = class_1.sample(len(class_0), replace=True)

# # Dataframe mới
# df_new = pd.concat([class_1_over, class_0], axis=0)

# # Sau khi Oversampling
# plt.figure(figsize=(8, 6))
# sns.countplot(x=df_new.columns[0], data=df_new)
# plt.title('Sau khi cân bằng')
# plt.show()

# df_new.hist(figsize=(15, 10))
# plt.tight_layout()
# plt.show()

# # Xuất dataset mới
# df_new.to_csv('df_new.csv', index=False)