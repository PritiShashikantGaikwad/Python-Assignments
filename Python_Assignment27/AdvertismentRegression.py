import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import metrics
import numpy as np

def MarvellousRegression(Datapath):
    df=pd.read_csv(Datapath)
    print(df.head())
    print(df.shape)

    print("Clean Data:")
    df.drop(columns=df.columns[0],inplace=True)
    print(df.shape)

    print("Fill missing values")
    print(df.isnull().sum())
    print(df.describe())

    print("Correlation Matrix")
    print(df.corr())
    
    plt.figure(figsize=(12,8))
    sns.heatmap(df.corr(),annot=True,cmap="coolwarm")
    plt.title("Advertising HeatMap")
    sns.pairplot(df)
    plt.suptitle("pairplot of independent features",y=1.02)
    plt.show()

    x=df[['TV','radio','newspaper']]
    y=df['sales']

    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

    model=LinearRegression()

    model.fit(x_train,y_train)

    y_predict=model.predict(x_test)
    MSE=metrics.mean_squared_error(y_predict,y_test)
    RMSE=np.sqrt(MSE)
    R2=metrics.r2_score(y_predict,y_test)

    print("Mean Squared error:",MSE)
    print("Root Mean Squared Error:",RMSE)
    print("R Square",R2)

def main():
  MarvellousRegression("Advertising.csv")


if __name__=="__main__":
    main()