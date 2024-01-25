commissionrate_purchase=float(input("Enter commission rate percentage on stock purchase: "))
commissionrate_sale=float(input("Enter commission rate percentage on stock sale: "))
num_sharespurchased=int(input("Enter amount of shares purchased: "))
num_sharessold=int(input("Enter amount of shares sold: "))
purchase_pricepershare=int(input("Enter purchase price per share: "))                    
sell_pricepershare=float(input("Enter sell price per share: "))

amountPaidForStock=num_sharespurchased*purchase_pricepershare
purchaseCommission=commissionrate_purchase*amountPaidForStock
totalPaid=amountPaidForStock + purchaseCommission
stockSoldFor=num_sharespurchased*sell_pricepershare
sellingCommission=commissionrate_purchase*stockSoldFor
totalReceived=stockSoldFor - sellingCommission
profitOrLoss=totalReceived - totalPaid

print("")
display_amountpaidstock = "Amount paid for stock: ${:,.2f}"
print(display_amountpaidstock.format(amountPaidForStock))
display_commissiononpaidpurchase = "Commission paid on the purchase: ${:,.2f}"
print(display_commissiononpaidpurchase.format(purchaseCommission))
display_amountstocksold = "Amount the stock sold for: ${:,.2f}"
print(display_amountstocksold.format(stockSoldFor))
display_commissionpaidsale = "Commission paid on the sale: ${:,.2f}"
print(display_commissionpaidsale.format(sellingCommission))
display_profit = "Profit (or loss if negative): ${:,.2f}"
print(display_profit.format(profitOrLoss))
