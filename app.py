{
    
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8bdf5934",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import pickle\n",
    "import streamlit as st\n",
    "from PIL import Image"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b890233f",
   "metadata": {},
   "outputs": [],
   "source": [
    "loaded_model=pickle.load(open('trained_model.sav','rb'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "0bac0f6a",
   "metadata": {},
   "outputs": [],
   "source": [
    "def welcome():\n",
    "    return 'welcome all'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "93907e00",
   "metadata": {},
   "outputs": [],
   "source": [
    "def prediction(TotalCharges,MonthlyCharges,tenure_range,OnlineSecurity_No,SeniorCitizen):\n",
    "    \n",
    "    prediction=loaded_model.predict([TotalCharges,MonthlyCharges,tenure_range,OnlineSecurity_No,SeniorCitizen])\n",
    "    print(prediction)\n",
    "    return prediction"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "62881993",
   "metadata": {},
   "outputs": [],
   "source": [
    "if(prediction[0])==0):\n",
    "    return 'The customer will not churn'\n",
    "else:\n",
    "    return 'The customer will churn'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "2b6027e6",
   "metadata": {},
   "outputs": [],
   "source": [
    "def main():\n",
    "    st.title(\"Customer Churn prediction\")\n",
    "    html_temp=\"\"\"\n",
    "    <div style=\"background-color:yellow;padding:13px\">\n",
    "    <h1 style=\"color:black;text-align:center;\">Customer churn prediction app </h1>\n",
    "    </div>\n",
    "    \"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "e87225fe",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2022-07-31 17:41:15.519 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\akshaya.nambiar\\anaconda3\\lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator(_root_container=0, _provided_cursor=None, _parent=None, _block_type=None, _form_data=None)"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "st.markdown('html_temp',unsafe_allow_html=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "478eecf1",
   "metadata": {},
   "outputs": [],
   "source": [
    "TotalCharges=st.text_input(\"TotalCharges\",\"Type here\")\n",
    "MonthlyCharges=st.text_input(\"MonthlyCharges\",\"Type here\")\n",
    "tenure_range=st.text_input(\"tenure_range\",\"Type here\")\n",
    "OnlineSecurity_No=st.text_input(\"OnlineSecurity_No\",\"Type here\")\n",
    "SeniorCitizen=st.text_input(\"SeniorCitizen\",\"Type here\")\n",
    "result=\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "1630a0cc",
   "metadata": {},
   "outputs": [],
   "source": [
    "if st.button(\"Predict\"):\n",
    "    result=prediction(TotalCharges,MonthlyCharges,tenure_range,OnlineSecurity_No,SeniorCitizen)\n",
    "    st.success('The output is {}'.format(result))\n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "c5d1fe2e",
   "metadata": {},
   "outputs": [],
   "source": [
    "if __name__=='__main__':\n",
    "        main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": "none",
   "id": "32e62fdb",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
