# 23-24: 4682 -- DATA REPRESENTATION  
Big Project  
Project Type B  
Andras Csullog  
G00411428  

---------------------------------------------------------------------  

## Project Overview:

### Main Objective:

The primary goal of this project is to streamline and enhance the efficiency of our data retrieval and analysis processes. In comparison to manual CSV downloads, my solution offers significant time-saving benefits. The key objectives include:

- **Automated Data Retrieval:** The code to automate the weekly retrieval of essential market intelligence data from HQ Revenue's API.

- **Seamless Integration with PowerBI:** The extracted data seamlessly integrates with Power BI, empowering us to create dynamic and interactive visualizations.

- **Enhanced Decision-Making:** By automating the process, we reduce manual effort, allowing us to focus more on interpreting insights, making informed decisions, and optimizing our corporate travel strategies.

This project is designed to bring about operational efficiency, allowing us to harness the power of data for strategic decision-making.

### On Data provider:

HQ revenue is a company that provides hoteliers with market intelligence and data-driven insights to optimize their revenue strategy. They offer a suite of tools that help hoteliers track market trends, compare their rates to competitors, and make informed pricing decisions.

HQ revenue aggregates data from a variety of sources, including OTAs, metasearch engines, and hotel websites, to provide hoteliers with up-to-date information on market trends, competitor pricing, and occupancy levels.

HQ revenue uses data science to forecast demand for hotels in specific markets. This helps hoteliers plan their staffing and inventory levels accordingly.

### On Data usage:

While I'm not a hotelier, my role is on the other side of the table, working for a corporate travel agency. The insights and data provided by HQ Revenue's API are instrumental in enhancing our corporate travel services. The data empowers us to:

- **Optimize Price Predictions:** Utilize historical and real-time market data to predict prices more accurately.

- **Forecast Company Performance:** Leverage data science and market trends to forecast our company's performance more effectively.

- **Negotiate Competitive Rates:** Make informed decisions during rate negotiations with hotels based on comprehensive market intelligence.

- **Strategic Decision-Making:** Understand demand patterns to make strategic decisions, such as identifying the likelihood of corporate rates being yielded or comparing them to wholesaler rates offered by hoteliers.

This project serves as a valuable tool in streamlining our processes, enhancing our negotiation strategies, and ultimately providing better services to our corporate clients.

## Instructions to run the app:

```
git clone https://github.com/splitcomma/Big_Project.git
```
```
cd Big_Project
```
Create virtual enviroment (optional but recomended):
```
python -m venv venv
```
Ativate virtual enviroment
- On Windows:
```
.\venv\Scripts\activate
```
- On macOS and Linux:
```
source venv/bin/activate
```
### Install dependecies
```
pip install -r requirements.txt
```
Paste config.py file in the working folder consisting API key and Data Base config info sent via email.
(This project utilizes a paid 3rd-party API to retrieve data. While the data returned by the API is not sensitive it comes from a paid service, the API key used for authentication is confidential. To ensure the security of this information, the config.py file containing the API key is not included in this public repository.)

Run Main Program:
```
python BIG_Project_API_db.py
```

## Additional programs to test SQL and db maintanance:
- SQLdelete_table.py
- SQLget_table_names.py
- SQLselect_query

[Results and user-friendly visualization accessible over PowerBI](https://app.powerbi.com/links/IF6DC0UZWe?ctid=47855545-00bb-4800-a65f-e79104ec0fc4&pbi_source=linkShare)






