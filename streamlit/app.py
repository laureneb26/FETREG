import streamlit as st
from contexte import contexte
from task1 import task1
from task2 import task2
from challenge import challenge
from conclusion import conclusion

def main():

    st.sidebar.title("FETREG")
    
    menu_list = ["Motivation","Segmentation", "Registration", "Challenge: Beat the performance", "Openings for further work"]
    menu = st.sidebar.radio("Table of Content", menu_list)
    if menu == menu_list[0]:
        contexte()
    elif menu == menu_list[1]:
        task1()
    elif menu == menu_list[2]:
        task2()
    elif menu == menu_list[3]:
        challenge()
    else:
        conclusion()

        # Group member information
    st.sidebar.info(
        "FETREG: MediCSS - Session: 2022"
        "\n\n"
        "Under the supervision of:"
        "\n\n"
        "[Sophia BANO](https://www.linkedin.com/in/sophia-bano/)"
        "\n\n"
        "[Francisco VASCONCELOS](https://www.linkedin.com/in/francisco-vasconcelos-aa793ab6/)"
        "\n\n"
        "Codes may be found on GitHub:"
        "\n\n"
        "[Github 2021](https://github.com/sophiabano/EndoVis-FetReg2021)"
        "\n\n"
        "[Github 2022](https://github.com/Zrrr1997/fet_reg_2022)"
        )


if __name__ == "__main__":
    main()