import streamlit as st

st.set_page_config(
    page_title="app_1",
    layout="centered",
    page_icon=':cat:',
)

#Creamos un diccionario con las páginas de mi APP.
pages = {
    "Página_1": [
        st.Page("pag_1.py", title="Creamos página 1"),
        st.Page("pag_2.py", title="Creamos página_2"),
    ],
    "Recursos": [
        st.Page("recurso1.py", title="Nociones básicas "),
        st.Page("recurso2.py", title="Nociones avanzadas"),
    ],
}

pg = st.navigation(pages)
pg.run()


