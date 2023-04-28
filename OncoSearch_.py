#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests as requests
from bs4 import BeautifulSoup
from selenium import webdriver



# # 1st website
base = 'https://faculty.mdanderson.org/'
parameters = 'profiles/seungtaek_choi.html'
url = base + parameters
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
# # Name
data = soup.find('h1').text
mdName1 = data[:-6]
# # mdSpecialty
mdSpecialty1='Genitourinary_Oncologist'
# # School
mdSchool1 = soup.find('body').find("td").find_next_sibling("td").text[:-33]
# # resLink
for p in soup.find('body').find_all('div', attrs={'class' : 'faculty-publications'}):
    resLink1 = p.a['href']
# # Hospital name
div = soup.find('div', 'mda-nav-top flex-row')
img = div.find('img', alt=True)
mdFacility1 = img['alt']
# # facilityZip
base = 'https://www.mdanderson.org/'
parameters = 'about-md-anderson/our-locations/texas-medical-center.html'
url = base + parameters
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
div = soup.find('body').find('div', {'class': 'panel-content'})
data = div.find('p').text.split()
for i in range(len(data)):
    i = i+5
    facilityZip1 = data[i]
    break
        


# In[3]:


# # 2nd Website
base = 'https://www.mskcc.org/'
parameters = 'cancer-care/doctors/borys-mychalczak'
url = base + parameters
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
# # mdName
data = soup.find('h1').text
mdName2 = data[:-4]
# # mdSpecialty
mdSpecialty2='Genitourinary Oncologist'
# # mdSchool
mdSchool2 = soup.find('div', 'about-me__text-column').find('p').text[4:]
# # mdFacility
url = base
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
div = soup.find('div', 'msk-site-navigation__masthead')
mdFacility2 = div.title.text
# # facilityZip
parameters = 'contact'
url = base + parameters
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
div = soup.find('div', 'msk-markup')
data = div.find('p').find_next_sibling("p").text.split()
for i in range(len(data)):
    i = i+13
    facilityZip2 = data[i]
    break
# # resLink
response = requests.get('https://pubmed.ncbi.nlm.nih.gov/?cmd=search&term=((neoplasms%5BMH%5D+OR+cancer%5BTW%5D)+OR+sloan-kettering+AND+Mychalczak+B)')
soup = BeautifulSoup(response.content, 'html.parser')
link = 'https://pubmed.ncbi.nlm.nih.gov'
for p in soup.find_all('div', attrs={'class' : 'docsum-content'}):
    resLink2 = link + p.a['href']
    break

# # 3rd website
base = 'https://www.mskcc.org/'
parameters = 'cancer-care/doctors/dhwani-parikh'
url = base + parameters
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
# # Name
data = soup.find('h1').text
mdName3 = data[:-4]
# # mdSpecialty
mdSpecialty3='Genitourinary Oncologist'
# # mdSchool
mdSchool3 = soup.find('div', 'about-me__text-column').find('p').text[4:]
# # mdFacility
div = soup.find('div', 'msk-site-navigation__masthead')
mdFacility3 = div.title.text
# # facilityZip
facilityZip3 = "07920"
# # resLink
parent = soup.find('ul', attrs={'class' : 'msk-list msk-list--unordered'})
resLink3 = base + parent.a['href']



# # 4th website
base = 'https://physiciandirectory.brighamandwomens.org/'
parameters = 'details/163/anthony-damico-cancer_-_radiation_oncology-radiation_oncology-boston'
url = base + parameters
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
# # Name
data = soup.find('h1').text.strip()
mdName4 = data[:-9]
# # mdSpecialty
mdSpecialty4='Genitourinary Oncologist'
# # School
div = soup.find('div', {'id':'accordion-education'}).findAll('div', {'class': 'profileData'})
for span in range(len(div)):
    span = span + 1
    data = div[span].text
    mdSchool4 = data.strip()[:-6]
    break
# # resLink
resLink4 = 'https://www.researchgate.net/publication/369381976_Cribriform_morphology_is_associated_with_higher_risk_of_biochemical_recurrence_after_radical_prostatectomy_in_patients_with_Grade_Group_5_prostate_cancer'
# # mdFacility
div = soup.find('div', 'container-fluid iw_section')
img = div.find('img', alt=True)
mdFacility4 = img['alt'][:-5]
# # facilityZip
data = soup.find('div', 'footer__contact-info').find('address').text.split()
for i in range(len(data)):
    i = i+5
    facilityZip4 = data[i]
    break



