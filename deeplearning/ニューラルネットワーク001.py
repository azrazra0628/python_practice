
# 活性化関数について
# ニューロンの興奮状態を表す信号に変換する

## 1. ステップ関数
# 0か１かをシンプルに表現する

#%%
import numpy as np
import matplotlib.pyplot as plt 
def step_function(x):
    return np.where(x<=2, 0, 1)

x = np.linspace(-5, 5, 10000)
y = step_function(x)

plt.plot(x, y)
plt.show()

print(x)
