import pandas as pd

from util.logger import get_logger

logger = get_logger("recommender")


def recommend_with_age(item, gender, age):
    logger.debug("Received parameters, item: %s, gender: %s, age: %s", item, gender, age)

    df = pd.read_csv("Bigdataset.csv")

    if age <= 18:
        data = df[df['Age'] <= 18]
    elif age <= 24:
        data = df[df['Age'] <= 24]
    elif age <= 34:
        data = df[df['Age'] <= 34]
    elif age <= 44:
        data = df[df['Age'] <= 44]
    else:
        data = df[df['Age'] >= 45]

    result = _process_data(data, item, gender)
    logger.info("Result size: %s", len(result))
    if len(result) > 0:
        return result
    else:
        return recommend(item, gender)


def recommend(item, gender):
    logger.debug("Received parameters, item: %s, gender: %s", item, gender)
    data = pd.read_csv("Bigdataset.csv")
    return _process_data(data, item, gender)


def _process_data(data, item, gender):
    new = data[data['Gender'] == gender]
    # print(new)

    new.groupby('ItemName')['order rate'].mean().sort_values(ascending=False).head()

    new.groupby('ItemName')['order rate'].count().sort_values(ascending=False).head()

    order_rating = pd.DataFrame(new.groupby('ItemName')['order rate'].mean())
    # print(order_rating.head())

    order_rating['num of Order_rate'] = pd.DataFrame(new.groupby('ItemName')['order rate'].count())
    # print(order_rating.head())

    item_matrix = new.pivot_table(index='CustomerID', columns='ItemName', values='order rate')
    # print(item_matrix.head())

    order_rating.sort_values('num of Order_rate', ascending=False).head(10)

    order_rating.head(20)

    # system get the gender from API
    x_user_ratings = item_matrix[item]
    x_user_ratings.head()

    similar_to_x = item_matrix.corrwith(x_user_ratings)

    corr_x = pd.DataFrame(similar_to_x, columns=['Correlation'])
    corr_x.dropna(inplace=True)
    # print(corr_x.head())

    corr_xx = corr_x.join(order_rating['num of Order_rate'])
    # print(corr_xx)

    recom_data = corr_xx[corr_xx['num of Order_rate'] > 4].sort_values('Correlation', ascending=False)
    # print(recom_data)

    output = recom_data['Correlation']
    output.head(5)
    logger.debug("Result: %s", output.head(6))
    return output.head(6).index.tolist()
