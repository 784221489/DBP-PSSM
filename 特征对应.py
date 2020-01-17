import pandas as pd
df = pd.read_csv("E:\\Graduate\\DNA-Binding\\data\\feature_selection\\newdnarset\\z-score.csv", low_memory=False)
name = pd.read_csv("E:\\Graduate\\DNA-Binding\\data\\feature_selection\\feature\\mrmr排序.csv")
feature_name = name.columns.tolist()[:180]
select_feature = pd.DataFrame()
print(len(feature_name))
for i in df.columns.tolist():
    if i in feature_name:
        select_feature.loc[:,i] = df.loc[:,i]
select_feature.to_csv('E:\\Graduate\\DNA-Binding\\data\\feature_selection\\newdnarset\\180select_feature\\z-score.csv',sep = ',',header=True)



