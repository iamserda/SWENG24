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
