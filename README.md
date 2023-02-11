# Binance_and_TradingView_API
[Previous Upwork Job] as consultant regarding an Issue with API and RSI calculation. 


## Summary
- Job Completed:  February 2022
- Job type:				Consultation 
- Job categogy:		API integration, Finance
- Language:				Python


#Norwegian description:
rådgivning; optimalisering av datastrøm
Oppdragsgiver ville opprinnelig at jeg skulle lage en kode som hentet aksjedata fra to platformer uten å bruke API. Oppdragsgiver var missfornøyd med API'en da han la merke til at dataen (RSI, Relative Strength Index) fra de to trading platformene ikke matchet med hverandre. Jeg forklarte han at det ikke ville være mulig da en API snakker direkte med serveren. Jeg ville gi han et ordentlig svar han kunne bruke så jeg utforsket dypere. Jeg analyserte med å gjøre to ting; jeg sammenlignet datastrømmen fra APIene (Platform A vs Platform B), i tillegg til å sammenlignet jeg datastrømmen mellom API og platform (selve bruker UIen på nettsiden). Jeg fikk bekreftet at dataen ikke matchet, (funn 1) det var de samme tallene (innenfor et viss slingringsrom) men at datastrømmen fra den ene platformen "lagget" med 15 minutter i forhold til den andre. (funn 2) grunnen var at platform A hentet dataen sin fra Platform B, istedenfor å hente dataen direkte fra kilden, så platform A's datastrømø hadde en mellommann som skapte "laggen". Når jeg justerte tiden på platform A og sammenlignet dem på nytt igjen, lå differansen på gjsn 0.08$, altså en reduksjon på 93%.Det meste av den resterende differansen på 0.08 konkluderte jeg kom i fra "laggen" som kommer fra tiden det tar for platformens server å sende informasjonen (API) VS hvor fort det tar å laste inn dataen på nettsiden. Som kan variere etter en rekke faktorer, derav; hvor mye traffikk platformen generellt opplever, og trafikken som kilden opplever, mengden handelsaktivitet for det gitte produktet.  Jeg la til at den ene platformen har muligens en feil eller annen måte å kalkulere RSI (Relative Strength Index) på, som gir de mer/mindre presise tall. 




## Project description
Binance/Tradingview RSI calculation
The Client was searching for an expert to decipher RSI calculation on Binance/Tradingview platforms because the recommended formula were not matching to the public data feed on the platforms.

The first thing I overruled was data recieved from Tradingview since Tradingviews's data comes from Binanve and any data recieved from Tradingview would naturally be to a greater extent more delayed, than fetching the data straight from the source. 
I took a look at it and concluded that the timestamps on the API output was wrong (displayed one interval into the future) so the comparison would always be wrong, I also concluded with that the API's were not powerfull enough to gather all of the data in time (data leak), especially during periods of high traffic.
So I found an alternative API solution, which gave a much accurate output.

In the Pdf attachment; "written explaination.pdf" you'll find the letter I sent to my costumer, further explaining my findings. 


## ScreenShots
![image](https://user-images.githubusercontent.com/97392841/174435658-2b6bc390-cbdc-4767-a6b0-2f33568c9e03.png)

