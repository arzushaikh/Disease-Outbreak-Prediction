import os
import pickle #pretrained model loading 
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title='prediction of disease outbreaks',
                   layout='wide',
                   page_icon="👨‍⚕️"
                   )
diabetes_model=pickle.load(open(r"D:\vs codes\Disease Outbreaks\Saved Models\diabetes_model.sav",'rb'))
heart_disease_model=pickle.load(open(r"D:\vs codes\Disease Outbreaks\Saved Models\heart_model.sav",'rb'))
parkinsons__model=pickle.load(open(r"D:\vs codes\Disease Outbreaks\Saved Models\parkinsons_model.sav",'rb'))

with st.sidebar:
    selected=option_menu("prediction Of Disease Outbreak System", ['Diabetes Prediction', 'Heart Disease Prediction','Parkinsons Prediction'],
                         menu_icon='hospital-fill', icons=['activity', 'heart', 'person'],default_index=0)


if selected == 'Diabetes Prediction':
    st.title("Diabetes prediction using ML ")
    col1,col2,col3=st.columns(3)
    with col1:
        Pregnancies = st.text_input("Number of pregnancies")
    with col2:
        Glucose=st.text_input("Glucose Level")
    with col3:
        Bloodpressure=st.text_input("Blood pressure value")
    with col1:
        Skinthickness=st.text_input("Skin Thickness vlaue")
    with col2:
        Insulin=st.text_input("Insulin Level")
    with col3:
        BMI=st.text_input("BMI Value")
    with col1:
        DiabetesPedigreeFunction=st.text_input("Diabetes Pedigree Function Value")
    with col2:
        Age=st.text_input("Age Of the Person")

diab_diagnosis=''
if st.button('Diabetes Test Result'):
    user_input=[Pregnancies,Glucose,Bloodpressure,Skinthickness,Insulin,BMI,DiabetesPedigreeFunction,Age]
    def convert_to_float(value):
            try:
                return float(value) if value else 0.0  # If empty, return 0.0
            except ValueError:
                st.error(f"Invalid input for: {value}")
                return None
    user_input=[convert_to_float(x) for x in user_input]

    diab_prediction=diabetes_model.predict([user_input])
    if diab_prediction[0]==1:
        diab_diagnosis="The person is diabetic"
    else:
        diab_diagnosis="The person is not diabetic"
    st.success(diab_diagnosis)

#heart disease prediction

if selected == "Heart Disease Prediction":
    st.title("Heart Disease Prediction Using ML")
    col1,col2,col3=st.columns(3)
    with col1:
        Age = st.text_input("Age")
    with col2:
        Sex=st.text_input("Sex")
    with col3:
        cp=st.text_input("Chest pain types")
    with col1:
        trestbps=st.text_input("Resting Blood Pressure")
    with col2:
        Chol=st.text_input("Serum Cholestrol in mg/dl")
    with col3:
        fbs=st.text_input("Fasting Blood Sugar > 120 mg/dl")
    with col1:
        restecg=st.text_input("Resting Electrocardiographic results")
    with col2:
        thalach=st.text_input("Maximum heart rate achieved")
    with col3:
        exang=st.text_input("Exercise induces Angina")
    with col1:
        oldspeak=st.text_input("ST Depression induced by exercise")
    with col2:
        slope=st.text_input("Slope of the peak exercise ST Segment")
    with col3:
        ca=st.text_input('Major vessels colored by flourosopy')
    with col1:
        thal=st.text_input("thal : 0 = normal ; 1 = fixed defect; 2 = reversable defect")
#code for prediction
heart_diagnosis=''

#creating a button for prediction
if st.button('Heart Disease Test Result'):
    user_input=[Age,Sex,cp,trestbps,Chol,fbs,restecg,thalach,exang, oldspeak,slope,ca, thal ]
    user_input=[float(x)for x in user_input]
    heart_prediction=heart_disease_model.predict([user_input])
    if heart_prediction[0]==1:
        heart_diagnosis='The person is having heart disease'
    else:
        heart_diagnosis='The person does not have any heart disease'
st.success(heart_diagnosis)

#parkinspns prediction page 
if selected=="Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction using ML")
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        fo = st.text_input("MDVP:Fo(Hz)")
    with col2:
        fhi=st.text_input("MDVP:Fhi(Hz)")
    with col3:
        flo=st.text_input("MDVP:Flo(Hz)")
    with col4:
        Jitter_percent=st.text_input("MDVP:Jitter(%)")
    with col5:
        jitter_Abs=st.text_input("MDVP:Jitter(Abs)")
    with col1:
        RAP=st.text_input("MDVP:RAP")
    with col2:
        PPQ=st.text_input("RMDVP:PPQ")
    with col3:
        DDP=st.text_input("Jitter:DDP")
    with col4:
        shimmer=st.text_input("MDVP:Shimmer")
    with col5:
        shimmer_dB=st.text_input("MDVP:Shimmer(dB)")
    with col1:
        APQ3=st.text_input("Shimmer:APQ3")
    with col2:
        APQ5=st.text_input('Shimmer:APQ5')
    with col3:
        APQ=st.text_input("MDVP:APQ")
    with col4:
        DDA=st.text_input("Shimmer:DDA")
    with col5:
        NHR=st.text_input("NHR")
    with col1:
        HNR=st.text_input("HNR")
    with col2:
        RPDE=st.text_input('RPDE')
    with col3:
        DFA=st.text_input("DFA")
    with col4:
        spread1=st.text_input("spread1")
    with col5:
        spread2=st.text_input("spread2")
    with col1:
        D2=st.text_input("D2")
    with col2:
        PPE=st.text_input('PPE')
#code for prediction
parkinsons_diagnosis=''

if st.button("Parkinson's Test Result"):
    user_input=[fo,fhi,flo,Jitter_percent,jitter_Abs,RAP,PPQ,DDP,shimmer,shimmer_dB,APQ3, APQ5,APQ,
    DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]

    user_input=[float(x) for x in user_input]

    parkinsons_prediction=parkinsons__model.predict([user_input])

    if parkinsons_prediction[0]== 1:
        parkinsons_diagnosis="The person has parkinsons disease"
    else:
        parkinsons_diagnosis="The person doesnot have parkinsons disease"
st.success(parkinsons_diagnosis)




