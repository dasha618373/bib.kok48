import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas as pd

# Загрузка данных
data = sm.datasets.co2.load_pandas()
df = data.data

# Преобразование индекса в datetime
df.index = pd.to_datetime(df.index)

# Выбор промежутка времени
df = df['1958':'1980']

# Построение графика
plt.figure(figsize=(12, 6))  
plt.plot(df.index, df['co2'], label='CO2')

# Добавление подписей и заголовка
plt.xlabel("Год")
plt.ylabel("CO2 (ppm)")
plt.title("Динамика CO2 (1958-1980)")
plt.legend()

# Отображение графика
plt.grid(True)  
plt.tight_layout()  
plt.show()