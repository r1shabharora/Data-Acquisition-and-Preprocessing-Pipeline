

names=[]
prices=[]
changes=[]
percentChanges=[]
marketCaps=[]
totalVolumes=[]
circulatingSupplys=[]

CryptoCurrenciesUrl = "https://finance.yahoo.com/gainers"
for i in range(0,11):
    CryptoCurrenciesUrl ="https: //in. finance .yahoo.com/most-active?of fset="+str(i)+"&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp ; amp ; amP;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;count=18"
    r= requests.get(CryptoCurrenciesUr1)
    data=r.text
    soup=BeautifulSoup(data)

for listing in soup.find_all(‘tr', attrs={'class' :'SimpleDataTableRow' }) :
for name in listing.find_all(‘td', attrs={'aria-label' :'Name'}):
names . append (name. text)
for price in listing.find_all('td', attrs={'aria-label':'Price
(intraday) '}):
prices. append(price. find(' span’). text)
for change in listing.find_all('td', attrs={‘aria-label' :'Change'}):
changes . append( change. text)
for percentChange in listing.find_all('td', attrs={'aria-label’:
change’ }) :
percentChanges . append(percentChange. text)
for marketCap in listing.find_all(‘td’, attrs={‘aria-label' :'Market
cap'}):
marketCaps .append(marketCap.text)
for totalVolume in listing.find_all('td', attrs={'aria-label’:'Avg vol
(3-month) '}) :
totalVolumes.append(totalVolume.text)
for circulatingSupply in listing.find_all(‘td’,
attrs={'aria-label' :'Volume' }) :
circulatingSupplys.append(circulatingSupply.text)

 



