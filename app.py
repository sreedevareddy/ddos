import numpy as np
import pickle
import streamlit as st


#loading the saved model
#loaded_model contains the model which is trained using dataset
loaded_model = pickle.load(open('trained_model.sav','rb'))   #rb - reading binary 


#creating a function 

def ddos_prediction(input_data):
    

     # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
     return 'not malicious'
    else:
     return 'malicious'
 
    

input_data = (1,4777,5092282,10,711000000,10711000000,3,1790,0,0,0,0,2,3683,1422,0)
print(ddos_prediction(input_data))  


#streamlit function

def main():
    
    #giving a title to our webpage
    st.title('DDOS ATTACK PREDICTION')
    
    #getting the input data from the user
    switch = st.text_input('enter switch value')
    pktcount = st.text_input('enter pkt_count value')
    bytecount = st.text_input('enter bytecount value')
    dur = st.text_input('enter dur value')
    dur_nsec = st.text_input('enter dur_nsec value')
    tot_dur = st.text_input('enter tot_dur value')
    flows = st.text_input('enter flows value')
    packetins = st.text_input('enter packetins value')
    pktperflow = st.text_input('enter pktperflow value')
    byteperflow = st.text_input('enter byteperflow value')
    pktrate = st.text_input('enter pktrate value')
    Pairflow = st.text_input('enter pairflow value')
    port_no = st.text_input('enter port value')
    tx_bytes = st.text_input('enter tx_bytes value')
    rx_bytes = st.text_input('enter rx_bytes value')
    tx_kbps =st.text_input('enter tx_kbps value')
    
    #code for prediction
    predict = ''
    
    #creating a button anout prediction
    if st.button('Ddos predict'):
        predict = ddos_prediction([switch,pktcount,bytecount,dur,dur_nsec,tot_dur,flows,packetins,pktperflow,byteperflow,pktrate,Pairflow,port_no,tx_bytes,rx_bytes,tx_kbps])
        
    
    st.success(predict)




if __name__ == '__main__':
   main()    