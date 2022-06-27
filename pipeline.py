import pandas as pd
import joblib
# from sklearn.experimental import enable_hist_gradient_boosting
# from sklearn.ensemble import HistGradientBoostingRegressor

model = joblib.load('model.sav')
transformer = joblib.load('transformer.sav')

class Pipeline:

    def transform(self, cement, slag, water, superplasticizer, age):
        df = pd.DataFrame({'cement':[cement], 'slag':[slag], 'water': [water], 'superplasticizer':[superplasticizer], 'age': [age]})

        # Dealing with outliers

        for idx, row in df.iterrows():

            if df.loc[idx, 'cement']> 600:
                df.loc[idx, 'cement'] = 600

            if df.loc[idx, 'cement']< 0:
                df.loc[idx, 'cement'] = 0

            if df.loc[idx, 'slag']> 350:
                df.loc[idx, 'slag'] = 350

            if df.loc[idx, 'slag']< 0:
                df.loc[idx, 'slag'] = 0
                
            if df.loc[idx, 'water']> 230:
                df.loc[idx, 'water'] = 230
                
            if df.loc[idx, 'water']< 124:
                df.loc[idx, 'water'] = 124
                
            if df.loc[idx, 'superplasticizer']> 25:
                df.loc[idx, 'superplasticizer'] = 25
            
            if df.loc[idx, 'superplasticizer']< 0:
                df.loc[idx, 'superplasticizer'] = 0
            
        mylist = [28, 2, 7, 56, 90, 120, 14, 100]
        mydict = {}
        mylist.sort()
        for (x,y) in enumerate(mylist):
            mydict[y]=x
            

        takeClosest = lambda num,collection:min(collection,key=lambda x:abs(x-num))

        for idx, row in df.iterrows():
            df.loc[idx, 'age'] = mydict[takeClosest(df.loc[idx, 'age'], mylist)]

        return df
