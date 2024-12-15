import streamlit as st
import pandas as pd
import numpy as np
from joblib import load

insurancemodel = load('insurance.pkl')

def predict_premium(age, 
                  sex,
                  bmi, 
                  children,
                  smoker, 
                  region):

    inputs_dict = {'age' : float(age), 
                   'sex': sex, 
                   'bmi': float(bmi), 
                   'children': float(children), 
                   'smoker': smoker, 
                   'region': region}

    df = pd.DataFrame(inputs_dict, index = [0])


    price = insurancemodel.predict(df)[0]
    return price 

 
#function to define the app_layout
def app_layout():

    st.title('Insurance Premium Prediction')
    st.header('Enter your details:')  
    
    ## Creating the user input fields 

    age = st.number_input('Age:',
                      value=1)

    sex = st.selectbox('Sex:', 
                         ['female', 'male'])

    bmi = st.number_input('BMI:', 
                      value=1)
    
    children = st.number_input('Children:',
                      value=1)

    smoker = st.selectbox('Smoker:', 
                            ['yes', 'no'])
    
    region = st.selectbox('Region:', 
                        ['southwest','southeast','northwest','northeast'])
    
    if st.button('Predict Premium'):
        price = predict_premium(age, sex, bmi, children, smoker,  region)
        st.success(f'Explected Premium : INR {np.round(price, 2)}')
 
if __name__=='__main__':
  app_layout()
