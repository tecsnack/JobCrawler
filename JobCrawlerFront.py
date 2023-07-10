import requests
from bs4 import BeautifulSoup
import csv

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
                if any(keyword in job_description for keyword in keywords):
                    writer.writerow({'Jobtitel': job_title, 'Beschreibung': job_description,
                                     'Unternehmen': company, 'Veröffentlicht am': posted_date, 'Link': job_link})

# Beispielaufruf des Crawlers mit den gewünschten Fähigkeiten
keywords = ['Python', 'Webentwicklung', 'Datenbanken']
crawl_job_sites(keywords)