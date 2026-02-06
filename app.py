
import streamlit as st
from core.cursos import cursos
from core.calculo_score import calcular_score

st.set_page_config(page_title="🎓 UniAdvisorAI", layout="wide")
st.title("🎓 UniAdvisorAI - Escolha o Curso Ideal")

# Entradas do estudante
nome = st.text_input("Nome")
matematica = st.slider("Nota em Matemática",0,20,15)
portugues = st.slider("Nota em Português",0,20,15)
ciencias = st.slider("Nota em Ciências",0,20,15)
interesses = st.multiselect("Interesses",["Robótica","AI","Biologia","Economia","Gestão","Saúde","Programação"])
preferencia = st.selectbox("Preferência de carreira",["Pesquisa","Indústria","Mercado","Clínica"])
quiz = [st.slider(f"Pergunta {i+1}",1,5,3) for i in range(5)]

if nome:
    estudante = {
        "nome":nome,
        "notas":{"matematica":matematica,"portugues":portugues,"ciencias":ciencias},
        "interesses":interesses,
        "preferencia_trabalho":preferencia,
        "quiz":quiz
    }

    # Calcular scores
    for c in cursos:
        c["score"] = calcular_score(estudante,c)
    cursos.sort(key=lambda x:x["score"],reverse=True)

    st.subheader("🏆 Top Cursos Recomendados:")
    for i,c in enumerate(cursos[:3]):
        st.markdown(f"**{i+1}. {c['nome']} - Score: {c['score']}**")
        st.markdown(f"- Combinação de interesses/skills: {set(estudante['interesses']).intersection(set(c['skills']))}")
        st.markdown(f"- Carreira compatível: {', '.join(c['carreira'])}")
        st.markdown("---")
