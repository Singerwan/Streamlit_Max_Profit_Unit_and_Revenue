import streamlit.components.v1 as components
import streamlit as st
from sympy import symbols, Function, solve, Eq,plot

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

# Number input with placeholder and no default value
st.title("Data Entry for two Points for Calculating Max Revenue")
col1, col2, col3 ,col4= st.columns(4, vertical_alignment="bottom")

with col1:
    x_price_1 = st.number_input(
    label=":blue[Please enter the price of the product (x_price_1):]",
    placeholder="Type a number...",
    step=0.5,
    value=10.00,
    format="%0.1f",key="x_price_1"
    )
    st.write("x_price_1:", x_price_1)

with col2:
    y_demand_1 = st.number_input(
    label=":blue[Please enter the quantity_sold based on price (x_price_1):]",
    placeholder="Type a number...",
    step=0.5,
    value=100.00,
    format="%0.1f",key="y_demand_1"
    )
    st.write("y_demand_1:", y_demand_1)

with col3:
    x_price_2 = st.number_input(
    label=":red[Please enter the price of the product (x_price_2):]",
    placeholder="Type a number...",
    step=0.5,
    value=20.00,
    format="%0.1f",key="x_price_2"
    )
    st.write("x_price_2:", x_price_2)

with col4:
    y_demand_2 = st.number_input(
    label=":red[Please enter the quantity_sold based on price (x_price_2):]",
    placeholder="Type a number...",
    step=0.5,
    value=200.00,
    format="%0.1f",key="y_demand_2"
    )
    st.write("y_demand_2:", y_demand_2)

st.markdown(":red[**Slope and y-intercept formula&emsp;:**] &emsp;:blue[**$y=mx+b$  &rarr; &emsp;**] &rarr;&emsp;Revenue = Slope(m) * Price + y_intercept(b)&rarr; &emsp; :green[Slope (m)=$ \\frac{y_{demand_2}-y_{demand_1}}{x_{price_2}-x_{price_1}}$]")
slope_prb=round((y_demand_2-y_demand_1)/(x_price_2-x_price_1),2)

y_intercept=round(y_demand_1-slope_prb*x_price_1,2)   

y_maxrev = symbols('y_maxrev')
x_pricmx = symbols('x_pricmx')
expr =y_maxrev=(slope_prb*x_pricmx+y_intercept)*x_pricmx

import sympy as sympy
df_prb=sympy.diff(expr)
x_pricmx_solved=round(solve(df_prb)[0],2)

y_maxrev=round(slope_prb*x_pricmx_solved**2+ y_intercept*x_pricmx_solved,2)
st.write("b(y_intercept):", y_intercept , "m(slope):", slope_prb,"Price is: ", str(x_pricmx_solved), "Max Revenue is : ", str(y_maxrev))
st.divider()
st.title("Data Entry for Maximizing Profit:Units Sold & Revenue")
col1, col2, col3 ,col4= st.columns(4, vertical_alignment="bottom")

with col1:
    price_constant = st.number_input(
    label=":blue[Please enter the **price constant**:]",
    placeholder="Type a number...",
    step=0.5,
    value=10.00,
    format="%0.1f",key="price_constant"
    )
    st.write("price constant:", price_constant)

with col2:
    coefficient_unit_x = st.number_input(
    label=":blue[Please enter the coefficient of unit x:]",
    placeholder="Type a number...",
    step=0.5,
    value=20.00,
    format="%0.1f",key="coefficient_unit_x"
    )
    st.write("coefficient_unit_x is :", coefficient_unit_x)

with col3:
    cost_constant = st.number_input(
    label=":red[Please enter the cost constant:]",
    placeholder="Type a number...",
    step=0.5,
    value=100.00,
    format="%0.1f",key="cost_constant"
    )
    st.write("cost_constant:", cost_constant)
with col4:
    coefficient_unitx_in_cost = st.number_input(
    label=":red[Please enter the coefficient of unitx in cost:]",
    placeholder="Type a number...",
    step=0.5,
    value=200.00,
    format="%0.1f",key="coefficient_unitx_in_cost"
    )
    st.write("coefficient_unitx_in_cost:", coefficient_unitx_in_cost)



st.markdown(" :red[profit = Revenue - Cost &emsp; &rarr;&emsp; ] :blue[price=price_constant + coefficient_unit_x * x &emsp;|&emsp;] :green[cost= cost_constant + coefficient_unitx_in_cost * x]")

            
unitx = symbols('unitx')

expr_max_prof =x_max_profit=((price_constant - coefficient_unit_x * unitx)*unitx)-(coefficient_unitx_in_cost*unitx + cost_constant)

import sympy as sympy
df_prb_max_prof=sympy.diff(expr_max_prof)
x_pricmx_prof_solved=round(solve(df_prb_max_prof)[0],2)


max_profit_rev=((price_constant - coefficient_unit_x * x_pricmx_prof_solved)*x_pricmx_prof_solved)-(coefficient_unitx_in_cost*x_pricmx_prof_solved + cost_constant)
st.write(   " Profit Equation:", str(expr_max_prof), 
            " To achieve Max Profit:unitx is:", int(x_pricmx_prof_solved),  
            "  Total Revenue based on maximum profit unitx : ", int(max_profit_rev) )

st.divider()
# html section
st.title("Maximizing Profit and Revenue Workflow ")
st.subheader("Compiled by Singer")
with open("max_profit.html", "r", encoding="utf-8") as html_file:
    html_content = html_file.read()
    components.html(html_content, height=580,width=1200)

with open("max_revenue.html", "r", encoding="utf-8") as html_file:
    html_content = html_file.read()
    components.html(html_content, height=1150,width=1200)