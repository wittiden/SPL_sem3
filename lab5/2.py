import pandas as pd

def fill_data(df):
    if df['Age'].isna().sum() > 0:
        df['Age'] = df['Age'].fillna(df['Age'].median())

    if df['Cabin'].isna().sum() > 0:
        df['Cabin'] = df['Cabin'].fillna('unknown')

    if df['Embarked'].isna().sum() > 0:
        df['Embarked'] = df['Embarked'].fillna('unknown')

    return df

def detect_anomalies(df):
    age_anomalies = df[(df['Age'] < 0) | (df['Age'] > 100)]
    if not age_anomalies.empty:
        print(age_anomalies['Age'])
    else:
        print("No Age Anomalies")

    family_anomalies = df[(df['SibSp'] > 5) | (df['Parch'] > 5)]
    if not family_anomalies.empty:
        print(family_anomalies['SibSp'])
    else:
        print("No SibSp Anomalies")

    return df

df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
print("Тип объекта:", type(df))
print("Размер данных:", df.shape)

df = df.head(len(df))
print(df)

print(df[['Name', 'Age']])
print(df.loc[[1,50,100],['Name', 'Age']])

print("\nДО ЗАПЛНЕНИЯ ПРОПУСКОВ")
print(f"{df.isna().sum()}")

fill_data(df)

print("\nПОСЛЕ ЗАПЛНЕНИЯ ПРОПУСКОВ")
print(f"{df.isna().sum()}")

print("\nПОИСК АНОМАЛИЙ")
detect_anomalies(df)


print("\n1. ОСНОВНАЯ СТАТИСТИКА:")
print(df.describe())
print("\n2. АНАЛИЗ ВЫЖИВАЕМОСТИ:")
print(df['Survived'].mean()*100)
print("\n2. АНАЛИЗ ВЫЖИВАЕМОСТИ ПО ПОЛУ:")
print(df.groupby('Sex')['Survived'].mean()*100)
print("\n2. АНАЛИЗ ВЫЖИВАЕМОСТИ ПО КЛАССУ:")
print(df.groupby('Pclass')['Survived'].mean()*100)

df.to_csv('titanic.csv', index=False)
# df2 = pd.DataFrame({'Age':[1,2,3,4,5,6,7,8,9,10],})
# print(df2)
#
# df2.to_csv('age.csv')
# df2.info()
