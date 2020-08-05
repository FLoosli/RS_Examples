import pandas as pd
from sklearn.model_selection import train_test_split


def filmtrust_preprocessing():

    ratings = pd.read_table('filmtrust/ratings.txt', delimiter=' ')
    ratings = ratings.rename(columns={'1': 'userId', '1.1': 'movieId', '2': 'movieRating'})

    print(ratings.shape, len(ratings['userId'].unique()), len(ratings['movieId'].unique()))

    rating_matrix = pd.DataFrame(0, index=range(len(ratings['userId'].unique())+1),
                                 columns=range(len(ratings['movieId'].unique())+1))
    for i, rating in enumerate(ratings.iterrows()):
        rating_matrix.at[rating[1][0], rating[1][1]] = rating[1][2]

    print(rating_matrix.shape)
    rating_matrix = rating_matrix[1:].T[1:]

    train, test = train_test_split(rating_matrix, test_size=0.2)
    train.reset_index(inplace=True, drop=True)
    test.reset_index(inplace=True, drop=True)
    train.to_csv('train.csv', index=True)
    test.to_csv('test.csv', index=True)
    print(train.shape, test.shape)
