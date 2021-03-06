# Pages Import
import pages.side_bar as side_bar

# Modules Import
import streamlit as st
from streamlit import caching


# Utilities Import
import utilities.requests_server as requests_server
import pages.broker.helperfunctions as hf


"""
    desc: Creates FrontEnd page for the sell part of the broker page using the Streamlit framework.

    author: Luca Weissbeck

    date: 2020-10-14
"""


def run(session_state):
    """
    This method runs the sell part of the broker page by encapsulating every other Streamlit function.

    :param session_state: (Object)
    :test Correct: Method is called using a valid session_state. Incorrect: Method is called without any parameters.
    """
    side_bar.run(session_state)

    st.title("Broker")
    st.subheader(
        "Welcome to your personalised broker. Here you can buy or sell stocks."
    )

    # Switch between BUY and SELL
    mode_switch = st.radio(
        "Please choose whether you want to buy or sell stocks.", ("Buy", "Sell")
    )
    if mode_switch == "Sell":
        st.write("Please choose a stock, that you want to sell.")

        depot_array, depot_information = hf.get_depo_array(session_state.auth_key)
        ticker_code_entry_raw = st.selectbox("Stock ticker:", [" "] + depot_array)
        if ticker_code_entry_raw != " ":
            ticker_code_entry = ticker_code_entry_raw.split(": ")[0]
            quantity_in_user_portfolio = int(hf.get_stock_quantity_in_depot(depot_information, ticker_code_entry))
            if quantity_in_user_portfolio > 1:
                if st.checkbox("Sell all stocks", value=True):
                    # Set the value of quantity to the amount user has in portfolio
                    stock_quantity_for_sale = quantity_in_user_portfolio
                else:
                    col1, col2 = st.beta_columns((4, 1))

                    # Selection of quantity
                    with col1:
                        quantity_input_method_choice = st.radio("Input method:", ("Slider", "Number Input"))

                        # Slider
                        if quantity_input_method_choice == "Slider":
                            stock_quantity_for_sale = st.slider("Please choose the quantity of stocks you want to sell:", 1, quantity_in_user_portfolio)

                        # NumberInput
                        if quantity_input_method_choice == "Number Input":
                            stock_quantity_for_sale_raw = st.number_input(
                                "Please enter the quantity of stocks you want to sell:",
                                min_value=1,
                                max_value=quantity_in_user_portfolio,
                                step=1,
                                value=1,
                            )
                            stock_quantity_for_sale = int(stock_quantity_for_sale_raw)

                    # Quantity in Portfolio for specified stock
                    with col2:
                        st.markdown(
                            """
                                <div class="greyish padding">
                                <h4>Quantity in Depot</h4>
                                <h1 style="text-align:center;">"""
                            + str(quantity_in_user_portfolio)
                            + """</h1>
                                </div>
                                """,
                            unsafe_allow_html=True
                        )
            else:
                stock_quantity_for_sale = quantity_in_user_portfolio

            # Get stockinformation
            single_stock_price = hf.get_single_stock_value(session_state.auth_key, ticker_code_entry)
            selling_fees = hf.get_transaction_fees(session_state.auth_key)
            stock_sell_value_price = round(float(stock_quantity_for_sale * single_stock_price), 2)
            total_sell_value = (str(round((stock_sell_value_price - float(selling_fees)), 2)) + "$")
            stock_description = hf.get_stock_description(session_state.auth_key, ticker_code_entry)
            stock_name = str(stock_description["stockName"])
            dividend_yield = hf.get_dividend_yield(stock_description["dividend"])
            image_source = hf.get_image_url((stock_description["logoUrl"]))
            stock_buyin_price = hf.get_buyin_for_stock(depot_information, ticker_code_entry)

            # Sell Pricing information
            col1, col2 = st.beta_columns(2)
            with col1:
                st.write("---")
                st.subheader("Sell - Overview")
                st.write("---")
                st.write(
                    """<div class="markdown-text-container stMarkdown" style="width: 349px;"><p>Quantity in Portfolio: <b><code style="color: black;">"""
                    + str(stock_quantity_for_sale)
                    + """</code></b></p></div> """,
                    unsafe_allow_html=True,
                )
                st.write(
                    """<div class="markdown-text-container stMarkdown" style="width: 349px;"><p>Transaction Value: <b><code style="color: black;">"""
                    + str(stock_sell_value_price)
                    + "$"
                    + """</code></b></p></div> """,
                    unsafe_allow_html=True,
                )
                st.write(
                    """<div class="markdown-text-container stMarkdown" style="width: 349px;"><p>Selling Fees: <code style="color: #F52D5B;">"""
                    + str(selling_fees)
                    + "$"
                    + """</code></p></div> """,
                    unsafe_allow_html=True,
                )
                st.write("---")
                st.write(hf.gethtml_for_change_buyin_current(stock_buyin_price, single_stock_price), unsafe_allow_html=True)
                st.write(hf.calculate_total_change(stock_buyin_price, single_stock_price, stock_quantity_for_sale), unsafe_allow_html=True)
                st.write("---")
                st.subheader("Total Selling Value:")
                st.title(total_sell_value)

                # Sell button
                if st.button("Sell"):
                    sell_response = requests_server.post_transaction(session_state.auth_key, ticker_code_entry, stock_quantity_for_sale, transaction_type="sell")
                    st.subheader("Sold")
                    caching.clear_cache()
                    session_state.page = "boerse"
                    st.experimental_rerun()

            # Stock Information to the right hand side
            with col2:
                st.write("---")
                st.markdown(
                    """
                                            <div class="greyish padding box">
                                            <h2>Stock Information</h2>
                                            <p>Stock Name: <b>"""
                    + str(stock_name)
                    + """ </b></p>
                                            <p>Single Stock Value: <b>"""
                    + str(single_stock_price)
                    + "$"
                    + """<b></p>
                                            <p>Dividend Yield: <b>"""
                    + str(dividend_yield)
                    + "%"
                    + """<b></p>
                                            <img class = "circle_and_center" src = """
                    + image_source
                    + """>
                                            </div>
                                            """,
                    unsafe_allow_html=True,
                )

    elif mode_switch == "Buy":
        session_state.page = "boerse"
        st.experimental_rerun()
