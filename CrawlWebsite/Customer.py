class Customer:
    def __init__(self, mallName, orderNum, invoiceNum, recipientName, recipientNum, recipientHnum, address, zipCode, shipMessage, orderName, orderCode, orderAmount, price, shipFee, orderTotal, option):
        self.option = option
        self.price = price
        self.orderTotal = orderTotal
        self.shipFee = shipFee
        self.orderAmount = orderAmount
        self.orderCode = orderCode
        self.orderName = orderName
        self.zipCode = zipCode
        self.address = address
        self.recipientHnum = recipientHnum
        self.recipientNum = recipientNum
        self.recipientName = recipientName
        self.invoiceNum = invoiceNum
        self.orderNum = orderNum
        self.mallName = mallName
        self.shipMessage = shipMessage


