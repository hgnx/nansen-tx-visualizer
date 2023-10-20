# Nansen TX Visualizer with Labels from Arkham

The Nansen TX Visualizer with Labels from Arkham allows you to gain deep insights into ERC-20 token transactions by combining data from Nansen and Arkham Intelligence. It provides a visual representation of token transfers, including sender and recipient addresses, transaction values, and transaction times. What sets it apart is the ability to overlay these transaction markers directly on the Binance price chart, making visualization more intuitive and informative.

## Features

- Fetches detailed information about ERC-20 token transactions, including sender and recipient addresses, token addresses, values, and timestamps from Nansen.
- Enhances Nansen data by incorporating Arkham Intelligence labels. These labels provide insights into the entities and labels associated with each address, allowing for a deeper understanding of token transactions.
- Retrieves historical price data for a specific token from Binance, enabling users to analyze transaction activity in the context of token price movements.
- Utilizes Plotly to generate interactive visualizations, facilitating a better grasp of transaction patterns.
- Overlay markers on the custom price chart for a more comprehensive view of transaction activity.

## Setup

- Before running the main script (`main.ipynb`), configure your Nansen API token using the `setup.py` script. You will be prompted to provide your Nansen API token, which will be stored in a config.ini file for the main script to reference.

- _Note: Nansen only provides API token to paid users._

## Installation and Usage

1. Download the project code.
```
git clone https://github.com/hgnx/nansen-tx-visualizer.git
```

2. Install the required libraries.
```
pip install -r requirements.txt
```

3. Get the api token from Nansen.
    - 3-1. Log in to [Nansen Query](https://query.nansen.ai/users/me).
    - _Note: Nansen only provides API token to paid users._

4. Run the setup script and enter your Nansen API token.
```
python setup.py
```

5. In `main.ipynb`, assign the token name(ETHUSDT, etc) to the `TOKEN_NAME` variable and its ERC-20 wallet address to the `TOKEN_ADDRESS` variable.
   - TOKEN_NAME must be listed on Binance.
   - TOKEN_ADDRESS must always start with "0x".

6. Run each cell.

## Example
  
![alt text](https://github.com/hgnx/nansen-tx-visualizer/blob/main/output.png?raw=true)

## Disclaimer
This script is for informational purposes only and should not be used as the basis for any financial decisions. I take no responsibility for any personal financial loss. Use this script at your own risk.