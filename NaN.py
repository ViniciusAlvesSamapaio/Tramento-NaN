import pandas as pd
import numpy as np

#tratamento com dados Nan

datas = pd.date_range('20230101', periods=60)

df = pd.DataFrame(np.random.randn(60, 5), index = datas, columns=["A_", "B_", "C_", "D_", "E_"])

df ['F_'] = df.A_[ df.A_ > 0]

df2 = df.copy()
df3 = df.copy()

print(df2.dropna()) #eleminando todas as linhas que possuem um NaN

df3 = df3.F_.fillna(np.mean(df3.A_)) #substituindo todos os valores NaN por uma média da coluna A_
print(df3)
