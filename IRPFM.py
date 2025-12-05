import streamlit as st

st.sidebar.image("logo_matriz_red.png", width=220)

tipo = st.sidebar.selectbox('Quem pagará o imposto?', ['Empresa', 'Sócio'])

# ----- PARCELAS DINÂMICAS -----
st.sidebar.write("### Parcelas distribuídas no mês")

if "parcelas" not in st.session_state:
    st.session_state.parcelas = [0.0]  # começa com uma parcela

# Botão para adicionar nova parcela
if st.sidebar.button("Adicionar parcela"):
    st.session_state.parcelas.append(0.0)

# Exibir inputs dinamicamente
total = 0
for i, valor in enumerate(st.session_state.parcelas):
    novo_valor = st.sidebar.number_input(
        f"Parcela {i+1}",
        min_value=0.0,
        step=100.0,
        value=valor,
        key=f"parcela_{i}"
    )
    st.session_state.parcelas[i] = novo_valor
    total += novo_valor

# Resultado final
valor = total

# -------------------------------------

st.markdown("""
### O que é IRPF Mínimo?

A partir de 2025, quem recebe mais de R$ 600 mil por ano passa a estar sujeito ao Imposto de Renda Mínimo.
Esse mecanismo garante que, independentemente de deduções ou formas de remuneração, o contribuinte pague pelo menos uma alíquota mínima efetiva sobre sua renda anual total.

Na prática, a Receita Federal compara o imposto calculado tradicionalmente com o valor mínimo exigido. 
Se o imposto calculado for menor que o mínimo, a diferença será cobrada na declaração.

Esta calculadora mostra quanto de imposto você pagará e se haverá complemento devido ao IR Mínimo.
""")

st.write("---")
st.write("## Resultado")

col1, col2 = st.columns(2)

if valor > 0:
    if valor > 50000:
        if tipo == 'Empresa':

            with col1:
                st.metric('Sócio recebe', f'R$ {valor * 0.9:,.2f}')

            with col2:
                st.metric('Empresa Retém', f'R$ {valor * 0.1:,.2f}')

        else:
            with col1:
                st.metric('Sócio recebe', f'R$ {valor:,.2f}')

            with col2:
                st.metric('Custo para empresa', f'R$ {valor / 0.9:,.2f}')

    else:
        st.success(
            f"Com base no valor informado de R$ {valor:,.2f}, não há incidência de IR na fonte."
        )
else:
    st.info("Informe ao menos uma parcela no menu lateral.")
