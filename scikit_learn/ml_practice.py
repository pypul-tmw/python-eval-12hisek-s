from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline 
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


iris = load_iris()

x = iris.data
y = iris.target

print("Features shape:",x.shape)
print("Target shape:",y.shape)


#split dataset

x_train, x_test,y_train,y_test = train_test_split(
    x,y,
    test_size=0.3,
    random_state=4
)


# Create pipeline
pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier',LogisticRegression())
])

# Train model
pipe.fit(x_train,y_train)

# Predict
y_pred = pipe.predict(x_test)

print("Accuracy:",accuracy_score(y_test,y_pred))

print("Classification Report:\n",classification_report(y_test,y_pred))

print(iris.feature_names)