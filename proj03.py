    ###########################################################

    #  Computer Project #3

    #    tuition calculator  

    #    input resident/international

    #    input level

    #       input college

    #           input credits
    
    # ------------> calculate tuition
    ##########################################################
    
print("2019 MSU Undergraduate Tuition Calculator.")  

INPUT = "Do you want to do another calculation (yes/no): "
while True:
    RESIDENT = input("\nResident (yes/no): ").lower()
    RESIDENT = str(RESIDENT) # convert to string for if statements (done to all future inputs)
    
    if RESIDENT == 'yes':
        LEVEL = input("Level—freshman, sophomore, junior, senior: ").lower() #.lower for all inputs so that all cases can be inputed 
        LEVEL = str(LEVEL)
        while LEVEL != 'freshman' and LEVEL != 'sophomore' and LEVEL != 'junior' and LEVEL != 'senior': # to test if the input is valid or not 
            print("Invalid input. Try again.")
            LEVEL = input("Level—freshman, sophomore, junior, senior: ").lower()
            LEVEL = str(LEVEL)
        if LEVEL == 'freshman' or LEVEL == 'sophomore': # for freshman and sophomores same questions are asked, so they are in the same if statement 
            COLLEGE = 'none' # not admitted to any college yet, so it must be defined as none
            ENG = input("Are you admitted to the College of Engineering (yes/no): ").lower()
            ENG = str(ENG)
            if ENG == 'yes':
                EXTRA = 670  # extra charges per college (done to all future charges to calculate tuition)
            else:
                EXTRA = 0 
            JMC = input("Are you in the James Madison College (yes/no): ").lower()
            JMC = str(JMC)
            if JMC == 'yes':
                EXTRA = 7.50 
            else:
                EXTRA = 0
        if LEVEL == 'junior' or LEVEL == 'senior': # juniors and seniors have the same questions asked 
            COLLEGE = input("Enter college as business, engineering, health, sciences, or none: ").lower()
            COLLEGE = str(COLLEGE)
            if COLLEGE == 'business':
                EXTRA = 226
            if COLLEGE == 'engineering':
                EXTRA = 670
            if COLLEGE == 'health':
                EXTRA = 100
            if COLLEGE == 'sciences':
                EXTRA = 100
            if COLLEGE == 'none':
                EXTRA = 0
            CME = input("Is your major CMSE (“Computational Mathematics and Engineering”) (yes/no): ").lower()
            CME = str(CME)
            if CME == 'yes':
                EXTRA = 670  
                JMC = input("Are you in the James Madison College (yes/no): ")
                JMC = str(JMC)
                if JMC == 'yes':
                    EXTRA = 7.50
                else:
                    EXTRA = 675
        CREDITS = input("Credits: ") # input the number of credits 
        while CREDITS.isdigit() == False or CREDITS == '0': # to make sure that invalid inputs are NOT taken in, but they are reprompted 
            if "." in CREDITS:
                print("Invalid input. Try again.")
                CREDITS = input("Credits: ")
            if CREDITS.isdigit() == False:
                print("Invalid input. Try again.")
                CREDITS = input("Credits: ")
            if CREDITS <= '0':
                print("Invalid input. Try again.")
                CREDITS = input("Credits: ")
        if CREDITS.isdigit() == True:
            CREDITS = int(CREDITS)      # only if it is an integer, change it from a string to an int  
            # perform calculations 
            if CREDITS >= 1 and CREDITS <= 11:
                if LEVEL == 'freshman':
                    CREDIT_TUITION = (CREDITS * 482)
                    TUITION = 24 
                    print("Tuition is $" + str("{:,.2f}".format(CREDIT_TUITION + TUITION + EXTRA) + "."))     # string formatting for the numbers to have commas in the right palces          
                if LEVEL == 'sophomore':
                    CREDIT_TUITION = (CREDITS * 494)
                    TUITION = 24 
                    print("Tuition is $" + str("{:,.2f}".format(CREDIT_TUITION + TUITION + EXTRA) + ".")) 
            if CREDITS >= 1 and CREDITS <= 11:
                if LEVEL == 'junior' or LEVEL == 'senior':
                    if COLLEGE == 'engineering' or COLLEGE == 'business':
                        CREDIT_TUITION = (CREDITS * 573)
                        TUITION = 24
                        print("Tuition is $" + str("{:,.2f}".format(CREDIT_TUITION + TUITION + EXTRA) + ".")) 
                    else:
                        CREDIT_TUITION = (CREDITS * 555)
                        TUITION = 24
                        print("Tuition is $" + str("{:,.2f}".format(CREDIT_TUITION + TUITION + EXTRA) + "."))   
                        
                            
            if CREDITS >= 12 and CREDITS <= 18:
                 if LEVEL == 'freshman':
                     CREDIT_TUITION = 7230
                     TUITION = 29 
                     print("Tuition is $" + str("{:,.2f}".format(CREDIT_TUITION + TUITION + EXTRA) + "."))   
                 if LEVEL == 'sophomore':
                    CREDIT_TUITION = 7410
                    TUITION = 29 
                    print("Tuition is $" + str("{:,.2f}".format(CREDIT_TUITION + TUITION + EXTRA) + "."))  
                    
            if CREDITS >= 12 and CREDITS <= 18:
                if LEVEL == 'junior' or LEVEL == 'senior':
                    if COLLEGE == 'business' or COLLEGE == 'engineering':
                        CREDIT_TUITION = 8595
                        TUITION = 29
                        print("Tuition is $" + str("{:,.2f}".format(CREDIT_TUITION + TUITION + EXTRA) + ".")) 
                    else:
                        CREDIT_TUITION = 8325
                        TUITION = 29
                        print("Tuition is $" + str("{:,.2f}".format(CREDIT_TUITION + TUITION + EXTRA) + ".")) 
                        
            if CREDITS > 18:
                if LEVEL == 'freshman':
                    CREDIT_TUITION = 7230 + ((CREDITS-18)*482) 
                    TUITION = 29
                    print("Tuition is $" + str("{:,.2f}".format(CREDIT_TUITION + TUITION + EXTRA) + ".")) 
                if LEVEL == 'sophomore':
                    CREDIT_TUITION = 7410 + ((CREDITS-18)*494) 
                    TUITION = 29
                    print("Tuition is $" + str("{:,.2f}".format(CREDIT_TUITION + TUITION + EXTRA) + ".")) 
                
            if CREDITS > 18:
                if LEVEL == 'junior' or LEVEL == 'senior':
                    CREDIT_TUITION = 8325 + ((CREDITS-18)*555)
                    TUITION = 29
                    print("Tuition is $" + str("{:,.2f}".format(CREDIT_TUITION + TUITION + EXTRA) + "."))  

        IN = input("Do you want to do another calculation (yes/no): ").lower() # reprompt user so they can calculate tuition again 
        if IN == 'no':
            break

    # same method as above for international students, but different charges for tuition 
    elif RESIDENT == 'no':
        INTERNATIONAL = input("International (yes/no): ")
        INTERNATIONAL = str(INTERNATIONAL)
        if INTERNATIONAL == 'yes':
            INT_EXTRA = 750
            LEVEL = input("Level—freshman, sophomore, junior, senior: ").lower()
            LEVEL = str(LEVEL)
            if LEVEL == 'freshman' or LEVEL == 'sophomore':
                COLLEGE = 'none'
                ENG = input("Are you admitted to the College of Engineering (yes/no): ").lower()
                ENG = str(ENG)
                if ENG == 'yes':
                    EXTRA = 670
                else:
                    EXTRA = 0 
            if LEVEL == 'freshman':
                JMC = input("Are you in the James Madison College (yes/no): ").lower()
                JMC = str(JMC)
                if JMC == 'yes':
                    EXTRA = 7.50 
                else:
                    EXTRA = 0
            if LEVEL == 'junior' or LEVEL == 'senior':
                COLLEGE = input("Enter college as business, engineering, health, sciences, or none: ").lower()
                COLLEGE = str(COLLEGE)
                if COLLEGE == 'business':
                    EXTRA = 226
                if COLLEGE == 'engineering':
                    EXTRA = 670
                if COLLEGE == 'health':
                    EXTRA = 100
                if COLLEGE == 'sciences':
                    EXTRA = 100
                if COLLEGE == 'none':
                    EXTRA = 0
                CME = input("Is your major CMSE (“Computational Mathematics and Engineering”) (yes/no): ").lower()
                CME = str(CME)
                if CME == 'yes':
                    EXTRA = 670  
        CREDITS = input("Credits: ")
        CREDITS = int(CREDITS)
        
        if CREDITS >= 1 and CREDITS <= 11:
            if LEVEL == 'freshman' or LEVEL == 'sophomore':
                CREDIT_TUITION = (CREDITS * 1325.50)
                TUITION = 24 
                print("Tuition is $" + str("{:,.2f}".format(CREDIT_TUITION + TUITION + EXTRA + INT_EXTRA) + "."))              
            
        if CREDITS >= 1 and CREDITS <= 11:
            if LEVEL == 'junior' or LEVEL == 'senior':
                CREDIT_TUITION = (CREDITS * 1366.75)
                TUITION = 24
                print("Tuition is $" + str("{:,.2f}".format(CREDIT_TUITION + TUITION + EXTRA + INT_EXTRA) + "."))   
                
        if CREDITS >= 12 and CREDITS <= 18:
            if LEVEL == 'freshman' or LEVEL == 'sophomore':
                CREDIT_TUITION = 19883
                TUITION = 29 
                print("Tuition is $" + str("{:,.2f}".format(CREDIT_TUITION + TUITION + EXTRA + INT_EXTRA) + "."))               
        
        if CREDITS >= 12 and CREDITS <= 18:
            if LEVEL == 'junior' or LEVEL == 'senior':
                if COLLEGE == 'business' or COLLEGE == 'engineering':
                    CREDIT_TUITION = 20501
                    TUITION = 29
                    print("Tuition is $" + str("{:,.2f}".format(CREDIT_TUITION + TUITION + EXTRA + INT_EXTRA) + "."))   
            
        if CREDITS > 18:
            if LEVEL == 'freshman' or LEVEL == 'sophomore':
                CREDIT_TUITION = 19883 + ((CREDITS-18)*1325.50) 
                TUITION = 29
                print("Tuition is $" + str("{:,.2f}".format(CREDIT_TUITION + TUITION + EXTRA + INT_EXTRA) + "."))   
        
        if CREDITS > 18:
            if LEVEL == 'junior' or LEVEL == 'senior':
                CREDIT_TUITION = 20501 + ((CREDITS-18)*1366.75)
                TUITION = 29
                print("Tuition is $" + str("{:,.2f}".format(CREDIT_TUITION + TUITION + EXTRA + INT_EXTRA) + "."))   
                        
        IN = input("Do you want to do another calculation (yes/no): ").lower()
        if IN == 'no':
            break        






















