import pandas as pd
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

def  Playpredictor(Datapath):
    line='_'*60
    print(line)
    print("load The Csv Succesfully")
    df=pd.read_csv(Datapath)
    print(df.shape)
    print(df.head())


    df.drop(columns=df.columns[0],inplace=True)
    print("After Droping the column ",df.shape)
    print(line)
    print(line)
    print("After Encoding the code")
    label_to_ecoder=['Whether','Temperature','Play']
    le=LabelEncoder()

    for col in label_to_ecoder:
        
      df[col]=le.fit_transform(df[col])

    print(df.head())
    print(line)

    print("split the code for traiing and testing purpose")

    x=df.drop(columns=['Play'])
    y=df['Play']

    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
    print(line)

    accuracy_scores=[]
    k_range=range(1,20)
    print(line)
    print("here inside the loop used the concept of parameter tuning")
    for k in k_range:
       
        model=KNeighborsClassifier(n_neighbors=k)

        model.fit(x_train,y_train)

        y_predict=model.predict(x_test)
        Accuracy=accuracy_score(y_predict,y_test)
        accuracy_scores.append(Accuracy)

    best_k=k_range[accuracy_scores.index(max(accuracy_scores))]
    print(line)
    print("the best k value is:",best_k)
    print(line)
    


    #data visualization
    plt.figure(figsize=(12,8))
    plt.plot(k_range,accuracy_scores,marker='o',linestyle='--')
    plt.title("k range  vs accuracy")
    plt.xlabel("The k Ranges  ")
    plt.ylabel("The Accuracy Score is")
    plt.grid(True)
    plt.show()
    print(line)

    print("train and test the model")
    model=KNeighborsClassifier(n_neighbors=best_k)

    model.fit(x_train,y_train)
    y_predict=model.predict(x_test)
    Accuracy=accuracy_score(y_predict,y_test)
    print('The  accuracy ',Accuracy*100)


    
def main():
   Playpredictor("PlayPrediction.csv")

if __name__=="__main__":
    main()
