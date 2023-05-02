import openai
import json
import requests
import streamlit as st


openai.api_key="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"

def BasicGeneration(Prompt):
    completion=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role":"user","content":Prompt}
        ]
    )
    return completion.choices[0].message.content

st.title('ChatGPT Advanced Prompting with Python')
st.subheader(
    'Example :Analyzing Live Crypto Prices')


def GetBitcoinPrizes():
    #Define the API endpoint and query parameters
    url = "https://coinranking1.p.rapidapi.com/coin/Qwsogvtv82FCd/history"
    querystring = {"referenceCurrencyUuid":"yhjMzLPhuIDl","timePeriod":"7d"}

    #define the request headers with API key and Host
    headers = {
	"X-RapidAPI-Key": "44ecca8ea1msh452f73cde7f5781p13860ejsn51abf62f4178",
	"X-RapidAPI-Host": "coinranking1.p.rapidapi.com"
    }

    #Send a GET request to the API endpoint with query parameters and headers
    response = requests.request(
        "GET",url, headers=headers, params=querystring)
    #Parse the response data as a JSON object
    JSONResult =json.loads(response.text)
    #Extract the "history" feild from the JSON response
    history=JSONResult["data"]["history"]
    #extract the "price" field from element in the "history" array and add to a lisr
    prices=[]
    for change in history:
        prices.append(change["price"])
    #Join the list of prices into a coma-separated string
    pricesList=','.join(prices)
    #Return the comma-separated string of prices
    return pricesList





if st.button("Analysis"):
    with st.spinner('Getting Bitcoin Prices'):
        bitcoinprices=GetBitcoinPrizes()
        st.success("Done !")
    with st.spinner('Anlysis Bitcoin Prices'):
        chatGPTPrompt=f"""You are a expert crypto trader with more than 10 years of experience
        I will provide you with a list of bitcoin prices for the last 5 days
        can you provide me with a technical analysis 
        of bitcoin based on these prices .here is what I want:
        Price Overview,
        Moving Averages,
        Relative Strength Index(RSI),
        Moving Average Convergence Divergence (MACD),
        Advice and suggestion,
        Do I buy or sell?,
        PLease be as detailed as much as you can , and explain in a way any beginner can understand and here is the 
        price list :{bitcoinprices}   """
        analysis=BasicGeneration(chatGPTPrompt)
        st.text_area("analyis",analysis,
                     height=550)
        st.success("Done !")

    