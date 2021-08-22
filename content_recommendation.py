import pandas as pd


def recommendation():
    print('input_item')
    print('input_age')
    print('input_gender')

    # Read Local directory
    hello = pd.read_csv("Bigdataset.csv")

    # system get the gender from API
    new = hello[hello['Gender'] == 'input_gender']

    # code start

    # grouping the items count and the order rate in the data set in the ascending order
    new.groupby('ItemName')['order rate'].mean().sort_values(ascending=False).head()

    new.groupby('ItemName')['order rate'].count().sort_values(ascending=False).head()

    # take the mean of the above grouping
    Order_rating = pd.DataFrame(new.groupby('ItemName')['order rate'].mean())
    # print(Order_rating.head())

    # how no of order_rate has flowed with mean with order_rate (ItemName,order rate)
    # here the order rate depicts the mean of the order rate
    # here the num of Order_rate depicts the actual no of order rate
    Order_rating['num of Order_rate'] = pd.DataFrame(new.groupby('ItemName')['order rate'].count())
    # print(Order_rating.head())

    # CustomerID,ItemName,order rate distribution in dataset using table
    itemmat = new.pivot_table(index='CustomerID', columns='ItemName', values='order rate')
    # print(itemmat.head())

    # sort num of Order_rate in the ascending order
    Order_rating.sort_values('num of Order_rate', ascending=False).head(10)

    Order_rating.head(20)

    # system get the gender from API
    # item_name='Sports Bags - Puma'
    x_user_ratings = itemmat['input_item']
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

    return print(output.head(5))


class Content:
    def __init__(self, input_item, input_age, input_gender):
        self.input_item = input_item
        self.input_age = input_age
        self.input_gender = input_gender
