from bookings.booking import Booking

# With 'with' we can automatically exit the browser

# 'with' comes with a magic function(__exit__()) which
# run when we reach the end of the indentation

try:

    with Booking() as bot:
        bot.land_page()
        # bot.change_currency(currency='inr'.upper())
        bot.select_place_to_go(place_name='dharamshala')
        bot.select_dates(
            check_in_dates='7 December 2021',
            check_out_dates='10 December 2021')
        bot.select_adults(count=1)
        bot.search()
        # bot.start_filtration()
        bot.show_results()

except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '    set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            '    PATH=$PATH:/path/toyour/folder/ \n'
        )
    else:
        raise
