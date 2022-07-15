import streamlit as st

def challenge():
    st.title("Performances comparaison")
    st.subheader("Last Year (2021):")
    st.image("images/2021a.png")
    st.image("images/2021b.png",caption="Estimating the mapping directly from segmentation masks (AIRLAB)")

    st.subheader("Our challenge (2022):")
    st.subheader("Segmentation task")
    st.image('images/attention_crf.png')
    st.markdown("We improved the performence with respect to the baseline Dice metric: +3%. This is due to the fact that the UNet++ does not compensate for noisy isolated regions and elongated holes in the blood vessels.")
    st.markdown("")

    st.subheader("Registration task")
    