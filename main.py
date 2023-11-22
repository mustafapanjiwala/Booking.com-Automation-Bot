from booking.booking import Booking
import time

try:
    with Booking() as bot:
        bot.land_first_page()
        bot.close_signin_modal()
        # bot.change_currency(currency="USD")
        bot.select_place_to_go(input("Where do you want to go? "))
        bot.select_date(check_in_date=input("Enter Check-in Date: "),check_out_date=input("Enter Check-out Date: "))
        bot.select_adults(count=int(input("No. of Adults: ")))
        # bot.select_children(count=5)
        # bot.select_room(count=3)
        bot.click_search()
        bot.apply_filtrations()
        bot.refresh() #A workaround to get the updated names
        bot.report_results()
except Exception as e:
    print("there is a problem: ",e)

