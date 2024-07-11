import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('Perpendiculares y paralelismo entre rectas.')

with st.container(border=True):
    st.subheader('Rectas Paralelas:')
    st.markdown('''
    Cuando graficas dos o más ecuaciones lineales en el plano de coordenadas, generalmente se cruzan en algún punto. Sin embargo, cuando dos rectas en un plano coordenado nunca se cruzan, se llaman rectas paralelas.
    $$
    y1=4x+2
    $$

    $$
    y2=4x-6
    $$

    La ecuación de una recta es $$y=mx+b$$, la pendiente de una recta es representada con la letra $$m$$, y el punto de corte con el eje y con la letra $$b$$.


    Para que las recta sean paralelas la pendiente de $$y1$$ y $$y2$$ deben se iguales, osea, $$m1=m2$$.
    ''')
    st.markdown("**Geometricamente las rectas paralelas se ven así:**")

    col1, col2= st.columns([1,2], gap="medium") 
with col1:
    ini=int(st.number_input("Inicio:", value=1))
    fin=int(st.number_input("Fin:", value=1))
with col2:
    x=np.linspace(ini,fin)
    X=4*x+2
    Y=4*x-6

    fig, ax=plt.subplots()
    ax.plot(x,X)
    ax.plot(x,Y)
    st.pyplot(fig)
   

with st.container(border=True):
    st.subheader('Rectas perpenticulares:')
    st.markdown('''
    Cuando dos rectas en el plano de coordenadas se cruzan en un ángulo recto. Estas se llaman rectas perpendiculares.

    $$
    y1=3x-2
    $$
    $$
    y2=-\\frac{1}{3}{x}+1
    $$

    Para que las recta sean perpendiculares la pendiente de $$y1$$ y $$y2$$ debe cumplir con la siguiente formula:
    $$
    m1*m2=-1
    $$
    $$
    m2=-\\frac{1}{m1}
    $$
    ''')
    st.markdown("**Geometricamente las rectas perpenticulares se ven así:**")

    col1, col2= st.columns([1,2], gap="medium") 
with col1:
    ini=int(st.number_input("Inicio:", value=-1))
    fin=int(st.number_input("Fin:", value=5))
with col2:
    x=np.linspace(ini,fin)
    A=(3*x)-2
    B=-(x/3)+1

    fig, ax=plt.subplots()
    ax.plot(x,A)
    ax.plot(x,B)
    ax.set_xlim(ini,fin)
    ax.set_ylim(ini,fin)
    st.pyplot(fig)

with st.container(border=True):
        st.subheader('Rectas Paralelas y Perpenticulares:')
        st.markdown("Digite los valores de la pendiente y el punto de corte con el eje y de la recta 1:")
        col1, col2= st.columns(2) 
        with col1:
            m= int(st.number_input("a:", value=1))
        with col2:
            b= int(st.number_input("b:", value=1))

        if m!=0:
            st.markdown("La ecuación de la recta que ingreso es:")
            st.latex(f"y1={m}x+{b}")
            st.markdown('''
            Ingrese el punto de corte con el eje y de la recta 2:''')
            b2=int(st.number_input("b2:", value=1))
            st.markdown('''
            Una recta paralela a la ingresada es:''')
            st.latex(f"y2={m}x+{b2}")
            st.markdown("**Geometricamente la recta paralela a la ingresada es:**")
            col1, col2= st.columns([1,2], gap="medium") 
            with col1:
                ini=int(st.number_input("Inicio:", value=2))
                fin=int(st.number_input("Fin:", value=2))
            with col2:
                x=np.linspace(ini,fin)
                X=m*x+b
                Y=m*x+b2

                fig, ax=plt.subplots()
                ax.plot(x,X)
                ax.plot(x,Y)
                st.pyplot(fig)

            
            st.markdown('''
            Una recta perpendicular a la ingresada es:''')
            m2=-(1/m)
            st.latex(f"y2={m2}x+{b2}")

            
        st.markdown("**Geometricamente la recta perpendicular a la ingresada es:**") 
        col1, col2= st.columns([1,2], gap="medium") 
        with col1:
            ini=int(st.number_input("Inicio:", value=-5))
            fin=int(st.number_input("Fin:", value=10))
        with col2:
            x=np.linspace(ini,fin)
            A=(m*x)+b
            B=(m2*x)+b2

            fig, ax=plt.subplots()
            ax.plot(x,A)
            ax.plot(x,B)
            ax.set_xlim(ini,fin)
            ax.set_ylim(ini,fin)
            st.pyplot(fig)


            




    
