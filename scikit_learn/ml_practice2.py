from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd 

data = pd.DataFrame(
    {
        'size':[1000,1200,1500,2000],
        'price':[200000,300000,350000,450000]
    }
)

x = data[['size']]
y = data[['price']]

#Split Data
x_train,x_test,y_train,y_test = train_test_split(
    x,y,
    test_size = 0.2,
    random_state=42
)

model = LinearRegression()
model.fit(x_train,y_train)


predictions = model.predict(x_test)


#Evaluate
mse = mean_squared_error(y_test,predictions)
print("MSE:",mse)

new_price = model.predict([[1600]])
print("Prediction price:",new_price[0])