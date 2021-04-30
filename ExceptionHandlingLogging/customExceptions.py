class OverLimitWithdrawException(Exception):  # Custom exception creation
    def __init__(self, msg):
        self.msg = msg


def withdrawAmount(amt):
    if (amt > 500):
        raise OverLimitWithdrawException("Cannot withdraw over INR 500/-")  # Raising custom exception
    else:
        print("Withdrawal Successful for amount :: ", amt)


withdrawAmount(600)
