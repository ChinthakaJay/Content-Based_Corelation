import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('white')
#%matplotlib inline

gender = input("Enter your gender: ")


item_name = input("Enter your item: ")

print('My details ')
print('...........................................')

print('Your gender is : '+gender)
print('Your item name is : '+item_name)

hello = pd.read_csv("Bigdataset.csv")
##print(print(hello))




# system get the gender from API
new = hello[hello['Gender'] == gender]
#print(new)

new.groupby('ItemName')['order rate'].mean().sort_values(ascending=False).head()

new.groupby('ItemName')['order rate'].count().sort_values(ascending=False).head()

Order_rating = pd.DataFrame(new.groupby('ItemName')['order rate'].mean())
##print(Order_rating.head())

Order_rating['num of Order_rate'] = pd.DataFrame(new.groupby('ItemName')['order rate'].count())
##print(Order_rating.head())

itemmat = new.pivot_table(index='CustomerID',columns='ItemName',values='order rate')
##print(itemmat.head())

Order_rating.sort_values('num of Order_rate',ascending=False).head(10)

Order_rating.head(20)

# system get the gender from API
#item_name='Sports Bags - Puma'
x_user_ratings = itemmat[item_name]
x_user_ratings.head()

similar_to_x = itemmat.corrwith(x_user_ratings)

corr_x = pd.DataFrame(similar_to_x,columns=['Correlation'])
corr_x.dropna(inplace=True)
##print(corr_x.head())

corr_xx = corr_x.join(Order_rating['num of Order_rate'])
##print(corr_xx)

recom_data = corr_xx[corr_xx['num of Order_rate']>4].sort_values('Correlation',ascending=False)
##print(recom_data)

output = recom_data['Correlation']
output.head(5)


print('-----------------------------------------------------------------------------------')
print(output.head(6))


# item: Sports Bags - Diesel, Sports Bags - Puma
#gender: Female


