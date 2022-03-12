from GetData import GetData
from HandleData import HandleData
import DataForTest

if __name__ == '__main__':
    sendable_offers = []
    non_sendable_offers = []

    # # ged data from jobs.ge and hr.ge
    # pages_for_jobs = 36
    # pages_for_hr = 8
    # GetData.get_data_from_jobs(
    #     sendable_offers,
    #     non_sendable_offers,
    #     pages_for_jobs
    # )
    # GetData.get_data_from_hr(
    #     sendable_offers,
    #     non_sendable_offers,
    #     pages_for_hr
    # )

    # create data for test
    test_mail = ['testmail@example.com']
    DataForTest.create_fake_data(sendable_offers, test_mail)
    DataForTest.create_fake_invalid_data(non_sendable_offers)

    # send mail and save failed
    applicant_email = 'applicantmail@gmail.com'
    applicant_password = 'applicanpasswprd123'
    HandleData.send_mail(
        applicant_email,
        applicant_password,
        sendable_offers
    )
    HandleData.save_data(non_sendable_offers)
