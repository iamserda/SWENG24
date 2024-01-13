import datetime
scapital_clients = {}
amex_issued_set = set()
visa_issued_set = set()
master_issued_set = set()


def select_card(pmt_servicer: str) -> str:
    if not pmt_servicer or pmt_servicer not in ['amex', 'visa', 'master']:
        raise ValueError(
            "Card Payment Servicer was not provided. Info logged. Application   will terminate now.")
    servicers_tools = {
        "amex": (amex_factory, amex_issued_set),
        "visa": (visa_factory, visa_issued_set),
        "master": (master_factory, master_issued_set)
    }

    return generate_card(pmt_servicer, servicers_tools[pmt_servicer][0], servicers_tools[pmt_servicer][1])


def generate_card(svc, card_genrator, verifier):
    """generates a new card based on servicer:str, card_generator:def, verifier:set"""
    new_card = card_genrator()
    while new_card in verifier:
        new_card = card_genrator()
    return new_card


def amex_factory():
    """generates a fake amex card"""
    import random
    amex_id = random.randint(32000, 85000)
    group_nums = random.randint(312123, 985430)
    customer_nums = random.randint(32000, 85000)
    return f"{amex_id}-{group_nums}-{customer_nums}"


def visa_factory():
    """generates a fake visa card"""
    import random
    visa_id = random.randint(4100, 4999)
    bank_id = random.randint(1111, 9000)
    group_id = random.randint(1110, 9900)
    client_id = random.randint(1100, 9990)
    return f"{visa_id}-{bank_id}-{group_id}-{client_id}"


def master_factory():
    """ a fake master card generator"""
    import random
    issuer_id = random.randint(5100, 5999)
    group_id1 = random.randint(1111, 9999)
    group_id2 = random.randint(1111, 9999)
    customer_id = random.randint(1111, 9999)
    return f"{issuer_id}-{group_id1}-{group_id2}-{customer_id}"


def issue_card(user_credit):
    if user_credit < 300 or user_credit > 850:
        print("One of our Client Concierge will be with your shorty!")
        return None

    if user_credit >= 720:
        print("Excellent, we can offer you the Deluxe AMEX card. Processing....")
        return select_card("amex")

    if user_credit >= 690:
        print("Excellent, we can offer you our Premium VISA card. Processing....")
        return select_card("visa")

    if user_credit >= 630:
        print("Excellent, we can offer you own of our Premium MASTERCard. Processing....")
        return select_card("master")