# # 5th website
base = 'https://www.dana-farber.org/'
parameters = 'find-a-doctor/jennifer-r-bellon/'
url = base + parameters
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
# # Name
data = soup.find('h2').text
mdName5 = data[:-4]
# # mdSpecialty
mdSpecialty5='Breast Oncologist '
# # School
parent = soup.find("body").find("div", {'class': 'doctor-accomplishments'}).find('ul', {'id':'ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder1_MedicalSchoolList'})
mdSchool5 = parent.li.text
# # resLink
link = 'https://pubmed.ncbi.nlm.nih.gov'
for p in soup.find_all('div', attrs={'id' : 'ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder1_headingTWO'}):
     resLink5 = link + p.a['href']
# # mdFacility
logo = soup.find('body').find('figure', {'class': 'logo'})
img = logo.find('img', alt=True)
mdFacility5 = img['alt']
# # facilityZip                                                                                                                                                                                                                                                                          
div = soup.find('body').find('div', {'id': 'ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder1_LocationsList'})
data = div.p.text.split()
for i in range(len(data)):
    i = i+6
    facilityZip5 = data[i][:5]
    break


# # 7th website
base = 'https://www.med.upenn.edu/'
parameters = 'apps/faculty/index.php/g275/p8199210'
url = base + parameters
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
# # Name
data = soup.find('h2').text
mdName7 = data[:-6]
# # mdSpecialty
mdSpecialty7='Genitourinary Oncologist'
# # School
data = soup.find('body').find('div', {'class': 'fac_education'}).find('span').find_next_sibling("span").text
mdSchool7 = data[10:-21].strip()[:-1]
# # Hospital
logo = soup.find('body').find('a', {'class': 'logo'})
img = logo.find('img', alt=True)
mdFacility7 = img['alt']
# # facilityZip
data = soup.find('body').find('section', {'class': 'contact one-third unit'}).p.text.split()
for i in range(len(data)):
    i = i+15
    facilityZip7 = data[i]
    break
# # resLink
response = requests.get('https://pubmed.ncbi.nlm.nih.gov/?term=bekelman+j')
soup = BeautifulSoup(response.content, 'html.parser')
link = 'https://pubmed.ncbi.nlm.nih.gov'
for p in soup.find_all('div', attrs={'class' : 'docsum-content'}):
    resLink7 = link + p.a['href']
    break



# # 8th website

base = 'https://www.mayoclinic.org/'
parameters = 'biographies/ahmed-safia-k-m-d/bio-20433784'
url = base + parameters
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
# # Name
data = soup.find('h1').text
mdName8 = "Safia K. Ahmed"
# # mdSpecialty
mdSpecialty8='Breast Oncologist'
# # School
span = soup.find('body').find_all('span', {'class': 'bio-subtext'})
for i in range(len(span)):
    i = i+1
    data = span[i].text
    break
mdSchool8 = "Mayo Clinic College of Medicine"
# # facilityZip
facilityZip8 = "55902"
# # mdFacility
mdFacility8 = "Mayo Clinic"
# # resLink
resLink8 = 'http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=pubmed&dopt=Abstract&list_uids=36573830&query_hl=11&itool=pubmed_docsum'





# # 9th website
response = requests.get('https://www.mayoclinic.org/biographies/attia-albert-n-m-d/bio-20535394')
soup = BeautifulSoup(response.content, 'html.parser')
# # Name
data = soup.find('h1').text
mdName9 = "Albert N. Attia"
# # mdSpecialty
mdSpecialty9='Genitourinary Oncologist'
# # School
span = soup.find('body').find_all('span', {'class': 'bio-subtext'})
for i in range(len(span)):
    i = i+1
    data = span[i].text
    break
mdSchool9 = "Wake Forest University School of Medicine"
# # facilityZip
facilityZip9 = ("32224")
# # mdFacility
mdFacility9 = "Mayo Clinic"
# # resLink
response = requests.get('https://pubmed.ncbi.nlm.nih.gov/?term=albert+attia')
soup = BeautifulSoup(response.content, 'html.parser')
link = 'https://pubmed.ncbi.nlm.nih.gov'
parent = soup.find('body').find('article', {'class': 'full-docsum'})
resLink9 = link + parent.a['href']

