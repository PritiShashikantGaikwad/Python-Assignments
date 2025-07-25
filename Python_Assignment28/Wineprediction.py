import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

def WinePredictionRegtession(Datapath):
    line="*"*60
    print(line)
    print("Load Csv...")
    df=pd.read_csv(Datapath)

    print(df.head())
    print(df.shape)
    print(line)

    print("data Cleaning...")
    df.dropna(inplace=True)

    x=df.drop(columns=['Class'])
    y=df['Class']
    """    print(x.head())
    print(y.head())"""
    print(line)

    scaler=StandardScaler()
    x_scaler=scaler.fit_transform(x)


    x_train,x_test,y_train,y_test=train_test_split(x_scaler,y,test_size=0.2,random_state=42)

    accuracy_Scores=[]
    ranges=range(1,22)

    for k in ranges:
        model=KNeighborsClassifier(n_neighbors=k)
        model.fit(x_train,y_train)
        y_predict=model.predict(x_test)
        Accuracy=accuracy_score(y_predict,y_test)
        accuracy_Scores.append(Accuracy)
    best_k=ranges[accuracy_Scores.index(max(accuracy_Scores))]
    print(line)
    print("best Accuracy score is:",best_k)
    print(line)

    model=KNeighborsClassifier(n_neighbors=best_k)
    model.fit(x_train,y_train)
    y_predict=model.predict(x_test)
    Accuracy=accuracy_score(y_predict,y_test)
    print(line)
    
    print("Accuracy is:",Accuracy*100)
    print(line)



       
 

def main():
    WinePredictionRegtession("Wineprediction.csv")

if __name__=="__main__":
    main()