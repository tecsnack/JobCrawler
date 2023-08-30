import requests
from bs4 import BeautifulSoup
import csv
import operator
from fuzzywuzzy import fuzz
from difflib import get_close_matches

# Synonyme und Variationen der Fähigkeiten
keywords = ['Python', 'Webentwicklung', 'Datenbanken', 'Frontend-Entwicklung', 'Programmierung']

def crawl_job_sites(keywords):
    job_sites = ['https://example1.com', 'https://example2.com']  # Liste der Jobbörsen-Websites

    with open('job_listings.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Jobtitel', 'Beschreibung', 'Unternehmen', 'Veröffentlicht am', 'Link']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for site in job_sites:
            response = requests.get(site)
            soup = BeautifulSoup(response.text, 'html.parser')

            job_listings = soup.find_all('div', class_='job-listing')  # HTML-Elemente, die Jobangebote enthalten

            for job in job_listings:
                job_title = job.find('h2').text
                job_description = job.find('p').text
                company = job.find('span', class_='company').text
                posted_date = job.find('span', class_='posted-date').text
                job_link = job.find('a')['href']

                # Überprüfe, ob das Jobangebot den gesuchten Fähigkeiten entspricht
                matched_keywords = []
                for keyword in keywords:
                    if keyword in job_description:
                        matched_keywords.append(keyword)
                    elif any(fuzz.partial_ratio(keyword, skill) >= 80 for skill in job_description.split()):
                        matched_keywords.append(keyword)
                    elif get_close_matches(keyword, job_description.split(), n=1, cutoff=0.8):
                        matched_keywords.append(keyword)

                if matched_keywords:
                    writer.writerow({'Jobtitel': job_title, 'Beschreibung': job_description,
                                     'Unternehmen': company, 'Veröffentlicht am': posted_date, 'Link': job_link})

# Beispielaufruf des Crawlers mit den gewünschten Fähigkeiten
crawl_job_sites(keywords)
