# Ernest ATM program 
print('')
print('WELCOME TO ERNE MERCHANT BANK\n')
print('************   Please Enter your card to begin.  ************\n')

restart = ('y')
trials = 3
usage_limit = 4
withdrawal_limit = 5

current_balance = 23099

while trials >= 0 :
    pin = int(input('Enter your 4 digit PIN.\n'))
    if pin == (1234) :
        print('CORRECT PIN! WELCOME.\n')
        while restart not in ('n', 'N', 'no', 'NO') : 
            print('Please choose your transction to process\n')
            print('1.  Check Balance')
            print('2.  Withdraw Cash')
            print('3.  Make Payment')
            print('4.  Deposit Cash')
            print('5.  Airtime Top up')
            print('6.  To Return Card\n')
            
            option = int(input(''))
            
            # processing account balance
            if option == 1  : 
                print(f'Your account balance as of today is :K{current_balance}\n')
                restart = input('Press [y] to proceed with other transactions.\nPress [n] if you Want to exit.\n')
                if restart in ('n', 'N', 'no', 'NO') : 
                    print('Thank you for using this ATM. Take your card')
                    break
            # processing cash withdrawal    
            elif option == 2 :
                option2 = ('y')
                while withdrawal_limit >= 0 :
                    withdrawal = float(input('How much would you like to withdraw? Enter amount in multiples of K2000.\n'))
                    #if withdrawal in [2000,4000,6000,8000,10000,12000,14000,16000,20000,24000,28000,30000,40000,50000,60000,70000,80000,90000,100000]:
                    
                    if withdrawal in range(2000, 1000000, 2000) and withdrawal <= current_balance :
                        current_balance = current_balance - withdrawal
                        print(f'Withdrawal successful. Your balance is now {current_balance}\n')
                        restart = input('Want to go back for another withdrawal?\nPress y for yes OR press n for no to exit program.\n')
                        if restart in  ('n', 'N', 'no', 'NO') : 
                            print('Thank you for using this ATM. Take your card')
                            break
                
                        
                    elif withdrawal not in range(2000, 1000000, 2000) : # another option is to use the list (arrays) withdrawal != []
                        print('Withdrawal failed !!\nYour withdrawal amount is not a multiple of K2000. Try again with amount in multiples of K2000.\n')
                        restart = ('y')
                        withdrawal = float(input('How much would like to withdraw? Enter amount in multiples of K2000\n'))
                        if withdrawal in range(2000, 1000000, 2000) and withdrawal <= current_balance :
                            current_balance = current_balance - withdrawal
                            print(f'Withdrawal successful. Your balance is now {current_balance}')
                            restart = input('Want to go back for another withdrawal?\nPress y for yes OR press n for no to exit program.\n')
                            if restart in  ('n', 'N', 'no', 'NO') : 
                                print('Thank you for using this ATM. Take your card')
                                break
                        
                    elif  withdrawal >= current_balance :
                        print('Withdrawal failed !!\nYou have Insufficient funds in your account.')
                        print(f'Try again with amount less than {current_balance}\n')
                        restart = ('y')
                        withdrawal = float(input('How much would like to withdraw? Enter amount in multiples of K2000\n'))
                        if withdrawal in range(2000, 1000000, 2000) and withdrawal <= current_balance :
                            current_balance = current_balance - withdrawal
                            print(f'Withdrawal successful. Your balance is now {current_balance}')
                            restart = input('Want to go back for another withdrawal?\nPress y for yes OR press n for no to exit program.\n')
                            if restart in  ('n', 'N', 'no', 'NO') : 
                                print('Thank you for using this ATM. Take your card')
                                break
                
                    
                    withdrawal_limit -= 1 # same as ( trials = trials - 1  )
                    if withdrawal_limit == 0:
                        print('You have reached the withdrawal limit. Try again the service after 24 hours.\nThank you for using the service.\n\n')
                        break            
            # processing account payments
            elif option == 3 : 
                print('Choose the kind of payment you want to make below?\n')
                payment = int(input('1.\tMRA\n2.\tFuel\n3.\tDSTV\n4.\tWater\n5.\tTuition\n6.\tElectricity\n'))
                # MRA
                if payment == 1 : 
                    # pay as you earn TAX
                    tax_cat = int(input('Choose the Tax to pay\n1.\tPAYE Tax\n2.\tOthers'))
                    if tax_cat == 1 : 
                        cus_gross_pay = float(input('Enter your Take home salary in Malawi kwacha\n'))
                        if cus_gross_pay > 100000 :
                            paye_rate = 0.25
                            taxable =  (cus_gross_pay - 100000)
                            nsonkho = taxable * paye_rate
                            net_salary = cus_gross_pay - nsonkho
                                                                                
                            print("------------------------------------------------------------------------------------------------------")
                            print("Your gross pay is : ",cus_gross_pay , "\nPay as you earn Tax is :",nsonkho,"\nNet pay or take home salary is :", net_salary) 
                            print("------------------------------------------------------------------------------------------------------") 
                            print('Thank you for paying tax. Please wait to get your MRA receipt')
                            
                    
                    elif tax_cat == 2 :
                        # other tax categories
                        tax_amount = float(input('Please anter the amount of tax to pay\.n'))
                        if tax_amount < current_balance :
                            current_balance = current_balance - tax_amount
                            print(f'Tax payment succeful. Thank you for paying your tax amounting to K{tax_amount}.')
                            print(f'Your account balance after tax payment is K{current_balance}.')
                        
                            restart = input('Want to go back for another transaction?\n\nPress y for yes OR press n for no to exit program.\n')
                            if restart in  ('n', 'N', 'no', 'NO') : 
                                print('Thank you for using this ATM. Take your card') 
                                break
                        else :
                                print('Insufficient funds! Deposit the cash into your account first.')
                    else:   
                        print('Ooops ! Invalid input. Try again with correct input')
                                
                # fuel           
                elif payment == 2 :
                    # something about fuel types and prices 
                    print('Fuel payment for :\n')
                    fuel_choice = int(input('1.\tOil\n2.\tPetrol\n3.\tDiesel\n4.\tParaffin\n'))
                    
                    if fuel_choice == 1 :
                        oil_amount_per_litre = 250 # per litre
                        oil_amount = float(input('Enter amount of oil in litres\n'))
                        oil_cash = oil_amount * oil_amount_per_litre
                        if oil_cash < current_balance :                   
                            current_balance = current_balance - oil_cash
                            print(f'Fuel payment succeful. Thank you for buying oil amounting to K{oil_cash}.')
                            print(f'Your account balance after fuel payment is K{current_balance}.')
                            restart = input('Want to go back for another transaction?\nPress y for yes OR press n for no to exit program.\n')
                            if restart in  ('n', 'N', 'no', 'NO') : 
                                print('Thank you for using this ATM. Take your card') 
                                break
                        else :
                            print('Insufficient funds! Try again with less amount of fuel.')
                            
                    # petrol fuel        
                    elif  fuel_choice == 2 :   
                        petro_amount_per_litre = 780 # per litre
                        petro_amount = float(input('Enter amount of oil in litres\n'))
                        petrol_cash = petro_amount * petro_amount_per_litre
                        if petrol_cash < current_balance :                   
                            current_balance = current_balance - petrol_cash
                            print(f'Fuel payment succeful. Thank you for buying petrol amounting to K{petrol_cash}.')
                            print(f'Your account balance after fuel payment is K{current_balance}.')
                            restart = input('Want to go back for another transaction?\nPress y for yes OR press n for no to exit program.\n')
                            if restart in  ('n', 'N', 'no', 'NO') : 
                                print('Thank you for using this ATM. Take your card') 
                                break
                        
                        else :
                            print('Insufficient funds! Try again with less amount of fuel.')
                    
                    elif fuel_choice == 3 :    
                        diesel_amount_per_litre = 725 # per litre
                        diesel_amount = float(input('Enter amount of oil in litres\n'))
                        diesel_cash = diesel_amount * diesel_amount_per_litre
                        if diesel_cash < current_balance :                   
                            current_balance = current_balance - diesel_cash
                            print(f'Fuel payment succeful. Thank you for buying diesel amounting to K{diesel_cash}.')
                            print(f'Your account balance after fuel payment is K{current_balance}.')
                            restart = input('Want to go back for another transaction?\nPress y for yes OR press n for no to exit program.\n')
                            if restart in  ('n', 'N', 'no', 'NO') : 
                                print('Thank you for using this ATM. Take your card') 
                                break
                        
                        else :
                            print('Insufficient funds! Try again with less amount of fuel.')
                            
                    elif fuel_choice == 4 : 
                        parafn_amount_per_litre = 725 # per litre
                        parafn_amount = float(input('Enter amount of oil in litres\n'))
                        parafn_cash = parafn_amount * parafn_amount_per_litre
                        if parafn_cash < current_balance :                   
                            current_balance = current_balance - parafn_cash
                            print(f'Fuel payment succeful. Thank you for buying paraffin amounting to K{parafn_cash}.')
                            print(f'Your account balance after fuel payment is K{current_balance}.')
                            restart = input('Want to go back for another transaction?\nPress y for yes OR press n for no to exit program.\n')
                            if restart in  ('n', 'N', 'no', 'NO') : 
                                print('Thank you for using this ATM. Take your card') 
                                break
                        
                        else :
                            print('Insufficient funds! Try again with less amount of fuel.')  
                    
                    else:
                        print('Invalid input! Please enter the correct number.\n')    
                    
                    
                elif payment == 3 :
                    print('')
                    go_dstv_choice = int(input('1.\tGOtv Package Payment\n2.\tDSTV Package Payment\n'))
                    if go_dstv_choice == 1 : 
                        print('Select GOtv package to make payment for :\n')
                        go_bouk_num = int(input('1.\tLite at K1950 per month.\n2.\tAccess at K3999 per month.\n3.\tPremium at K7500 per month.\n'))
                        if go_bouk_num == 1 : 
                            go_bouk_price = 1950
                            if go_bouk_price < current_balance :
                                current_balance = current_balance - go_bouk_price
                                print(f'Gotv payment succeful. Thank you for payment of a GOtv package amounting to K{go_bouk_price}.\n')
                                print(f'Your account balance after fuel payment is K{current_balance}.\n')
                                restart = input('Want to go back for another transaction?\nPress y for yes OR press n for no to exit program.\n')
                                if restart in  ('n', 'N', 'no', 'NO') : 
                                    print('Thank you for using this ATM. Take your card\n') 
                                    break 
                                
                        elif go_bouk_num == 2 :  
                            go_bouk_price = 3999
                            if go_bouk_price < current_balance :
                                current_balance = current_balance - go_bouk_price
                                print(f'Gotv payment succeful.\nThank you for payment of a GOtv Access package amounting to K{go_bouk_price}.\n')
                                print(f'Your account balance after fuel payment is K{current_balance}.\n')
                                restart = input('Want to go back for another transaction?\nPress y for yes OR press n for no to exit program.\n')
                                if restart in  ('n', 'N', 'no', 'NO') : 
                                    print('Thank you for using this ATM. Take your card\n') 
                                    break
                        
                        elif go_bouk_num == 3 :    
                            go_bouk_price = 7500 # per month
                            if go_bouk_price < current_balance :
                                current_balance = current_balance - go_bouk_price
                                print(f'Gotv payment succeful. Thank you for payment of a GOtv package amounting to K{go_bouk_price}.\n')
                                print(f'Your account balance after fuel payment is K{current_balance}.\n')
                                restart = input('Want to go back for another transaction?\nPress y for yes OR press n for no to exit program.\n')
                                if restart in  ('n', 'N', 'no', 'NO') : 
                                    print('Thank you for using this ATM. Take your card\n') 
                                    break  
                            
                            else:
                                print('Insufficient funds! Try a package with less amount. Or Top up account first\n')
                                    
                    elif go_dstv_choice == 2 :
                        dstv_dec_no = input('Enter your DSTV Decoder number :\t')
                        # DSTV packages and payments
                        print('Select DSTV package to make payment for :\n')
                        dstv_bouk = int(input('1.\tLite at K5350 per month.\n2.\tFamily at K9800 per month.\n3.\tPremium at K21800 per month.\n'))
                        if dstv_bouk == 1 :
                            dstv_bouk_price = 5350 # per month
                            
                            if dstv_bouk_price < current_balance :
                                current_balance = current_balance - dstv_bouk_price
                                print(f'DSTV Payment succeful under Decoder number{dstv_dec_no}.\nSubscription fee is K{dstv_bouk_price} for a Lite Package.')
                                print(f'Your account Balance after DSTV payment is K{current_balance}.\n')
                                restart = input('Want to go back for another transaction?\nPress y for yes OR press n for no to exit program.\n')
                                if restart in  ('n', 'N', 'no', 'NO') : 
                                    print('Thank you for using this ATM. Take your card\n') 
                                    break 
                                
                        elif dstv_bouk == 2 :
                            dstv_bouk_price = 9800 # per month
                            
                            if dstv_bouk_price < current_balance :
                                current_balance = current_balance - dstv_bouk_price
                                print(f'DSTV payment succeful. Thank you for payment of a DSTV package amounting to K{dstv_bouk_price}.\n')
                                print(f'Your account balance after DSTV payment is K{current_balance}.\n')
                                restart = input('Want to go back for another transaction?\nPress y for yes OR press n for no to exit program.\n')
                                if restart in  ('n', 'N', 'no', 'NO') : 
                                    print('Thank you for using this ATM. Take your card\n') 
                                    break  
                                
                        elif dstv_bouk == 3 :
                            dstv_bouk_price = 21800 # per month
                            
                            if dstv_bouk_price < current_balance :
                                current_balance = current_balance - dstv_bouk_price
                                print(f'DSTV payment succeful. Thank you for payment of a DSTV package amounting to K{dstv_bouk_price}.\n')
                                print(f'Your account balance after DSTV payment is K{current_balance}.\n')
                                restart = input('Want to go back for another transaction?\nPress y for yes OR press n for no to exit program.\n')
                                if restart in  ('n', 'N', 'no', 'NO') : 
                                    print('Thank you for using this ATM. Take your card\n') 
                                    break     
                            else :
                                print('Insufficient funds! Try a package with less amount. Or top up account first\n')
                        else:
                            print('Invalid input! Please enter the correct number.\n')    

                                
                elif payment == 4 :
                    # water bill then print successful 
                    meter_no = int(input('Enter your meter number :\t'))
                    water_bill = float(input('Enter the amount to pay for water bill\n'))
                    if water_bill < current_balance :
                        current_balance = current_balance - water_bill 
                        print(f'Water bill Payment succeful under meter number{meter_no}.\nYour current balnce is now {current_balance}')
                        restart = input('Want to go back for another transaction?\nPress y for yes OR press n for no to exit program.\n')
                        if restart in  ('n', 'N', 'no', 'NO') : 
                            print('Thank you for using this ATM. Take your card\n') 
                            break     
                    else :
                        print('Insufficient funds! Try a package with less amount. Or top up account first\n')
                
                                               
                elif payment == 5 :
                    print('Please choose your college to make tuition payment\n')
                    college_choice = int(input('1.\tUNIMA\n2.\tLUANAR\n3.\tMAGU\n4.\tMUST\n5.\tMZUNI\n6.\tCatholic University\n'))
                    if college_choice == 1 :  
                        unima_college = int(input('Select your college under UNIMA\n1.\tChancellor College\n2.\tCollege Of Medicine\n3.\tKamuzu College Of Nursing\n4.\tPolytechnic\n'))
                        if unima_college == 1 :
                            student_acc_no = int(input('Enter your Student Account Number:\t'))
                            tuition_fee = float(input('Enter the amount to pay for tuition:\t'))
                            if tuition_fee < current_balance :   
                                payment_response = int(input(f'Make Tuition Payment to Chanco under Student Account number:{student_acc_no} amounting to: K{tuition_fee}?\n1.\tConfirm\n2.\tCancel\n'))
                                if payment_response == 1 :    
                                    current_balance = current_balance - tuition_fee                  
                                    print(f'Tuition Payment Successful.\nYou paid Tuition to Chanco under student account number:{student_acc_no} amounting to: K{tuition_fee}\nYou account balance is now: K{current_balance}.')
                                
                                    restart = input('Want to go back for another transaction?\nPress y for yes OR press n for no to exit program.\n')
                                    if restart in  ('n', 'N', 'no', 'NO') : 
                                        print('Thank you for using this ATM. Take your card\n') 
                                        break
                                else :
                                    restart = input('Want to go back for another transaction?\nPress y for yes OR press n for no to exit program.\n')
                                    if restart in  ('n', 'N', 'no', 'NO') : 
                                        print('Thank you for using this ATM. Take your card\n') 
                                        break
                                    
                            else :
                                print('Insufficient funds! Try to pay with less amount. Or top up account first\n')
                  
                elif payment == 6 :
                    print('current balance after bill payment')
                
                else:
                    print('Invalid input! Please enter the correct number.\n')  
                      
             # processing cash deposit
            elif option == 4 :
                print(f'Your account balance as of now is: K{current_balance}.\n')   
                cash_deposit = float(input('Now enter amount of cash to deposit in Malawi Kwacha\n')) 
                current_balance = current_balance + cash_deposit 
                print(f'Cash Deposit successful.\nYou have made a cash deposit of {cash_deposit}.') 
                print(f'Your account balance is now: K{current_balance}.')
                print('Thank you for banking with us.')
                restart = input('Want to go back?\n')
                if restart in  ('n', 'N', 'no', 'NO') : 
                    print('Thank you for using this ATM. Take your card') 
                    break

                
             # processing airtime top up        
            elif option == 5 : 
                # network selection
                print('Please select your network service provider below\n')
                network = int(input('1\tTMN\tdirect recharge.\n2\tMTL\tdirect recharge\n3.\tAirtel\tdirect recharge\n'))
                # implementing TNM airtime top
                if network == 1 :
                    recharge_voucher = int(input('Enter airtime amount in Malawi kwacha.\n'))
                    if recharge_voucher in range(100, current_balance) :
                        current_balance = current_balance - recharge_voucher
                        print(f'TNM Airtime purchase successful! You made airtime purchase of K{recharge_voucher}.')
                        print(f'Your account balance is now: K{current_balance}.')
                        restart = input('Want to go back?\n')
                        if restart in  ('n', 'N', 'no', 'NO') : 
                            print('Thank you for using this ATM. Take your card') 
                            break 
                        
                    else:    
                        print('Airtime Recharge failed. Airtime amount out of range.\n')
                # AIRTEL top up
                elif network == 2 :
                    recharge_voucher = int(input('Enter airtime amount in Malawi kwacha.\n'))
                    if recharge_voucher in range(100, current_balance) :
                        current_balance = current_balance - recharge_voucher
                        print(f'MTL Airtime purchase successful! You made airtime purchase of K{recharge_voucher}.')
                        print(f'Your account balance is now: K{current_balance}.')
                        restart = input('Want to go back?\n')
                        if restart in  ('n', 'N', 'no', 'NO') : 
                            print('Thank you for using this ATM. Take your card') 
                            break 
                    
                    else:    
                        print('Airtime Recharge failed. Airtime amount out of range.\n')
                #TNM top up        
                elif network == 3 :
                    recharge_voucher = int(input('Enter airtime amount in Malawi kwacha.\n'))
                    if recharge_voucher in range(100, current_balance) :
                        current_balance = current_balance - recharge_voucher
                        print(f'AIRTEL Airtime purchase successful! You made airtime purchase of K{recharge_voucher}.')
                        print(f'Your account balance is now: K{current_balance}.')
                        restart = input('Want to go back?\n')
                        if restart in  ('n', 'N', 'no', 'NO') : 
                            print('Thank you for using this ATM. Take your card') 
                            break
                
                    else :
                        print('Top up Failed. Either Insufficient Funds or Incorrect input.\nPlease try again with less top amount or correct input')
                        if restart in  ('n', 'N', 'no', 'NO') : 
                            print('Thank you for using this ATM. Take your card') 
                            break
                    
                else:   
                    print('Invalid input. Please try again with correct input') 
                    restart = input('Want to go back?\n')
                    if restart in  ('n', 'N', 'no', 'NO') : 
                        print('Thank you for using this ATM. Take your card') 
                        break                     
            # Returning card
            elif option == 6 :
                print('Please be patient while your card is being returned\n')
                print('Thank you for using this ATM and for banking with us.\n\n')
                print('************   Please Enter your card to begin.  ************')
                break
            
            else:
                print('Invalid input. Please enter a correct number.')
                restart = ('y')
    # validating PIN then Trials  
    elif pin != ('1234'):
        print('Incorrect PIN !!!!\n\nPlease try again carefully.\n')
        trials -= 1 # same as ( trials = trials - 1  )
        if trials == 0:
            print('Too many PIN trials ! Your Account has been disabled\nPlease contact your branch manager or visit your branch for assistance.')
            break
    
          