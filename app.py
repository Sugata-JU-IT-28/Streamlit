import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide",page_title="Startup Funding Analysis")
df = pd.read_csv('startup_cleaned.csv')

df['date'] = pd.to_datetime(df['date'],format="%d/%m/%Y",errors="coerce")
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month_name()


def load_overall_analysis():
    st.title('Overall Analysis')

    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month_name()

    # total invested amount
    total = round(df['amount'].sum())

    # max amount infused in a startup
    max_funding = df.groupby('startup')['amount'].max().sort_values(ascending=False).head(1).values[0]

    # avg ticket size -> ek company mei avg kitna paisa lagaya hai
    avg_funding = df.groupby('startup')['amount'].sum().mean()

    # total funded startups
    num_startups = df['startup'].nunique()
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric('Total', str(total) + ' Cr')
    with col2:
        st.metric('Max', str(max_funding) + 'Cr')
    with col3:
        st.metric('Avg', str(round(avg_funding)) + ' Cr')
    with col4:
        st.metric('Funded Startups', num_startups)

    st.header('MoM graph')
    selected_option = st.selectbox('Select Type', ['Total', 'Count'])
    if selected_option == 'Total':
        temp_df = df.groupby(['year', 'month'])['amount'].sum().reset_index()
    else:
        temp_df = df.groupby(['year', 'month'])['amount'].count().reset_index()

    temp_df['x_axis'] = temp_df['month'].astype('str') + '-' + temp_df['year'].astype('str')

    #fig3, ax3 = plt.subplots()
    #ax3.plot(temp_df['x_axis'], temp_df['amount'])
    #st.pyplot(fig3)

    fig3, ax3 = plt.subplots(figsize=(12, 5))

    ax3.plot(temp_df['x_axis'], temp_df['amount'])

    ax3.set_xticks(ax3.get_xticks()[::3])  # show every 3rd label
    plt.xticks(rotation=90)

    plt.tight_layout()

    st.pyplot(fig3)


investor_set = set(
    x.strip()
    for item in df["investors"].dropna().astype(str)
    for x in item.split(",")
    if x.strip() != ""
)

def load_investor_detail(investor):
    st.title(investor)
    #load recent 5 investments of the investor
    last5_df = df[df['investors'].str.contains(investor)].head()[['date', 'startup', 'vertical', 'city', 'round', 'amount']]
    st.subheader('Most Recent Investments')
    st.dataframe(last5_df)

    col1, col2 = st.columns(2)
    with col1:
        #biggest investments
        big_series = df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head()
        st.subheader('Biggest Investments')
        fig, ax = plt.subplots()
        ax.bar(big_series.index, big_series.values)
        st.pyplot(fig)

    with col2:
        vertical_series = df[df['investors'].str.contains(investor)].groupby('vertical')['amount'].sum()
        st.subheader('Sectors invested in')
        fig1, ax1 = plt.subplots()
        ax1.pie(vertical_series, labels=vertical_series.index, autopct="%0.01f%%")

        st.pyplot(fig1)

    col3, col4 = st.columns(2)
    with col3:
        city = df[df['investors'].str.contains(investor)].groupby('city')['amount'].sum()
        st.subheader('Cities invested in')
        fig2, ax2 = plt.subplots()
        ax2.pie(city, labels=city.index, autopct="%0.01f%%")

        st.pyplot(fig2)

    with col4:
        df['year'] = df['date'].dt.year
        year_series = df[df['investors'].str.contains(investor)].groupby('year')['amount'].sum()
        st.subheader('Years invested in')
        fig3, ax3 = plt.subplots()
        ax3.plot(year_series.index, year_series.values)

        st.pyplot(fig3)

def load_startup_detail(startup):
    st.title(startup)

    startup_df = df[df['startup'] == startup].sort_values('date', ascending=False)

    if startup_df.empty:
        st.warning("No data found for this startup.")
        return

    latest_row = startup_df.iloc[0]

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Name", latest_row['startup'])
    with col2:
        st.metric("Industry", latest_row['vertical'])
    with col3:
        st.metric("City", latest_row['city'])
    with col4:
        st.metric("Founders", "Not available")

    st.subheader("Funding Details")

    funding_table = startup_df[['round', 'investors', 'date']].copy()
    funding_table.columns = ['Funding Round Stage', 'Investors', 'Date']
    funding_table['Date'] = funding_table['Date'].dt.date

    st.dataframe(funding_table, use_container_width=True)

st.sidebar.title('Startup Funding Analysis')

option = st.sidebar.selectbox('Select one', ['Overall Analysis', 'StartUp', 'Investor'])


if option == 'Overall Analysis':
    load_overall_analysis()

elif option == 'StartUp':
    selected_startup = st.sidebar.selectbox('Select Startup', sorted(df['startup'].dropna().unique().tolist()))
    btn1 = st.sidebar.button('Find Startup Details')
    if btn1:
        load_startup_detail(selected_startup)
else:
    selected_investor = st.sidebar.selectbox('Select Investor',investor_set)
    btn2 = st.sidebar.button('Find Investor Details')
    if btn2:
        load_investor_detail(selected_investor)
    # st.title('Investor Analysis')