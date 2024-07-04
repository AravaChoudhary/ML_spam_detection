import numpy as np
import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

class custommodel:
    is_legit = False
    def __init__(self,mail_text) -> bool:
        self.df = pd.read_csv('mail_data.csv')

        #Label Encoding
        self.df.loc[self.df['Category'] == 'spam','Category'] = 0
        self.df.loc[self.df['Category'] == 'ham','Category'] = 1

        self.X = self.df['Message']
        self.Y = self.df['Category']

        #Splitting Data into train test split
        X_train , X_test , Y_train , Y_test = train_test_split(self.X , self.Y , test_size = 0.2 , random_state = 2)

        #feature selection
        feature_extraction = TfidfVectorizer(min_df = 1 , stop_words = 'english' , lowercase =  True )

        X_train_1 = feature_extraction.fit_transform(X_train)
        X_test_1 = feature_extraction.transform(X_test)

        Y_train = Y_train.astype('int')
        Y_test = Y_test.astype('int')

        #Model Training
        model = LogisticRegression()
        model.fit(X_train_1 , Y_train)

        #Accuracy Check

        #Training Data
        X_train_prediction = model.predict(X_train_1)
        training_data_accuracy = accuracy_score(Y_train,X_train_prediction)
        print("Accuracy of the TRAINING DATA : ",training_data_accuracy * 100 , "%")

        #Testing Data
        X_test_prediction = model.predict(X_test_1)
        testing_data_accuracy = accuracy_score(Y_test,X_test_prediction)
        print("Accuracy of the TESTING DATA : ",testing_data_accuracy * 100 , "%")

        input_mail = [mail_text]
        input_mail_number = feature_extraction.transform(input_mail)

        #Making Predictions
        prediction = model.predict(input_mail_number)
        if(prediction == 1):
            print("HAM EMAIL --> Useful Email")
            self.is_legit = True
        else:
            print("SPAM EMAIL --> Unwanted Email")
            self.is_legit = False

        pass
