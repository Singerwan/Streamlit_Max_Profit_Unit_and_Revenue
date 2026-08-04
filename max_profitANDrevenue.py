import streamlit.components.v1 as components
import streamlit as st
from sympy import symbols, Function, solve, Eq,plot
import pandas as pd
import numpy as np
import plotly.graph_objs as go


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

with st.expander("Plot Visualization", expanded=True):
    x_price_input    = np.arange(x_price_1, x_price_2, 1)
    y_revenue_output = slope_prb*x_price_input**2+ y_intercept*x_price_input
    y_demand_output = slope_prb*x_price_input+ y_intercept
    
    # st.warning("This expander is open when the page loads.")
    # Create traces for each dataset
    linear_re_d_pr=pd.DataFrame({'demand': y_demand_output, 'price': x_price_input})
    
    trace1 = go.Scatter(x= x_price_input,
                        y=linear_re_d_pr["price"],
                        mode="lines",
                        name="price ",
                        line=dict(color="yellow"))
    
    trace2 = go.Scatter(x=x_price_input,
                        y=linear_re_d_pr["demand"],
                        mode="lines",
                        name="demand",
                        line=dict(color="red"),
                        yaxis="y2" )
                        
    trace3 = go.Scatter(x=x_price_input,
                        y=y_revenue_output,
                        mode="lines",
                        name="revenue",
                        line=dict(color="blue"),
                        yaxis="y3" )
                        
    # Define layout with dual axes
    layout = go.Layout(
                        title="Demand VS Price VS Revenue Relationship",
                        xaxis=dict(title="price range"),
                        yaxis=dict(title="price",color='yellow'),
                        yaxis2=dict(title="demand", overlaying="y", side="right",color='red'),
                        yaxis3=dict(title="revenue", overlaying="y", side="right", position=0.5,color='blue') )
                        
    # Combine traces and layout into a figure
    fig = go.Figure(data=[trace1, trace2, trace3], layout=layout)
    fig.update_layout(  legend=dict(
                        yanchor="top",
                        y=1.3,
                        xanchor="left",
                        x=1
                        ))
    st.plotly_chart(fig, use_container_width=True)

    # st.line_chart(linear_re_d_pr)
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
unitx_input=np.arange(0,1000,10)
profit_out=((price_constant - coefficient_unit_x * unitx_input)*unitx_input)-(coefficient_unitx_in_cost*unitx_input + cost_constant)
revenue_out=(price_constant - coefficient_unit_x * unitx_input)*unitx_input
cost_out=(coefficient_unitx_in_cost*unitx_input + cost_constant)

with st.expander("Plot Visualization", expanded=True):
    trace4 = go.Scatter(x=unitx_input,
                        y=profit_out,
                        mode="lines",
                        name="profit",
                        line=dict(color="green"),
                        yaxis="y1" )
    
    trace5 = go.Scatter(x=unitx_input,
                        y=revenue_out,
                        mode="lines",
                        name="revenue",
                        line=dict(color="red"),
                        yaxis="y2" )
        
    trace6 = go.Scatter(x=unitx_input,
                        y=cost_out,
                        mode="lines",
                        name="cost",
                        line=dict(color="yellow"),
                        yaxis="y3" )
                            
    # Define layout with dual axes
    layout = go.Layout(
                        title="Maximizing Profit Based on number of Units Sold",
                        xaxis=dict(title="number of units sold"),
                        yaxis=dict(title="profit",color='yellow'),
                        yaxis2=dict(title="demand", overlaying="y", side="right",color='red'),
                        yaxis3=dict(title="revenue", overlaying="y", side="right", position=0.5,color='blue') )
                        
    # Combine traces and layout into a figure
    fig1 = go.Figure(data=[trace4,trace5 ,trace6], layout=layout)
    fig1.update_layout(     legend=dict(
                            yanchor="top",
                            y=1.3,
                            xanchor="left",
                            x=1))
    st.plotly_chart(fig1, use_container_width=True)
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
