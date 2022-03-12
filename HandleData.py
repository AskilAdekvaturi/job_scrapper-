from importlib.metadata import files
import smtplib
from email.message import EmailMessage
from csv import writer
import concurrent.futures


class HandleData:
    def create_mail(applicant_email, subject, to):
        files = ['archil_gotsiridze_CV.pdf', 'არჩილ_გოცირიძე_CV.pdf']

        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = applicant_email
        msg['To'] = to
        msg.set_content('')

        for file in files:
            with open(file, 'rb') as file:
                file_data = file.read()
                file_name = file.name

            msg.add_attachment(
                file_data, maintype='application',
                subtype='octet-stream',
                filename=file_name
            )
        return msg

    def send_mail(applicant_email, my_password, sendable_offers):
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(applicant_email, my_password)

            for post in sendable_offers:
                smtp.send_message(HandleData.create_mail(
                    applicant_email, post.post_name, post.email
                ))

    def save_data(non_sendable_offers):
        with open('names.csv', 'w', newline='', encoding='UTF8') as csvfile:
            csv_writer = writer(csvfile)
            csv_writer.writerow(
                ['post_name', 'link']
            )
            with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.submit(csv_writer.writerow(
                    [post.post_name, post.link]) for post in non_sendable_offers)
