import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import RendererAgg


def conclusion():
     st.title("Openings for further work")

     st.subheader("Segmentation")
     st.markdown("Regarding the segmentation task, one could try to test other **architectures** such as:")
     st.markdown(" - GAN (taking into consideration the long training times and need for larger dataset")
     st.image("images/gan.png",caption="Segmentation Using Generative Adversarial Networks / Medium")
     st.markdown(" - T-Net (which performs well in retinal vessel segmentation")
     st.image("images/TNET.jpg",caption="T-Net: Nested encoder–decoder architecture for the main vessel segmentation in coronary angiography")
     st.markdown("Another lead to improve the performances if the processing:")
     st.markdown(" - **Preprocessing**: Using sequence data to get pseudolabels")
     st.markdown(" - **Postprocessing**: Removing falsely detected isolated vessel pixels regions with specific area (less than # pixels)")
     st.markdown(" - **Postprocessing**: Eliminate noise")

     st.subheader("Registration")

     st.markdown("Thanks for listening !")