import joblib
from pipeline import Pipeline
model = joblib.load('model.sav')
transformer = joblib.load('transformer.sav')
pipe = Pipeline()
# cement, slag, water, superplasticizer, age
cement = float(input('Cement: '))
slag = float(input('Slag: '))
water = float(input('Water: '))
superplasticizer = float(input('Superplasticizer: '))
age = int(input('Age: '))
df = pipe.transform(cement, slag, water, superplasticizer, age)
df = transformer.transform(df)
print(f'{model.predict(df)[0]:.2f}')