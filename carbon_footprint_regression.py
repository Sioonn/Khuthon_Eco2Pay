import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_absolute_error
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
import warnings

warnings.filterwarnings("ignore")


# Importing the dataset
def co2_per_clothes(num):
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

    linearregression.fit(X_train, y_train)

    y_lin = linearregression.predict(X_test)


    data2 = {"Regression Algorithms": ["Linear Regression"],
        "Score": [mean_absolute_error(y_test,y_lin) ]}


    score2 = pd.DataFrame(data2)


    return linearregression.coef_[13]
# 16.39