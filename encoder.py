#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 03:50:33 2020

@author: zico
"""


import pandas as pd
from Bio.SeqIO import parse
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq


from sklearn.preprocessing import LabelEncoder

import numpy as np
import re


path="/home/zico/zico/2nd_Sem/DBMS/Project/SARS_Cov2_Classifier-master/final.csv"

raw_data=pd.read_csv(path)

# function to convert a DNA sequence string to a numpy array
# converts to lower case, changes any non 'acgt' characters to 'n'

def string_to_array(my_string):
    my_string = my_string.lower()
    my_string = re.sub('[^acgt]', 'z', my_string)
    my_array = np.array(list(my_string))
    return my_array

# create a label encoder with 'acgtn' alphabet

label_encoder = LabelEncoder()
label_encoder.fit(np.array(['a','c','g','t','z']))



# function to encode a DNA sequence string as an ordinal vector
# returns a numpy vector with a=0.25, c=0.50, g=0.75, t=1.00, n=0.00
def ordinal_encoder(my_array):
    
    integer_encoded = label_encoder.transform(my_array)
    float_encoded = integer_encoded.astype(float)
    float_encoded[float_encoded == 0] = 0.25 # A
    float_encoded[float_encoded == 1] = 0.50 # C
    float_encoded[float_encoded == 2] = 0.75 # G
    float_encoded[float_encoded == 3] = 1.00 # T
    float_encoded[float_encoded == 4] = 0.00 # anything else, z
    
    return float_encoded


data=raw_data[["Sequence","Geo_Location"]]

dummy=[]
dum=np.array(dummy)

form={"inp_seq":dum}

seq_df = pd.DataFrame (form, columns = ['inp_seq'])

seq_list=[]

for idx, seq in enumerate(list(data["Sequence"])):
    arr=ordinal_encoder(string_to_array(seq))
    seq_list.append(arr)
    
seq_df["inp_seq"]=seq_list

final_data= data.assign(enc_seq=seq_df)


#Using this dataframe for training 
final_data=final_data[["enc_seq","Geo_Location"]]