# # 10th website
base = 'https://faculty.mdanderson.org/'
parameters = 'profiles/karen_hoffman.html'
url = base + parameters
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
# # Name
data = soup.find('h1').text
mdName10= data[:-6]
# # mdSpecialty
mdSpecialty10='Breast Oncologist'
# # School
mdSchool10= soup.find('body').find("td").find_next_sibling("td").text[:-33]
# # resLink
for p in soup.find('body').find_all('div', attrs={'class' : 'faculty-publications'}):
    resLink10= p.a['href']
# # Hospital name
div = soup.find('div', 'mda-nav-top flex-row')
img = div.find('img', alt=True)
mdFacility10= img['alt']
# # facilityZip
base = 'https://www.mdanderson.org/'
parameters = 'about-md-anderson/our-locations/texas-medical-center.html'
url = base + parameters
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
div = soup.find('body').find('div', {'class': 'panel-content'})
data = div.find('p').text.split()
for i in range(len(data)):
    i = i+5
    facilityZip10= data[i]
    break

# # 11th website
base = 'https://www.med.upenn.edu/'
parameters = 'apps/faculty/index.php/g275/p8461884'
url = base + parameters
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
# # Name
data = soup.find('h2').text
mdName11= data[:-6]
# # mdSpecialty
mdSpecialty11='Breast Oncologist'
# # School
data = soup.find('body').find('div', {'class': 'fac_education'}).find('span').find_next_sibling("span").text
mdSchool11= "Temple University School of Medicine"
# # Hospital
logo = soup.find('body').find('a', {'class': 'logo'})
img = logo.find('img', alt=True)
mdFacility11= img['alt']
# # facilityZip
data = soup.find('body').find('section', {'class': 'contact one-third unit'}).p.text.split()
for i in range(len(data)):
    i = i+15
    facilityZip11= data[i]
    break
# # resLink
response = requests.get('https://pubmed.ncbi.nlm.nih.gov/?term=bekelman+j')
soup = BeautifulSoup(response.content, 'html.parser')
link = 'https://pubmed.ncbi.nlm.nih.gov'
for p in soup.find_all('div', attrs={'class' : 'docsum-content'}):
    resLink11= link + p.a['href']
    break

# # 12th website
base = 'https://faculty.mdanderson.org/'
parameters = 'profiles/deborah_kuban.html'
url = base + parameters
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
# # Name
data = soup.find('h1').text
mdName12 = data[:-6]
# # mdSpecialty
mdSpecialty12='Genitourinary Oncologist'
# # School
mdSchool2 = soup.find('body').find("td").find_next_sibling("td").text[:-33]
# # resLink
for p in soup.find('body').find_all('div', attrs={'class' : 'faculty-publications'}):
    resLink12 = p.a['href']
# # Hospital name
div = soup.find('div', 'mda-nav-top flex-row')
img = div.find('img', alt=True)
mdFacility12 = img['alt']
# # facilityZip
base = 'https://www.mdanderson.org/'
parameters = 'about-md-anderson/our-locations/texas-medical-center.html'
url = base + parameters
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
div = soup.find('body').find('div', {'class': 'panel-content'})
data = div.find('p').text.split()
for i in range(len(data)):
    i = i+5
    facilityZip12 = data[i]
    break

# # 13th website
base = 'https://faculty.mdanderson.org/'
parameters = 'profiles/sean_mcguire.html'
url = base + parameters
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
# # Name
data = soup.find('h1').text
mdName13 = data[:-6]
# # mdSpecialty
mdSpecialty13='Genitourinary Oncologist'
# # School
mdSchool3 = soup.find('body').find("td").find_next_sibling("td").text[:-33]
# # resLink
for p in soup.find('body').find_all('div', attrs={'class' : 'faculty-publications'}):
    resLink13 = p.a['href']
# # Hospital name
div = soup.find('div', 'mda-nav-top flex-row')
img = div.find('img', alt=True)
mdFacility13 = img['alt']
# # facilityZip
base = 'https://www.mdanderson.org/'
parameters = 'about-md-anderson/our-locations/texas-medical-center.html'
url = base + parameters
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
div = soup.find('body').find('div', {'class': 'panel-content'})
data = div.find('p').text.split()
for i in range(len(data)):
    i = i+5
    facilityZip13 = data[i]
    break

