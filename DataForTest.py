import concurrent.futures


class FakeOffers:
    def __init__(self, post_name, email):
        self.post_name = post_name
        self.email = email


class FakeInvalidOffers:
    def __init__(self, post_name, link):
        self.post_name = post_name
        self.link = link


def create_fake_data(sendable_offers, test_mail):
    with concurrent.futures.ThreadPoolExecutor() as executor:

        for _ in range(3):
            executor.submit(sendable_offers.append(
                FakeOffers('firefighter', test_mail)))
        print(sendable_offers)
        # executor.submit(sendable_offers.append(
        #     FakeOffers('firefighter', test_mail)) for _ in range(3))
        # print(sendable_offers)
    # for _ in range(3):
    #     sendable_offers.append(AllData('firefighter', test_mail))


def create_fake_invalid_data(non_sendable_offers):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for _ in range(3):
            executor.submit(non_sendable_offers.append(FakeInvalidOffers(
                'firefighter', 'https://google.com')))
        # executor.submit(non_sendable_offers.append(FakeInvalidOffers(
        #     'firefighter', 'https://google.com')) for _ in range(3))
        print(non_sendable_offers)
