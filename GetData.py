import requests
from bs4 import BeautifulSoup
from time import sleep
from SendableOffers import SendableOffers
from NonSendableOffers import NonSendableOffers


class GetData():

    def get_all_job_offers_from_jobs(job_offers, sendable_offers, non_sendable_offers):
        for job_offer in job_offers:
            job_offer_name = job_offer.get_text()
            sleep(1)
            job = requests.get(f'https://www.jobs.ge/{job_offer["href"]}')
            job_soup = BeautifulSoup(job.text, 'html.parser')
            emails_html = job_soup.find(
                class_='dtable').find_all('tr')[3].find_all('a')
            email = [
                email_html for email_html in emails_html if email_html['href'][:6] == 'mailto']
            if email != []:
                sendable_offers.append(
                    SendableOffers(job_offer_name, email)
                )
            else:
                non_sendable_offers.append(NonSendableOffers(
                    job_offer_name,
                    f'https://www.jobs.ge/{job_offer["href"]}'))

    def get_all_job_offers_from_hr(jobs, sendable_offers, non_sendable_offers):
        for job in jobs:
            job_offer_name = job.find(class_='title__text').get_text()
            job_offer_url = job['href']
            sleep(1)
            job_offer = requests.get(f'https://www.hr.ge/{job_offer_url}')
            soup2 = BeautifulSoup(job_offer.text, 'html.parser')

            try:
                email_banner = soup2.find(
                    class_='application-email-phone-address')
                email = email_banner.find(
                    class_='application__email').find_all('span')[1].get_text()
            except:
                non_sendable_offers.append(
                    NonSendableOffers(
                        job_offer_name, f'https://www.hr.ge/{job_offer_url}')
                )
                continue

            sendable_offers.append(SendableOffers(job_offer_name, email))

    def get_single_job_offer_from_jobs(job_offers, sendable_offers, non_sendable_offers):
        job_offer = job_offers[0]
        job_offer_name = job_offer.get_text()
        sleep(1)
        job = requests.get(f'https://www.jobs.ge/{job_offer["href"]}')
        job_soup = BeautifulSoup(job.text, 'html.parser')
        emails_html = job_soup.find(class_='dtable').find_all('tr')[
            3].find_all('a')
        email = [
            email_html for email_html in emails_html if email_html['href'][:6] == 'mailto']
        if email != []:
            sendable_offers.append(SendableOffers(job_offer_name, email))
        else:
            non_sendable_offers.append(NonSendableOffers(
                job_offer_name, f'https://www.jobs.ge/{job_offer["href"]}'))

    def get_single_job_offer_from_hr(jobs, sendable_offers, non_sendable_offers):
        job = jobs[0]
        job_offer_name = job.find(class_='title__text').get_text()
        job_offer_url = job['href']
        sleep(1)
        job_offer = requests.get(f'https://www.hr.ge/{job_offer_url}')
        soup2 = BeautifulSoup(job_offer.text, 'html.parser')

        try:
            email_banner = soup2.find(
                class_='application-email-phone-address')
            email = email_banner.find(
                class_='application__email').find_all('span')[1].get_text()
            sendable_offers.append(SendableOffers(job_offer_name, email))
        except:
            non_sendable_offers.append(
                NonSendableOffers(
                    job_offer_name,
                    f'https://www.hr.ge/{job_offer_url}'
                ))

    def get_data_from_jobs(sendable_offers, non_sendable_offers, pages):
        for page in range(pages+1):
            whole_page = requests.get(
                f'https://www.jobs.ge/?page={page}&q=&cid=0&lid=0&jid=0&in_title=0&has_salary=0&is_ge=0&for_scroll=yes')
            page_soup = BeautifulSoup(whole_page.text, 'html.parser')
            job_offers = page_soup.find_all(class_='vip')

            '''get data for single job'''
            # GetData.get_single_job_offer_from_jobs(job_offers, sendable_offers, non_sendable_offers)

            '''get data for all jobs'''
            GetData.get_all_job_offers_from_jobs(
                job_offers,
                sendable_offers,
                non_sendable_offers
            )

    def get_data_from_hr(sendable_offers, non_sendable_offers, pages):
        for page in range(pages+1):
            hr = requests.get(f'https://www.hr.ge/search-posting?pg={page}')
            soup = BeautifulSoup(hr.text, 'html.parser')
            jobs_table = soup.find(class_='ann')
            jobs = jobs_table.find_all(class_='title')

            '''get data for single job'''
            # GetData.get_single_job_offer_from_hr(jobs, sendable_offers, non_sendable_offers)

            '''get data for all jobs'''
            GetData.get_all_job_offers_from_hr(
                jobs,
                sendable_offers,
                non_sendable_offers
            )
