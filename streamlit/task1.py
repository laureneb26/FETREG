import streamlit as st
import pandas as pd
import numpy as np
import pyarrow as pa       

def task1():
    st.title("Placental Vessel Segmentation")
    st.markdown("Placental vessels segmentation is of great interest in this project since it would be of graid help to guide the surgeon while exploring the vessels.​")
    #2021
    st.subheader("From the previous session (2021):")
    st.markdown("Architecture: U-Net architecture training with ResNet backbone for vessel map prediction")
    st.image("images/segmentation.png", caption="Segmentation process scheme")
    st.markdown("As a results, and according to the used metrics (DICE and IoU), these are the obtained performances")
    st.image("images/unet_results.png")
    col1, mid, col2 = st.columns([12,1,12])
    with col1:
        st.image("images/loss1.png", caption="Loss evolution") 
    with col2:
        st.image("images/meandice1.png", caption="Dice Loss evolution")
           

    #2022
    st.subheader("Our challenge! (2022)")
    st.markdown("Our challenge was to overcome the performances in some way. Our work focused on two axes:")
    st.markdown(" - Testing a **more robust** segmentation architecture: Attention Unet")
    st.markdown(" - Fine-tuning the performances by applying **post-processing** techniques: CRF")

    st.markdown("**Conditional random fields** is a statistical modeling methode applied in pattern recogniton for structured prediction.")
    st.image('images/crf.jpeg')

    option = st.selectbox('Select an option in the drop-down menu to select one of the proposed method.', ('Unet++', 'Attention Unet','Attention Unet with CRF'))
    st.write('You selected:', option)
    if(option=='Unet++'):
        st.image('images/unet_crf.png')
    if(option=='Attention Unet'):
        st.image('images/attention.png')
    if(option=='Attention Unet with CRF'):
        st.image('images/attention_crf.png')
    st.image("images/table1.png")
    st.markdown("We can observe the following:")
    st.markdown(" 1. The residual UNet (UNet++) is a very tough baseline to beat, but has some limitations, e.g., noisy isolated regions and elongated holes in the blood vessels.")
    st.markdown("2. CRF post-processing fixes these both issues and increases the performance of the baseline 0.82 -> 0.85 Dice")

  