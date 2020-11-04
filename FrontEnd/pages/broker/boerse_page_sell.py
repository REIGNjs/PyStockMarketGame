# Pages Import
import pages.side_bar as side_bar

# Modules Import
import streamlit as st

# Utilities Import
import utilities.requests_server as requests_server


def run(session_state):
    side_bar.run(session_state)

    # Load CSS File for Formatting
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
    local_css("FrontEnd/css/style.css")

    st.header("Broker")
    st.subheader("Welcome to your personalised broker. Here you can buy and sell your stocks.")

    # switch between BUY and SELL
    mode_switch = st.radio("Please choose whether you want to buy or sell stocks", ("Buy", "Sell"))

    if mode_switch == "Sell":
        st.write("Please choose the stock, that you want to sell.")

        # Get the stock from user, which he / she wants to sell
        ticker_code_entry = st.selectbox("WKN:", [" "] + session_state.stock_names)
        if ticker_code_entry != " ":
            ticker_code_entry_for_post_request = ticker_code_entry.split(": ")[1]
            # Connect to Database later!!!
            quantity_of_specific_stock_in_depot = 6

            if st.checkbox("Sell all stocks", value=True):
                # Set the Value of quantity to the amount user has in Depot
                stock_quantity = 6

            else:
                # Site is split Die Seite wird aufgeteilt, sodass der User auf der rechten Seite eine Angabe hat, wie viele Aktien er von der ausgewählten Aktie im Depot hat
                col1, col2 = st.beta_columns((4, 1))

                # Selection of quantity
                with col1:
                    # Sollte der User eine genau Anzahl eingeben wollen, so kann er hier "textfeld" auswaehlen
                    quantity_input_method_choice = st.radio("Input method", ("Slider", "Textfield"))

                    # Slider
                    if quantity_input_method_choice == "Slider":
                        stock_quantity = st.slider("Please choose the quantity of stocks", 1, 6)

                    # Textfeld & Button
                    if quantity_input_method_choice == "Textfield":
                        stock_quantity_raw = st.number_input("Please choose the quantity of stocks", min_value=1,
                                                             step=1)
                        stock_quantity = 1
                        if st.button("Apply"):
                            stock_quantity = int(stock_quantity_raw.title())

                # Anzeige der Quantitaät der ausgewaählten Aktie im Depot
                with col2:
                    st.markdown("""
                            <div class="greyish padding">
                            <h4>Quantity in Depot</h4>
                            <h1>""" + str(quantity_of_specific_stock_in_depot) + """</h1>
                            </div>
                            """, unsafe_allow_html=True)

            # Vorbereiten der Seitenaufteilung und Variablen für den Kauf:
            col1, col2 = st.beta_columns(2)

            # Get stockinformation
            stock_description = requests_server.get_stock_description(session_state.auth_key,
                                                                      ticker_code_entry_for_post_request)
            stock_sell_value_price = stock_quantity * 169.88
            selling_fees = 9.90
            total_sell_value = str(stock_sell_value_price - selling_fees) + "€"

            # Auflistung Verkaufspreis mit Ordergebühren
            with col1:
                st.subheader("Sell - Overview")
                st.write("----------------------")
                st.write("Stock value:", stock_sell_value_price)
                st.write("Selling fees: -", selling_fees)
                st.write("----------------------")
                st.subheader("Total selling value:")
                st.title(total_sell_value)

                # Sell button
                if st.button("Sell"):
                    st.subheader("Sold")
                    response = requests_server.post_transaction(session_state.auth_key,
                                                                ticker_code_entry_for_post_request,
                                                                stock_quantity, transactionType="sell")

            # Aktieninformationen neben der Verkaufsauflistung anzeigen
            with col2:
                stock_name = str(stock_description["stockName"])
                dividend_yield_raw = stock_description["dividend"]
                if dividend_yield_raw != "N/A":
                    dividend_yield = str(int(dividend_yield_raw) * 100)
                else:
                    dividend_yield = "N/A"
                image_source = stock_description["logoUrl"]

                st.markdown("""
                                            <div class="greyish padding">
                                            <h2>Stock Information</h2>
                                            <p>Stock name: <b>""" + stock_name + """ </b></p>
                                            <p>Stock value: <b>""" + "190" + """<b></p>
                                            <p>Dividendyield: <b>""" + dividend_yield + """<b></p>
                                            <img class = "circle_and_center" src = """ + image_source + """>
                                            </div>
                                            """, unsafe_allow_html=True)

    elif mode_switch == "Buy":
        session_state.page = "boerse"
        st.experimental_rerun()
