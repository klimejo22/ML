import pandas as pd
import kagglehub
import seaborn as sns

# Download latest version
path = kagglehub.dataset_download("kundanbedmutha/exam-score-prediction-dataset")

# Zakladni vykresleni
df = pd.read_csv(path + "/Exam_Score_Prediction.csv")

df

# DataFrame
variable = {
    "calories" : [100, 200, 300],
    "test" : [1, 2, 3]
}
var = pd.DataFrame(variable)

print(var.loc[0])

# Info o datovych typech
print(df.info())

# Prace s prazdnymi daty
new_df = df.dropna()

new_df

df.fillna({"exam_score" : df['exam_score'].mean()}, inplace=True)

# Nastavovani labels k datum
# df.loc[0, "exam_score"] = "Prosel"

# for x in df.index:
#   if df.loc[x, "exam_score"] > 75:
#     df.loc[x, "exam_score"] = "Prosel"

# Vykreslovani se seaborn
sns.histplot(data=df, x="exam_score")