# # 14th website
base = 'https://faculty.mdanderson.org/'
parameters = 'profiles/henry_mok.html'
url = base + parameters
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
# # Name
data = soup.find('h1').text
mdName14 = data[:-6]
# # mdSpecialty
mdSpecialty14='Genitourinary Oncologist'
# # School
mdSchool4 = soup.find('body').find("td").find_next_sibling("td").text[:-33]
# # resLink
for p in soup.find('body').find_all('div', attrs={'class' : 'faculty-publications'}):
    resLink14 = p.a['href']
# # Hospital name
div = soup.find('div', 'mda-nav-top flex-row')
img = div.find('img', alt=True)
mdFacility14 = img['alt']
# # facilityZip
base = 'https://www.mdanderson.org/'
parameters = 'about-md-anderson/our-locations/texas-medical-center.html'
url = base + parameters
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
div = soup.find('body').find('div', {'class': 'panel-content'})
data = div.find('p').text.split()
for i in range(len(data)):
    i = i+5
    facilityZip14 = data[i]
    break

# # 15th website
base = 'https://faculty.mdanderson.org/'
parameters = 'profiles/henry_mok.html'
url = base + parameters
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
# # Name
data = soup.find('h1').text
mdName15 = data[:-6]
# # mdSpecialty
mdSpecialty15='Genitourinary Oncologist'
# # School
mdSchool5 = soup.find('body').find("td").find_next_sibling("td").text[:-33]
# # resLink
for p in soup.find('body').find_all('div', attrs={'class' : 'faculty-publications'}):
    resLink15 = p.a['href']
# # Hospital name
div = soup.find('div', 'mda-nav-top flex-row')
img = div.find('img', alt=True)
mdFacility15 = img['alt']
# # facilityZip
base = 'https://www.mdanderson.org/'
parameters = 'about-md-anderson/our-locations/texas-medical-center.html'
url = base + parameters
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
div = soup.find('body').find('div', {'class': 'panel-content'})
data = div.find('p').text.split()
for i in range(len(data)):
    i = i+5
    facilityZip15 = data[i]
    break

# # 16th website
base = 'https://faculty.mdanderson.org/'
parameters = 'profiles/chad_tang.html'
url = base + parameters
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
# # Name
data = soup.find('h1').text
mdName16 = data[:-6]
# # mdSpecialty
mdSpecialty16='Genitourinary Oncologist'
# # School
mdSchool6 = soup.find('body').find("td").find_next_sibling("td").text[:-33]
# # resLink
for p in soup.find('body').find_all('div', attrs={'class' : 'faculty-publications'}):
    resLink16 = p.a['href']
# # Hospital name
div = soup.find('div', 'mda-nav-top flex-row')
img = div.find('img', alt=True)
mdFacility16 = img['alt']
# # facilityZip
base = 'https://www.mdanderson.org/'
parameters = 'about-md-anderson/our-locations/texas-medical-center.html'
url = base + parameters
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
div = soup.find('body').find('div', {'class': 'panel-content'})
data = div.find('p').text.split()
for i in range(len(data)):
    i = i+5
    facilityZip16 = data[i]
    break

# # 17th website
base = 'https://faculty.mdanderson.org/'
parameters = 'profiles/pamela_schlembach.html'
url = base + parameters
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
# # Name
data = soup.find('h1').text
mdName17 = data[:-6]
# # mdSpecialty
mdSpecialty17='Breast Oncologist'
# # School
mdSchool7 = soup.find('body').find("td").find_next_sibling("td").text[:-33]
# # resLink
for p in soup.find('body').find_all('div', attrs={'class' : 'faculty-publications'}):
    resLink17 = p.a['href']
# # Hospital name
div = soup.find('div', 'mda-nav-top flex-row')
img = div.find('img', alt=True)
mdFacility16 = img['alt']
# # facilityZip
base = 'https://www.mdanderson.org/'
parameters = 'about-md-anderson/our-locations/texas-medical-center.html'
url = base + parameters
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
div = soup.find('body').find('div', {'class': 'panel-content'})
data = div.find('p').text.split()
for i in range(len(data)):
    i = i+5
    facilityZip17 = data[i]
    break

