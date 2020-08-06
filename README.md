# Recommender Systems Examples
The algorithms are trained and evaluated on the filmtrust dataset
from https://drive.google.com/file/d/1ohQ9oo8aaR7aWlpe56hXx66x-bwXxB56/view. <br>
As an evaluation metric we used mean squared error (MSE) and root mean squared error (RMSE).

## Collaborative Filtering
This algorithm is based on similarity. Through searching for similarly rated movies,
we can come up with predictions for unseen ratings. To rate similarity between two movies,
we used the Pearson correlation coefficient and to get the most similar movies, we used a simple
KNN classifier. Based on the K most similar items,we computed a weighted average which results
in a predicted rating for the item. <br>
Best Hyperparameters in my case: <br>
- Neighbourhood size: 5
### Pros
- Easy to train as it only have to load the dataset, thus adding additional samples is very easy.
### Cons
- Decreasing prediction speed with bigger datasets as it relies on KNN algorithm to get the 
K most similar items.

## Probabilistic Matrix Factorization
This algorithm learns a feature vector for every movie item and for every user. Consequently,
if a user might like a movie the dot product between both vector results in a high value
and vice versa. <br>
Best Hyperparameters in my case: <br>
- learning rate: 0.01
- latent space dim: 5
- regulaizer: 0.01
### Pros
- Once the training process is completed, making predictions is very fast and cheap.
### Cons
- We require some training time for the algorithm to get going. 
- Because of training the algorithm, we can also suffer from the classic problem of
overfitting on the training dataset, thus a smart choice of the hyperparameter is a must.