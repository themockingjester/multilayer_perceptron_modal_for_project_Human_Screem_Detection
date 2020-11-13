from tensorflow import keras
import pandas as pd

model = keras.models.load_model('.')
print('hi')
df = pd.read_csv('newresources.csv', index_col=0, engine = 'c')



row_num_for_verification_of_model = 154
#X2 = df.iloc[row_num_for_verification_of_model:row_num_for_verification_of_model+1,1:]
X2 = df.iloc[row_num_for_verification_of_model:,1:]
predictions = model.predict(X2)

# round predictions
rounded = [round(x[0]) for x in predictions]

print("predicted value is"+str(rounded))
print("actual value was"+str(list(df.iloc[row_num_for_verification_of_model:,0])))