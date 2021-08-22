import pandas as pd
import seaborn as sns

sns.set_style('white')
# %matplotlib inline


age = int(input("Enter your age: "))

gender = input("Enter your gender: ")

item_name = input("Enter your item name: ")

print('My details ')
print('...........................................')

print('Your gender is : ' + gender)
print('Your item name is : ' + item_name)

df = pd.read_csv("Bigdataset.csv")

if age <= 18:
    data = df[df['Age'] <= 18]
    print(age)


elif age <= 24:
    data = df[df['Age'] <= 24]
    print(age)


elif age <= 34:
    data = df[df['Age'] <= 34]
    print(age)

elif age <= 44:
    data = df[df['Age'] <= 44]
    print(age)

else:
    data = df[df['Age'] >= 45]
    print(age)

new = data[data['Gender'] == gender]
# print(new)


new.groupby('ItemName')['order rate'].mean().sort_values(ascending=False).head()

new.groupby('ItemName')['order rate'].count().sort_values(ascending=False).head()

Order_rating = pd.DataFrame(new.groupby('ItemName')['order rate'].mean())
# print(Order_rating.head())

Order_rating['num of Order_rate'] = pd.DataFrame(new.groupby('ItemName')['order rate'].count())
# print(Order_rating.head())

itemmat = new.pivot_table(index='CustomerID', columns='ItemName', values='order rate')
# print(itemmat.head())

Order_rating.sort_values('num of Order_rate', ascending=False).head(10)

Order_rating.head(20)

# system get the gender from API
# item_name='Sports Bags - Puma'
x_user_ratings = itemmat[item_name]
x_user_ratings.head()

similar_to_x = itemmat.corrwith(x_user_ratings)

corr_x = pd.DataFrame(similar_to_x, columns=['Correlation'])
corr_x.dropna(inplace=True)
# print(corr_x.head())

corr_xx = corr_x.join(Order_rating['num of Order_rate'])
# print(corr_xx)

recom_data = corr_xx[corr_xx['num of Order_rate'] > 4].sort_values('Correlation', ascending=False)
# print(recom_data)

output = recom_data['Correlation']
output.head(5)

print('-----------------------------------------------------------------------------------')
print(output.head(6))

# item: Sports Bags - Diesel, Sports Bags - Puma
# age : 45
# gender: Female
