##1. Irisデータについて

# scikit-learnに用意されているデータ
# 「花がくの長さ」「花がくの大きさ」「花びらの長さ」「花びらの幅」という4つのデータを集め、
# アイリスの品種を教師データとして与えてある

#%%
from sklearn.datasets import load_iris

iris = load_iris()
print(iris.data.shape)
#(150, 4)
#データは150個用意されており、上記4つのデータが格納されている

print(iris.data[:10])
# [[5.1 3.5 1.4 0.2]
#  [4.9 3.  1.4 0.2]
#  [4.7 3.2 1.3 0.2]
#  [4.6 3.1 1.5 0.2]
#  [5.  3.6 1.4 0.2]
#  [5.4 3.9 1.7 0.4]
#  [4.6 3.4 1.4 0.3]
#  [5.  3.4 1.5 0.2]
#  [4.4 2.9 1.4 0.2]
#  [4.9 3.1 1.5 0.1]]
#10個だけ表示しているが全部で150個ある

print(iris.target_names)
# ['setosa' 'versicolor' 'virginica']

# irisデータは変数irisに格納されてる
# iris.data - irisのデータ
# iris.target - 教師用データ
# iris.target_names - 教師用データの各値に割り当てらている品種名が、リスト化されている

##2. 学習用データと予測用データを用意

# 読み込まれたデータを学習用のデータと、予測用データに振り分けて用意する

# 変数 = train_test_split(データ,教師データ, test_size=予測データの割合)

# 以下の変数に格納されて返される

# train_X - 学習用に割り当てるデータ
# test_X  - 予測用に割り当てるデータ
# train_Y - 学習用データの教師データ
# test_Y  - 予測用データの教師データ


#%%
from sklearn.model_selection import train_test_split

(train_X, test_X, train_Y, test_Y) = train_test_split(iris.data,
iris.target,  test_size=0.2)

print(iris.target_names[test_Y])
# ['virginica' 'setosa' 'virginica' 'virginica' 'versicolor' 'versicolor'
#  'virginica' 'setosa' 'versicolor' 'versicolor' 'setosa' 'versicolor'
#  'virginica' 'versicolor' 'virginica' 'versicolor' 'setosa' 'setosa'
#  'setosa' 'versicolor' 'virginica' 'setosa' 'setosa' 'versicolor'
#  'versicolor' 'setosa' 'versicolor' 'versicolor' 'virginica' 'setosa']
#予測用データの割り当てはランダム

print(test_Y)
# [2 0 2 2 1 1 2 0 1 1 0 1 2 1 2 1 0 0 0 1 2 0 0 1 1 0 1 1 2 0]
print(test_X)
# [[7.2 3.  5.8 1.6]
#  [4.8 3.  1.4 0.3]
#  [5.9 3.  5.1 1.8]
#  [6.3 3.3 6.  2.5]
#  [5.7 2.9 4.2 1.3]
#  [6.7 3.  5.  1.7]
#  [6.9 3.1 5.4 2.1]
#  [4.3 3.  1.1 0.1]
#  [6.  2.2 4.  1. ]
#  [6.7 3.1 4.4 1.4]
#  [5.  3.5 1.6 0.6]
#  [5.7 2.8 4.5 1.3]
#  [6.4 2.7 5.3 1.9]
#  [5.5 2.6 4.4 1.2]
#  [6.7 3.  5.2 2.3]
#  [5.9 3.  4.2 1.5]
#  [5.1 3.8 1.9 0.4]
#  [5.1 3.4 1.5 0.2]
#  [4.4 3.  1.3 0.2]
#  [6.1 2.8 4.7 1.2]
#  [5.7 2.5 5.  2. ]
#  [4.6 3.2 1.4 0.2]
#  [4.5 2.3 1.3 0.3]
#  [5.8 2.7 3.9 1.2]
#  [6.1 2.9 4.7 1.4]
#  [4.8 3.  1.4 0.1]
#  [5.2 2.7 3.9 1.4]
#  [5.8 2.6 4.  1.2]
#  [7.4 2.8 6.1 1.9]
#  [5.  3.6 1.4 0.2]]




