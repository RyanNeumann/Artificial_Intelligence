from bs4 import BeautifulSoup
import urllib
import pandas as pd
import pandas as np

price = []
where = []
bed = []
bath = []
size = []
monthly = []
street = []

for x in range (0,1500):
	url = package_url_rent(str(x))
	r = urllib.urlopen(url).read()
	soup = BeautifulSoup(r,'html.parse')
	lst = soup.find_all(lambda tag: tag.has_attr('data-id'))
	for i in range(len(lst)):
		#Determine Price
		if lst[i].find_all('span',{'class':'details_info'}) == []:
			price.append(' ')
		else:
			price.append(lst[i].find_all('span',{'class':'price'})[0].string)
		
		#Determine Where
		length = len(lst[i].find_all('div',{'class':'details_info'}))
		if (lst[i].find_all('div',{'class':'details_info'})[0].find_all('a',href=True)==[]):
			if (length==1):
				where.append(' ')
			else: 
				if((lst[i].find_all('div',{'class':'detail_info'}))[1].find_all('a', href=True)==[]):
					where.append(' ')
				else:
					where.append(lst[i].find_all('div',{'class':'details_info'})[1].find_all('a',href=True)[0].string)
		else:
			where.append(lst[i].find_all('div',{'class':'details_info'})[0].find_all('a', href = True)[0].string)
		
		#Determine Amount of Bedrooms
		if(lst[i].find_all('span',{'class':'detail_cell'}) == []):
			bed.append(' ')
		else:
			bed.append(lst[i].find_all('span',{'class':'detail_cell'})[0].string
		
		#Determine Amount of Bathrooms	
		if(lst[i].find_all('span',{'class':'detail_cell'}==[]):
			bed.append(' ')
		else:
			bed.append(lst[i].find_all('span',{'class':'detail_cell'})==[0].string)
		
		#Determine Size
		if(lst[i].find_all('span',{'class':'detail_cell'})==[]):
			size.append(' ')
		else:
			size.append(lst[i].find_all('span', {'class':'last_detail_cell')}[0].string)
		
		#Determine Rent
		rent.append(lst[i].find_all('div',{'class':'details_title'}).[0].a.string)
		
print price
print where
print bed
print bath
print size
print rent
print street
print "Completed"