# # 18th website
base = 'https://www.mskcc.org/'
parameters = 'cancer-care/doctors/lior-braunstein'
url = base + parameters
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
# # Name
data = soup.find('h1').text
mdName18 = data[:-4]
# # mdSpecialty
mdSpecialty18='Breast Oncologist'
# # mdSchool
mdSchool18 = soup.find('div', 'about-me__text-column').find('p').text[4:]
# # mdFacility
div = soup.find('div', 'msk-site-navigation__masthead')
mdFacility18 = div.title.text
# # facilityZip
facilityZip18 = "07645"
# # resLink
parent = soup.find('ul', attrs={'class' : 'msk-list msk-list--unordered'})
resLink18 = base + parent.a['href']


# # 19th website
base = 'https://www.mskcc.org/'
parameters = 'cancer-care/doctors/beryl-mccormick'
url = base + parameters
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
# # Name
data = soup.find('h1').text
mdName19 = data[:-4]
# # mdSpecialty
mdSpecialty19='Breast Oncologist'
# # mdSchool
mdSchool19 = soup.find('div', 'about-me__text-column').find('p').text[4:]
# # mdFacility
div = soup.find('div', 'msk-site-navigation__masthead')
mdFacility19 = div.title.text
# # facilityZip
facilityZip19 = "07748"
# # resLink
parent = soup.find('ul', attrs={'class' : 'msk-list msk-list--unordered'})
resLink19 = "https://pubmed.ncbi.nlm.nih.gov/31750868"

# # 20th website
base = 'https://www.mskcc.org/'
parameters = 'cancer-care/doctors/simon-powell'
url = base + parameters
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
# # Name
data = soup.find('h1').text
mdName20 = data[:-4]
# # mdSpecialty
mdSpecialty20='Breast Oncologist'
# # mdSchool
mdSchool20 = soup.find('div', 'about-me__text-column').find('p').text[4:]
# # mdFacility
div = soup.find('div', 'msk-site-navigation__masthead')
mdFacility20 = div.title.text
# # facilityZip
facilityZip20 = "10065"
# # resLink
parent = soup.find('ul', attrs={'class' : 'msk-list msk-list--unordered'})
resLink20 = "https://pubmed.ncbi.nlm.nih.gov/33834176"

# # 21st website
response = requests.get('https://www.mayoclinic.org/biographies/ahmed-safia-k-m-d/bio-20433784')
soup = BeautifulSoup(response.content, 'html.parser')
# # Name
data = soup.find('h1').text
mdName21 = "Safia K. Ahmed"
# # mdSpecialty
mdSpecialty21='Breast Oncologist'
# # School
span = soup.find('body').find_all('span', {'class': 'bio-subtext'})
for i in range(len(span)):
    i = i+1
    data = span[i].text
    break
mdSchool21= "Mayo Clinic College of Medicine"
# # facilityZip
facilityZip21 = ("55902")
# # mdFacility
mdFacility21 = "Mayo Clinic"
# # resLink
response = requests.get('https://pubmed.ncbi.nlm.nih.gov/?term=albert+attia')
soup = BeautifulSoup(response.content, 'html.parser')
link = 'https://pubmed.ncbi.nlm.nih.gov'
parent = soup.find('body').find('article', {'class': 'full-docsum'})
resLink21 = link + parent.a['href']

# # 22nd website
response = requests.get('https://www.mayoclinic.org/biographies/leenstra-james-l-m-d/bio-20182086')
soup = BeautifulSoup(response.content, 'html.parser')
# # Name
data = soup.find('h1').text
mdName22 = "James L. Leenstra"
# # mdSpecialty
mdSpecialty22='Genitourinary Oncologist'
# # School
span = soup.find('body').find_all('span', {'class': 'bio-subtext'})
for i in range(len(span)):
    i = i+1
    data = span[i].text
    break
mdSchool22= "Mayo Clinic College of Medicine"
# # facilityZip
facilityZip22 = ("55902")
# # mdFacility
mdFacility22 = "Mayo Clinic"
# # resLink
response = requests.get('https://pubmed.ncbi.nlm.nih.gov/?term=albert+attia')
soup = BeautifulSoup(response.content, 'html.parser')
link = 'https://pubmed.ncbi.nlm.nih.gov'
parent = soup.find('body').find('article', {'class': 'full-docsum'})
resLink22 = link + parent.a['href']


