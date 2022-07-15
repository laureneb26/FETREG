import streamlit as st

def contexte():
    st.title("FETREG: Placental Vessel Segmentation and Registration in Fetoscopy")
    col1, mid, col2 = st.columns([1,1,1])
    with col1:
        st.image("images/medicss.png", width=300)
    with col2:
        st.text("Segmentation Task, MediCSS 2022")

    # TTS
    st.header("Motivation")
    st.subheader("What is TTTS?")
    col1, mid, col2 = st.columns([1,1,2])
    with col1:
         st.image("images/TTTS.jpg", caption = "Twin-To-Twin Transfusion Syndrome", width= 300)
    with col2:
            st.markdown("**Twin-to-twin transfusion syndrome** is a fetal anomaly affecting identical twins sharing a monochorionicplacenta")
            st.markdown("Affects 10 to 15 percents of monochorionic twins. The consequences are:")
            st.markdown("- *Unbalanced flow of blood*")
            st.markdown("- *Donorexperience much slower growth*")
            st.markdown("- *Recipientat risk of heart failure*")    
    st.markdown("One common treatment is **Fetoscopic laser photocoagulation**.")
    
    #Surgery
    st.subheader("Fetoscopic laser photocoagulation")
    st.markdown(" - Visually **explore** the placenta to **identify** vascular anastomose")
    st.markdown(" - **Localize** the target vessels")
    st.markdown(" - User laser to **ablate** the target vessels")
    st.image("images/fetoscopic.png", caption = "Fetoscopic laser photocoagulation")

    st.subheader("Challenges")
    col1, mid1, mid, col3= st.columns(4)
    with col1:
        st.markdown("**Additional challenges for mosaicking**")
        st.markdown(" - Dynamically changing views")
        st.markdown(" - Ground-truth not available")
        st.markdown(" - Limited field-of-view (FOV)")
    with mid1:
        st.markdown("**Difficult visual conditions**")
        st.markdown(" - Poor visibility (low resolution, varying illumination, fluid highlights...)")
        st.markdown(" - Specular highlights")
        st.markdown(" - Occlusions")
    with mid:
        st.markdown("**Computer-assisted intervention can:**")
        st.markdown(" - Automatically **segment** the placental vessels")
        st.markdown(" - **Identify** the anastomotic placental vessels ")
        st.markdown(" - Register vessels images for an **expanded vessel maps**")

    with col3:
        st.markdown("**Impact:**")
        st.markdown(" - Overcome the **visibility challenges**")
        st.markdown(" - Improve the **surgical outcome**")
        

    # Datasets
    st.subheader("Dataset")
    st.markdown("This is the first publicly available dataset of in vivo fetoscopic videos with placental vessel annotations.")
    url = "[Dataset access](https://www.ucl.ac.uk/interventional-surgical-sciences/weiss-open-research/weiss-open-data-server/fetoscopy-placenta-data)"
    st.markdown("you can accesss the dataset from the following link:")
    st.markdown(url, unsafe_allow_html=True)

    col1, mid, col2 = st.columns([6,1,6])
    with col1:
        st.markdown("This dataset is made out from: ")
        st.markdown(" - 483 vessel annotated frames from 6 in vivo fetoscopy procedures")
        st.markdown(" - 6 unannotated in vivo fetoscopy video clips (950 frames)")
    with col2:
        st.image("images/viz.png",caption="Visualisation example", width=400)

    # Video
    st.subheader("A descriptive video")
    st.video("https://www.youtube.com/watch?v=28g9614UfDg")


