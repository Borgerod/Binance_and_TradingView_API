# Binance_and_TradingView_API
[Previous Upwork Job] as consultant regarding an Issue with API and RSI calculation. 


## Summary
- Language: Python
- Job type: Consultation 
- Job categogy: API integration, Finance


## Project description
Binance/Tradingview RSI calculation
The Client was searching for an expert to decipher RSI calculation on Binance/Tradingview platforms because the recommended formula were not matching to the public data feed on the platforms.

The first thing I overruled was data recieved from Tradingview since Tradingviews's data comes from Binanve and any data recieved from Tradingview would naturally be to a greater extent more delayed, than fetching the data straight from the source. 
I took a look at it and concluded that the timestamps on the API output was wrong (displayed one interval into the future) so the comparison would always be wrong, I also concluded with that the API's were not powerfull enough to gather all of the data in time (data leak), especially during periods of high traffic.
So I found an alternative API solution, which gave a much accurate output.

In the Pdf attachment; "written explaination.pdf" you'll find the letter I sent to my costumer, further explaining my findings. 


## ScreenShots
![image](https://user-images.githubusercontent.com/97392841/174435658-2b6bc390-cbdc-4767-a6b0-2f33568c9e03.png)

