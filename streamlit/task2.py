import streamlit as st

def task2():
    st.title("Placental Vessel Registration and Mosaicking")
    st.markdown("Placental vessels provide complimentary features for registration​")
    #2021
    st.subheader("From the previous session (2021):")
    st.markdown("**Pyramidal Lucas-Kanade** registration framework")
    st.markdown("Registration approximated with **affine transformation**")
    st.image("images/registration.png", caption="Registration and Mosaicking process scheme")
    st.markdown("Hereunder as the results obtained in 2021:")
    st.image("images/reg_res1.png",caption="Pipeline on video clip 1")

    #2022
    st.subheader("Our challenge! (2022)")
    st.markdown("The registration challenge:")
    st.markdown(" - Implement direct pairwise consecutive frames registration using either RGB or vessel maps (or both) provided in the [Banoet al. MICCAI2020] sequence data")
    st.markdown(" - Use the provided Registration visualisation code to generate the mosaic for at least video 1 sequence")
    st.markdown("To this end, we tested two methods for **affine registration**:")
    st.markdown(" - Vessel map registration with OpenCV")
    st.markdown(" - Image refistration with vessel maps as ROI with Elastix")
    st.markdown("Registrations have been compared and evaluated on:")
    st.markdown(" - SSIM (structural similarity index measure)")
    st.markdown(" - IoU")
    st.markdown(" - Mosaic image stitching all images together")
    st.image("images/registration_scheme.png")