# # 23rd website
response = requests.get('https://www.mayoclinic.org/biographies/corbin-kimberly-s-m-d/bio-20163919')
soup = BeautifulSoup(response.content, 'html.parser')
# # Name
data = soup.find('h1').text
mdName23 = "Kimberly S. Corbin"
# # mdSpecialty
mdSpecialty23='Breast Oncologist'
# # School
span = soup.find('body').find_all('span', {'class': 'bio-subtext'})
for i in range(len(span)):
    i = i+1
    data = span[i].text
    break
mdSchool23= "University of Rochester School of Medicine and Dentistry"
# # facilityZip
facilityZip23 = ("55902")
# # mdFacility
mdFacility23 = "Mayo Clinic"
# # resLink
response = requests.get('https://pubmed.ncbi.nlm.nih.gov/?term=albert+attia')
soup = BeautifulSoup(response.content, 'html.parser')
link = 'https://pubmed.ncbi.nlm.nih.gov'
parent = soup.find('body').find('article', {'class': 'full-docsum'})
resLink23 = link + parent.a['href']

# # 24th website
response = requests.get('https://www.mayoclinic.org/biographies/may-byron-c-m-d/bio-20138357')
soup = BeautifulSoup(response.content, 'html.parser')
# # Name
data = soup.find('h1').text
mdName24 = "Byron C. May"
# # mdSpecialty
mdSpecialty24='Genitourinary Oncologist'
# # School
span = soup.find('body').find_all('span', {'class': 'bio-subtext'})
for i in range(len(span)):
    i = i+1
    data = span[i].text
    break
mdSchool24= "Tulane College of Medicine"
# # facilityZip
facilityZip24 = ("32224")
# # mdFacility
mdFacility24 = "Mayo Clinic"
# # resLink
response = requests.get('https://pubmed.ncbi.nlm.nih.gov/?term=albert+attia')
soup = BeautifulSoup(response.content, 'html.parser')
link = 'https://pubmed.ncbi.nlm.nih.gov'
parent = soup.find('body').find('article', {'class': 'full-docsum'})
resLink24 = link + parent.a['href']


# # 25th website
base = 'https://www.dana-farber.org/'
parameters = 'find-a-doctor/fallon-chipidza/'
url = base + parameters
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
# # Name
data = soup.find('h2').text
mdName25 = data[:-4]
# # mdSpecialty
mdSpecialty25='Breast Oncologist '
# # School
parent = soup.find("body").find("div", {'class': 'doctor-accomplishments'}).find('ul', {'id':'ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder1_MedicalSchoolList'})
mdSchoo25 = parent.li.text
# # resLink
link = 'https://pubmed.ncbi.nlm.nih.gov'
for p in soup.find_all('div', attrs={'id' : 'ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder1_headingTWO'}):
     resLink25 = link + p.a['href']
# # mdFacility
logo = soup.find('body').find('figure', {'class': 'logo'})
img = logo.find('img', alt=True)
mdFacility25 = img['alt']
# # facilityZip                                                                                                                                                                                                                                                                          
div = soup.find('body').find('div', {'id': 'ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder1_LocationsList'})
data = div.p.text.split()
for i in range(len(data)):
    i = i+6
    facilityZip25 = data[i][:5]
    break


# # 26th website
base = 'https://www.dana-farber.org/'
parameters = 'find-a-doctor/homan-mohammadi/'
url = base + parameters
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
# # Name
data = soup.find('h2').text
mdName26 = data[:-4]
# # mdSpecialty
mdSpecialty26='Genitourinary Oncologist '
# # School
parent = soup.find("body").find("div", {'class': 'doctor-accomplishments'}).find('ul', {'id':'ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder1_MedicalSchoolList'})
mdSchoo26 = parent.li.text
# # resLink
link = 'https://pubmed.ncbi.nlm.nih.gov'
for p in soup.find_all('div', attrs={'id' : 'ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder1_headingTWO'}):
     resLink26 = link + p.a['href']
