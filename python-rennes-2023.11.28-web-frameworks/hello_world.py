import streamlit as st

st.title('Hello World App')
tab1, tab2 = st.tabs(['Onglet 1', 'Onglet 2'])
with tab1:
    display_tab_content = st.checkbox('Voir la suite', value=False)
    if display_tab_content:
        large_column, small_column = st.columns([3, 1])
        with large_column:
            with st.expander("Afficher l'image", expanded=False):
                st.image('meetup.png')
        with small_column:
            if st.button('Click me !', type='primary', use_container_width=True):
                st.toast("FIN DU HELLO WORLD !!", icon='🎉')
                st.toast(":blue[Alors facile ?]")
