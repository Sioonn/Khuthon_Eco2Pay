import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_absolute_error
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBRegressor
from sklearn.impute import SimpleImputer
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Importing the dataset
data = pd.read_csv("./data/Carbon_emission.csv")
pd.set_option('display.max_columns', None)

data.replace('', 'None', inplace=True)

categorical_columns = data.select_dtypes(include=['object']).columns
label_encoder = LabelEncoder()
for column in categorical_columns:
    data[column] = label_encoder.fit_transform(data[column])

X = data.iloc[:, :-1].values
y = data.iloc[:,-1].values
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=1)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

imputer = SimpleImputer(strategy='constant', fill_value=0)
X_train = imputer.fit_transform(X_train)
y_train = imputer.fit_transform(y_train.reshape(-1, 1))
y_train = np.ravel(y_train)

linearregression = LinearRegression()
decisiontreeregression = DecisionTreeRegressor()
supportvectorregression = SVR(kernel='rbf')
randomforestregression = RandomForestRegressor()
xgbregression = XGBRegressor()

linearregression.fit(X_train, y_train)
decisiontreeregression.fit(X_train, y_train)
supportvectorregression.fit(X_train, y_train)
randomforestregression.fit(X_train, y_train)
xgbregression.fit(X_train, y_train)

y_lin = linearregression.predict(X_test)
y_dectree = decisiontreeregression.predict(X_test)
y_supvec = supportvectorregression.predict(X_test)
y_randfor = randomforestregression.predict(X_test)
y_xgb = xgbregression.predict(X_test)

data1 = {"Regression Algorithms": ["Linear Regression", "Decision Tree Regression", 
                                       "Support Vector Regression", "Random Forest Classifier",
                                       "XGB Regression"],
      "Score": [r2_score(y_test,y_lin), r2_score(y_test, y_dectree), 
                r2_score(y_test, y_supvec), r2_score(y_test,y_randfor),
                r2_score(y_test, y_xgb) ]}

score = pd.DataFrame(data1)
print('r_squared metrics')
print(score)

data2 = {"Regression Algorithms": ["Linear Regression", "Decision Tree Regression", 
                                       "Support Vector Regression", "Random Forest Classifier",
                                       "XGB Regression"],
      "Score": [mean_absolute_error(y_test,y_lin), mean_absolute_error(y_test, y_dectree), 
                mean_absolute_error(y_test, y_supvec), mean_absolute_error(y_test,y_randfor),
                mean_absolute_error(y_test, y_xgb) ]}


score2 = pd.DataFrame(data2)
print('mean absolute error')
print(score2)

print(xgbregression.feature_importances_)

vif = pd.DataFrame()
vif["VIF Factor"] = [variance_inflation_factor(X, i) for i in range(X.shape[1])]
vif["features"] = data.columns[:-1]  # 마지막 열은 종속 변수이므로 제외
print(vif)

print(linearregression.coef_)