# # mdFacility
logo = soup.find('body').find('figure', {'class': 'logo'})
img = logo.find('img', alt=True)
mdFacility26 = img['alt']
# # facilityZip                                                                                                                                                                                                                                                                          
div = soup.find('body').find('div', {'id': 'ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder1_LocationsList'})
data = div.p.text.split()
for i in range(len(data)):
    i = i+6
    facilityZip26 = data[i][:5]
    break





# # Pandas DataFrame
mdName = [mdName1,mdName2,mdName3,mdName4,mdName5,mdName7,mdName8,mdName9,mdName10,mdName11,mdName12,mdName13,mdName14,mdName15, mdName16, mdName17, mdName18, mdName19, mdName20,mdName21,mdName22, mdName23, mdName24, mdName25, mdName26]
mdSpecialty = [mdSpecialty1,mdSpecialty2, mdSpecialty3, mdSpecialty4, mdSpecialty5, mdSpecialty7, mdSpecialty8, mdSpecialty9, mdSpecialty10, mdSpecialty11, mdSpecialty12, mdSpecialty13, mdSpecialty14, mdSpecialty15, mdSpecialty16, mdSpecialty17, mdSpecialty18, mdSpecialty19, mdSpecialty20, mdSpecialty21, mdSpecialty22, mdSpecialty23, mdSpecialty24, mdSpecialty25, mdSpecialty26]
mdSchool = [mdSchool,mdSchool2,mdSchool3,mdSchool4,mdSchool5,mdSchool7,mdSchool8,mdSchool9,mdSchool10,mdSchool11, mdSchool12, mdSchool13, mdSchool14, mdSchool15, mdSchool16,mdSchool17,mdSchool18,mdSchool19,mdSchool20, mdSchool21,mdSchool22,mdSchool23,mdSchool24,mdSchool25, mdSchool26]
mdFacility = [mdFacility1,mdFacility2,mdFacility3,mdFacility4,mdFacility5,mdFacility7,mdFacility8,mdFacility9,mdFacility10,mdFacility11,mdFacility12, mdFacility13, mdFacility14, mdFacility15, mdFacility16, mdFacility17, mdFacility18, mdFacility19, mdFacility20, mdFacility21, mdFacility22, mdFacility23, mdFacility24, mdFacility25, mdFacility26]
facilityZip = [facilityZip1,facilityZip2,facilityZip3,facilityZip4,facilityZip5,facilityZip7,facilityZip8,facilityZip9,facilityZip10,facilityZip11, facilityZip12, facilityZip13, facilityZip14, facilityZip15, facilityZip16, facilityZip17, facilityZip18, facilityZip19, facilityZip20, facilityZip21, facilityZip22, facilityZip23, facilityZip24, facilityZip25, facilityZip26]
resLink = [resLink1,resLink2,resLink3,resLink4,resLink5,resLink7,resLink8,resLink9,resLink10,resLink11, resLink12, resLink13, resLink14, resLink15, resLink16, resLink17, resLink18, resLink19, resLink20, resLink21, resLink22, resLink23, resLink24, resLink25, resLink26]
scrapped_data = {'mdName':mdName, 'mdSpecialty': mdSpecialty,'mdSchool': mdSchool,'mdFacility': mdFacility, 'facilityZip': facilityZip,'resLink': resLink}

df=pd.DataFrame(scrapped_data)
print(df)
df.to_csv('scrapped_data.csv', index=False)
print("Csv created successfully")

import streamlit as st



st.set_page_config(page_title='OncoSearch')
st.header('OncoSearch')
st.subheader('Search for the best genitourinary or breast radiation oncologist near you')
st.dataframe(df)
text_search = st.text_input("Search for an oncologist by specialty, name, or facility")
m1=df["mdSpecialty"].str.contains(text_search)
m2=df["mdName"].str.contains(text_search)
df_search=df[m1|m2]
if text_search:
    st.write(df_search)
    
st.sidebar.title("Information included in this database:")
st.sidebar.info(
    "mdName – Physician’s Name\n\n"
    "mdSpecialty – Physician’s specialty (Genitourinary or Breast Cancer)\n\n"
    "mdSchool – The school the physician attended\n\n"
    "mdFacility – The facility where the physician practices\n\n"
    "resLink – A link to the physician’s latest research related to the specific cancer type\n\n")




# In[ ]:





# In[ ]:




