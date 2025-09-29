from os import system, name
from turtle import back
# ======================================== #
#               Admin Module               #
# ======================================== #
# Functionalitiy included:
# 1. Login to access system
# 2. Add food item category-wise
# 3. Modify food item
# 4. Display all records of Food category, Food items category wise, customer orders, customer payment
# 5. Search specific records of customer order and payment
# 6. Order delivery management


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

# ===== Admin Account Management =====


def adminMenu(adminList, foodList, customerOrderList, customerFoodList, customerPayment, deliveryStaffList, orderAssign, customerList, feedbackList):
    # show admin menu
    choice = 1
    back = adminLogin()
    if(back):
        return
    while(choice != '17'):

        print()
        print("=====================================")
        print("|  APU ONLINE FOOD SERVICES (AOFS)  |")
        print("=====================================")
        print()
        print("1. Add food")
        print("2. Modify Food")
        print("3. Delete Food")
        print("4. Display Food")
        print("5. Display Food Category")
        print("6. Display Customer Order")
        print("7. Search Customer Order")
        print("8. Display Customer Payment")
        print("9. Search Customer Payment")
        print("10. Add Admin")
        print("11. Add delivery staff")
        print("12. Modify delivery staff")
        print("13. Delete delivery staff")
        print("14. Search delivery staff")
        print("15. Assign order to delivery staff")
        print("16. View Feedback")
        print("17. Exit")
        choice = input("What you want to do? > ")
        # Go to target action based on choice
        if(choice == '1'):
            clear()
            addFood(foodList)
        elif (choice == '2'):
            clear()
            modifyFood(foodList)
        elif(choice == '3'):
            clear()
            deleteFood(foodList)
        elif(choice == '4'):
            clear()
            showFoodItem(foodList)
            input("Press any key to continue...")
        elif(choice == '5'):
            clear()
            showFoodCategory()
            input("Press any key to continue...")
        elif(choice == '6'):
            clear()
            showCustomerOrderList(
                customerOrderList, customerFoodList, customerPayment, foodList)
            input("Press any key to continue...")
        elif(choice == '7'):
            clear()
            searchCustomerOrder(customerOrderList, customerFoodList,
                                customerPayment, foodList, customerList)
            input("Press any key to continue...")
        elif(choice == '8'):
            clear()
            showCustomerPaymentList(customerList, customerPayment)
            input("Press any key to continue...")
        elif(choice == '9'):
            clear()
            searchCustomerPayment(customerList, customerPayment)
            input("Press any key to continue...")
        elif(choice == '10'):
            clear()
            addAdmin(adminList)
        elif(choice == '11'):
            clear()
            addDeliveryStaff(deliveryStaffList)
        elif(choice == '12'):
            clear()
            modifyDeliveryStaff(deliveryStaffList)
        elif(choice == '13'):
            clear()
            deleteDeliveryStaff(deliveryStaffList)
        elif(choice == '14'):
            clear()
            searchDeliveryStaff(deliveryStaffList)
            input("Press any key to continue...")
        elif(choice == '15'):
            clear()
            assignDeliveryToOrder(customerOrderList, customerFoodList,
                                  customerPayment, foodList, orderAssign, deliveryStaffList)
        elif(choice == '16'):
            clear()
            viewFeedback(feedbackList)
            input("Press any key to continue...")
        elif(choice == '17'):
            break
        else:
            # Choice outside the range
            print("Error: Please input a valid choice from 1 to 17")
            print()


def adminLogin():
    admin = input("Username: ")
    passw = input("Password: ")
    f = open("admin.txt", "r")
    for line in f.readlines():
        ad, pw = line.strip().split("|")
        if (admin in ad) and (passw in pw):
            print("Login successful!")
            return
        else:
            print("Wrong username/password")
            return "-1"


def readAdminList(adminList):
    # read the admin list from the text file
    # Records: ID, Username, Password
    with open('admin.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            records = line.split('|')
            adminList.append(records)


def writeAdminList(adminList):
    # write the admin list to the text file
    # Records: ID, Username, Password
    with open('admin.txt', 'w') as f:
        for row in adminList:
            for col in row:
                if(col == '\n' or col == ''):
                    break
                f.write(str(col))
                f.write('|')
            f.write('\n')


def addAdmin(adminList):
    adminList = []
    while True:
        adminID = input("Please enter admin ID: ")
        adminUsername = input("Please enter the staff username: ")
        adminPassword = input("Please enter the staff password: ")
        mylist = [adminID, adminUsername, adminPassword]
        adminList.append(mylist)
        break
    # open txt file to append admin_list
    with open("admin.txt", "a") as fh:
        for mylist in adminList:
            rec = "|".join(mylist)+"\n"
            fh.write(rec)
    print()
    print("Admin added.")


# ===== Food Management =====

def readFood(foodList):
    # read the food list from the text file
    # Records: ID, Name, Category ID, Price
    with open('food.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            records = line.split('|')
            foodList.append(records)


def writeFood(foodList):
    # write the updated food list to the text file
    # Records: ID, Name, Category ID, Price
    with open('food.txt', 'w') as f:
        for row in foodList:
            for col in row:
                if(col == '\n' or col == ''):
                    break
                f.write(str(col))
                f.write('|')
            f.write('\n')


def addFood(foodList):
    foodList = []
    while True:
        foodID = input("Please enter a number: ")
        foodName = input("Please enter the food name: ")
        foodCategory = input("Please enter the food category: ")
        foodPrice = input("Please enter the price: ")
        mycuisine = [foodID, foodName, foodCategory, foodPrice]
        foodList.append(mycuisine)
        break

    with open("food.txt", "a") as fh:
        for mycuisine in foodList:
            rec = "|".join(mycuisine)+"\n"
            fh.write(rec)

    print()
    print("Food added.")


def modifyFood(foodList):
    showFoodItem(foodList)
    foodList = []
    with open("food.txt", "r") as fh:
        for rec in fh:
            foodList.append(rec.strip().split("|"))
    # Food ID
    id = input("Enter the foodID to edit: ")
    ind = -1
    for cnt in range(len(foodList)):
        if (id in foodList[cnt][0]):
            ind = cnt
            break
    if (ind != -1):
        foodList[ind][0] = input("Please enter new food id: ")
        foodList[ind][0] = input("Please enter new food name: ")
        foodList[ind][0] = input("Please enter new food category: ")
        foodList[ind][0] = input("Please enter new food price: ")
    else:
        print("Food not Exist.")
    with open("food.txt", "w") as fh:
        for mycuisine in foodList:
            rec = "|".join(mycuisine)+"\n"
            fh.write(rec)
    print()
    print("Food Modified.")


def deleteFood(foodList):
    showFoodItem(foodList)
    foodList = []
    with open("food.txt", "r") as fh:
        for rec in fh:
            foodList.append(rec.strip().split("|"))
    # foodID
    id = input("PLease enter the food ID to delete: ")
    ind = -1
    for cnt in range(len(foodList)):
        if (id in foodList[cnt][0]):
            ind = cnt
            break
    # foodID exist then delete
    if (ind != -1):
        foodList.pop(ind)
        print()
        print("Food removed.")
    else:
        print("Food not Exist.")
    with open("food.txt", "w") as fh:
        for mycuisine in foodList:
            rec = "|".join(mycuisine)+"\n"
            fh.write(rec)


def showFoodCategory():
    # show the category of the food list
    print()
    print("Food Category: ")
    print("1. Chinese Cuisine")
    print("2. Malay Cuisine")
    print("3. Drinks")
    print()


def showFoodItem(foodList):
    with open("food.txt", "r") as foodList:
        print("|"+"Food ID".center(20)+"|"+"Food Name".center(20) +
              "|"+"Food Category".center(20)+"|"+"Price".center(20)+"|")
        for rec in foodList:
            listrec = rec.strip().split("|")
            print("|"+listrec[0].center(20)+"|"+listrec[1].center(20) +
                  "|"+listrec[2].center(20)+"|"+listrec[3].center(20)+"|")

# ===== Customer Order Management =====


def readCustomerOrder(customerOrderList):
    # read the customer order information from the text file
    # Records: ID, Payment ID, Status
    with open('customerOrder.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            records = line.split('|')
            customerOrderList.append(records)


def writeCustomerOrder(customerOrderList):
    # write the updated customer order information to the text file
    # Records: ID, Payment ID, Status
    with open('customerOrder.txt', 'w') as f:
        for row in customerOrderList:
            for col in row:
                if(col == '\n' or col == ''):
                    break
                f.write(str(col))
                f.write('|')
            f.write('\n')


def readCustomerFoodList(customerFoodList):
    # read the customer food list information from the text file
    # Records: ID, Food ID, Quantity, Order ID
    with open('customerFood.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            records = line.split('|')
            customerFoodList.append(records)


def writeCustomerFoodList(customerFoodList):
    # write the updated customer food list information to the text file
    # Records: ID, Food ID, Quantity, Order ID
    with open('customerFood.txt', 'w') as f:
        for row in customerFoodList:
            for col in row:
                if(col == '\n' or col == ''):
                    break
                f.write(str(col))
                f.write('|')
            f.write('\n')


def showCustomerOrderList(customerOrderList, customerFoodList, customerPayment, foodList):
    # show the customer order list
    print("Order list:")
    for order in reversed(customerOrderList):
        status = ""
        if(order[2] == '1'):
            status = "Paid"
        else:
            status = "Delivered"
        print("- Order #" + order[0] + " ( " + status + " )")

    check = True
    id = ""
    while check:
        check = True
        # Read and validate order choice
        id = input("Which order you want to view the details? (-1 to back) ")
        if(id == "-1"):
            break
        for order in customerOrderList:
            if(order[0] == id):
                clear()
                # Show order details
                showCustomerOrderDetail(
                    customerOrderList, customerFoodList, customerPayment, foodList, id)
                check = False
        if(check == True):
            print("Order not found!")
    return id


def showCustomerOrderDetail(customerOrderList, customerFoodList, customerPayment, foodList, id):
    # show a customer order detail
    print("Order Details")
    print("-------------")
    for order in customerOrderList:
        if(order[0] == id):
            # Print order details
            print("Order ID: #" + id)
        for payment in customerPayment:
            if(order[1] == payment[0]):
                amountFormat = "{:.2f}".format(float(payment[2]))
                print("Total Amount: RM" + str(amountFormat))
                print("Card No.: " + payment[2][0:4] + "x")
            status = ""
            if(order[2] == '1'):
                status = "Paid"
            else:
                status = "Delivered"
            print("Status: " + status)
            print()
            print("Ordered Food: ")
            # Print order items
            count = 0
            for food in customerFoodList:
                if(food[1] == id):
                    count += 1
                    for fd in foodList:
                        if(fd[0] == food[1]):
                            print(str(count) + ". " + fd[1] + " x " + food[2])
            print()


def createCustomerOrder(adminList, foodList, customerOrderList, customerFoodList, customerPayment, deliveryStaffList, orderAssign, customerList, feedbackList, currentCustomer):
    # Create a new customer order
    showFoodItem(foodList)
    check = True
    orderList = []
    while check:
        matched = False
        # Read and validate food choice
        id = input("Which food you want to order? ( -1 to stop ) > ")
        if(id == '-1'):
            break
        for food in foodList:
            if(food[0] == id):
                records = []
                records.append(food)
                check2 = True
                quantity = -1
                while check2:
                    check2 = False
                    # Read and validate food quantity
                    quantity = input("Quantity > ")
                    if(quantity.isnumeric() == False):
                        print("Error: You must specify a valid number")
                        check2 = True
                        continue
                    elif(int(quantity) < 1):
                        print("Error: You must buy at least one food")
                        check2 = True
                        continue
                    records.append(quantity)

                matched = True
                # Store the items into the temporary order list
                orderList.append(records)
        if(matched == False):
            print("Error: Target food not found!")

    total = 0.0
    # Compute total cost
    for record in orderList:
        total += float(record[0][3]) * int(record[1])

    # Process for payment
    formatTotal = "{:.2f}".format(float(total))
    print("Total Amount: RM" + str(formatTotal))
    print("Payment: ")
    check = True
    card = ""
    expiryMonth = ""
    expiryYear = ""
    cvv = ""
    while check:
        check = False
        # Obtain card information
        card = input("Card No >  ")
        if(card.isnumeric() == False):
            print("Error: Invalid card number!")
            check = True
            continue
        elif(len(card) != 16):
            print("Error: Invalid card number!")
            check = True
            continue

        # Obtain card expiry information
        expiryMonth = input("Expiry Month > ")
        if(expiryMonth.isnumeric() == False):
            print("Error: Invalid expiry month!")
            check = True
            continue
        elif(int(expiryMonth) < 1 or int(expiryMonth) > 12):
            print("Error: Invalid expiry month!")
            check = True
            continue
        expiryYear = input("Expiry Year > ")
        if(expiryYear.isnumeric() == False):
            print("Error: Invalid expiry year!")
            check = True
            continue
        elif(int(expiryYear) < 2022 or int(expiryYear) > 2100):
            print("Error: Invalid expiry year!")
            check = True
            continue

        # Obtain card cvv
        cvv = input("CVV > ")
        if(cvv.isnumeric() == False):
            print("Error: Invalid cvv!")
            check = True
            continue
        elif(len(cvv) != 3):
            print("Error: Invalid cvv!")
            check = True
            continue

    # Save the order information to the list
    cPayment = [str(len(customerPayment) + 1),
                str(total), card, cvv, expiryMonth + "/" + expiryYear]
    cOrder = [str(len(customerOrderList) + 1),
              str(len(customerPayment) + 1), 1]
    for record in orderList:
        cItem = [str(len(customerFoodList) + 1), record[0][0],
                 record[1], str(len(customerOrderList) + 1)]
        customerFoodList.append(cItem)

    customerPayment.append(cPayment)
    customerOrderList.append(cOrder)

    print("Order created successfully!")
    input("Press any key to continue...")


def searchCustomerOrder(customerOrderList, customerFoodList, customerPayment, foodList, customerList):
    # Search for a customer order
    check = True
    cid = ""
    while check:
        check = True
        # Read the target username
        username = input("Enter target username (-1 to exit) > ")
        if(username == "-1"):
            return
        for customer in customerList:
            if(username == customer[2]):
                cid = customer[0]
                check = False

    # Load customer payments
    paymentIds = []
    for payment in customerPayment:
        if(payment[1] == cid):
            paymentIds.append(payment[0])

    # Print order list
    print("Order list:")
    for order in reversed(customerOrderList):
        if(order[1] in paymentIds):
            status = ""
            if(order[2] == '1'):
                status = "Paid"
            else:
                status = "Delivered"
            print("- Order #" + order[0] + " ( " + status + " )")

    check = True
    id = ""
    while check:
        check = True
        # Read and validate order choice
        id = input("Which order you want to view the details? (-1 to back) ")
        if(id == "-1"):
            break
        for order in customerOrderList:
            if(order[0] == id):
                clear()
                # Show the customer details
                showCustomerOrderDetail(
                    customerOrderList, customerFoodList, customerPayment, foodList, id)
                check = False
        if(check == True):
            print("Order not found!")


def showCustomerPaymentList(customerList, customerPayment):
    # show the customer payment list
    print("Payment received:")
    print("=================")
    for payment in customerPayment:
        print("Payment ID: #" + payment[0])
        # Load customer name from customer list
        for customer in customerList:
            if(customer[0] == payment[1]):
                print("Customer Name: " + customer[1])
        amountFormat = "{:.2f}".format(float(payment[2]))
        print("Payment Amount: RM" + str(amountFormat))
        print("Card: " + payment[3][0:4])
        print()


def searchCustomerPayment(customerList, customerPayment):
    # Search for a customer payment
    check = True
    cid = ""
    name = ""
    while check:
        check = True
        # Read and validate target username
        username = input("Enter target username (-1 to exit) > ")
        if(username == "-1"):
            return
        for customer in customerList:
            if(username == customer[2]):
                cid = customer[0]
                name = customer[1]
                check = False

    # Print payment details
    print("Payment received:")
    print("=================")
    for payment in customerPayment:
        if(payment[1] == cid):
            print("Payment ID: #" + payment[0])
            print("Customer Name: " + name)
            amountFormat = "{:.2f}".format(float(payment[2]))
            print("Payment Amount: RM" + str(amountFormat))
            print("Card: " + payment[3][0:4])
            print()


def readPayment(customerPayment):
    # Read customer payment from the text file
    # Records: ID, Customer ID, Amount, Card No, CVV, Expiry Date
    with open('customerPayment.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            records = line.split('|')
            customerPayment.append(records)


def writePayment(customerPayment):
    # Write customer payment to the text file
    # Records: ID, Customer ID, Amount, Card No, CVV, Expiry Date
    with open('customerPayment.txt', 'w') as f:
        for row in customerPayment:
            for col in row:
                if(col == '\n' or col == ''):
                    break
                f.write(str(col))
                f.write('|')
            f.write('\n')


def viewFeedback(feedbackList):
    # Check the feedback that provided by the customer
    count = 0
    print("Feedback: ")
    print("==========")
    for feedback in feedbackList:
        count += 1
        print(str(count) + ". " + feedback[0])


# ===== Order Delivery Management =====

def readDeliveryStaffList(deliveryStaffList):
    # Read the list of delivery staff from the text file
    # Records: ID, Name, Username, Password
    with open('deliveryStaffList.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            records = line.split('|')
            deliveryStaffList.append(records)


def addDeliveryStaff(deliveryStaffList):
    deliveryStaffList = []
    while True:
        staffID = input("Please enter the delivery staff id: ")
        staffUsername = input("Please enter the delivery staff ussername: ")
        staffPassword = input("Please enter the delivery stuff password: ")
        mystaff = [staffID, staffUsername, staffPassword]
        deliveryStaffList.append(mystaff)
        break
    # open txt file to append delivery_stuff_list
    with open("deliveryStaffList.txt", "a")as fh:
        for mystaff in deliveryStaffList:
            rec = "|".join(mystaff)+"\n"
            fh.write(rec)
    print()
    print("Delivery staff added.")


def searchDeliveryStaff(deliveryStaffList):
    # Search for a delivery staff
    check = True
    while check:
        check = True
        id = input("Target ID (-1 to exit) > ")
        if(id == '-1'):
            check = False
            break
        # Loop through and look for target staff
        for staff in deliveryStaffList:
            if(staff[0] == id):
                print(staff[0] + ". " + staff[1] +
                      " ( Username: " + staff[2] + " ) ")
                check = False
        if(check):
            check = True
            print("Error: ID not found!")


def showDeliveryStaffList(deliveryStaffList):
    # Show the list of delivery staff
    print("Delivery Staff available: ")
    for staff in deliveryStaffList:
        print(staff[1] + " ( Username: " + staff[2] + " ) ")
        print("ID = " + staff[0])


def modifyDeliveryStaff(deliveryStaffList):
    showDeliveryStaffList(deliveryStaffList)
    deliveryStaffList = []
    with open("deliveryStaffList.txt", "r") as fh:
        for rec in fh:
            deliveryStaffList.append(rec.strip().split("|"))
    # delivery staff id
    id = input("Please enter the delivery staff id to edit: ")
    ind = -1
    for cnt in range(len(deliveryStaffList)):
        if (id in deliveryStaffList[cnt][0]):
            ind = cnt
            break
    if (ind != -1):
        deliveryStaffList[ind][0] = input(
            "Please enter new delivery staff ID: ")
        deliveryStaffList[ind][1] = input(
            "Please enter new delivery staff username: ")
        deliveryStaffList[ind][2] = input(
            "Please enter new delivery staff password: ")
    else:
        print("Staff not exist.")
    with open("deliveryStaffList.txt", "w") as fh:
        for mylist in deliveryStaffList:
            rec = "|".join(mylist)+"\n"
            fh.write(rec)
    print()
    print("Delivery staff modified.")


def deleteDeliveryStaff(deliveryStaffList):
    # delete the delivery staff from the list
    showDeliveryStaffList(deliveryStaffList)
    deliveryStaffList = []
    with open("deliveryStaffList.txt", "r") as fh:
        for rec in fh:
            deliveryStaffList.append(rec.strip().split("|"))
    # Staff ID
    id = input("Please enter the staff id to delete: ")
    ind = -1
    for cnt in range(len(deliveryStaffList)):
        if (id in deliveryStaffList[cnt][0]):
            ind = cnt
            break
    # staff id exist then delete
    if (ind != -1):
        deliveryStaffList.pop(ind)
        print()
        print("Staff deleted.")
    else:
        print("Staff not Exist.")
    with open("deliveryStaffLiat.txt", "w") as fh:
        for mystaff in deliveryStaffList:
            rec = "|".join(mystaff)+"\n"
            fh.write(rec)


def readOrderAssign(orderAssign):
    # read the order assign list from the text file
    # Records: ID, Order ID, Delivery ID
    with open('orderAssign.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            records = line.split('|')
            orderAssign.append(records)


def writeOrderAssign(orderAssign):
    # write the order assign list to the text file
    # Records: ID, Order ID, Delivery ID
    with open('orderAssign.txt', 'w') as f:
        for row in orderAssign:
            for col in row:
                if(col == '\n' or col == ''):
                    break
                f.write(str(col))
                f.write('|')
            f.write('\n')


def assignDeliveryToOrder(customerOrderList, customerFoodList, customerPayment, foodList, orderAssign, deliveryStaffList):
    # Assign delivery staff to the order
    id = showCustomerOrderList(
        customerOrderList, customerFoodList, customerPayment, foodList)
    if(id == ""):
        return
    validOrders = []

    # Check if the target order had been assigned
    for order in customerOrderList:
        match = False
        for assignedOrder in orderAssign:
            if(order[0] == assignedOrder[1]):
                match = True
        if(match):
            continue
        else:
            if(order[2] != "1"):
                continue
            else:
                validOrders.append(order[0])
    # Error message
    if(id not in validOrders):
        print("Error: Invalid order! It can't be assigned to delivery staff")
        input("Press any key to continue...")
        return

    print()

    # Show delivery staff list
    showDeliveryStaffList(deliveryStaffList)
    print()
    check = True
    did = ""
    while check:
        check = True
        # Read and validate target staff
        did = input("Target delivery staff to assign (-1 to exit ) > ")
        if(did == "-1"):
            return
        for deliveryStaff in deliveryStaffList:
            if(did == deliveryStaff[0]):
                check = False
        if check:
            print("Error: Target staff not found!")
            input("Press any key to continue...")
    # Store the updates
    orderAssign.append([str(len(orderAssign) + 1), id, did])
    print("Order is Assigned Successfully!")
    input("Press any key to continue...")


# ======================================== #
#           Delivery Staff Module          #
# ======================================== #
# Functionality included:
# 1. Login to access system
# 2. View and select orders for delivery
# 3. Update Delivery Status

def deliveryMenu(foodList, customerOrderList, customerFoodList, customerPayment, deliveryStaffList, orderAssign, currentStaff):
    # show the menu for the delivery staff
    back = deliveryLogin(deliveryStaffList)
    if(back):
        return

    while True:
        print("=====================================")
        print("|  APU ONLINE FOOD SERVICES (AOFS)  |")
        print("=====================================")
        print("1. View all order")
        print("2. Update Delivery Status")
        print("3. Select order for delivery")
        print("4. Exit")
        choice = input("What you want to do? > ")
        # Run action based on the choice
        if(choice == '1'):
            clear()
            showCustomerOrderList(
                customerOrderList, customerFoodList, customerPayment, foodList)
            input("Press any key to continue...")
        elif (choice == '2'):
            clear()
            updateDeliveryStatus(orderAssign, currentStaff, customerOrderList)
        elif (choice == '3'):
            clear()
            selectOrderDelivery(customerOrderList, customerFoodList, customerPayment,
                                foodList, orderAssign, deliveryStaffList, currentStaff)
            input("Press any key to continue...")
        elif(choice == '4'):
            clear()
            exit
        else:
            # Choice out of range
            print("Error: Please input a valid choice from 1 to 4")
            break


def deliveryLogin(deliveryStaffList):
    deliveryStaffId = input("Please enter your staff id: ")
    deliveryStaffUsername = input("Please enter your username: ")
    deliveryStaffPassword = input("Please enter your password: ")
    deliveryStaffList = open("deliveryStaffList.txt", "r")
    for line in deliveryStaffList.readlines():
        id, us, pw = line.strip().split("|")
        if(deliveryStaffId in id) and (deliveryStaffUsername in us) and (deliveryStaffPassword in pw):
            print("Login Successful!")
            return
        else:
            print("Invalid username or password!")
            return "-1"


def selectOrderDelivery(customerOrderList, customerFoodList, customerPayment, foodList, orderAssign, deliveryStaffList, currentStaff):
    # select the order that the staff want to deliver
    id = showCustomerOrderList(
        customerOrderList, customerFoodList, customerPayment, foodList)
    if(id == ""):
        return
    orderAssign.append([str(len(orderAssign) + 1), id, currentStaff])


def updateDeliveryStatus(orderAssign, currentStaff, customerOrderList):
    # Update the status of the order

    orders = []
    for order in orderAssign:
        if(order[0] == currentStaff):
            orders.append(order[0])

    if(len(orders) == 0):
        print("Error: No order assigned")
        input("Press any key to continue...")
        return

    # Show the assigned order
    for order in customerOrderList:
        if(order[0] in orders):
            status = ""
            if(order[2] == '1'):
                status = "Paid"
            else:
                status = "Delivered"
            print("- Order #" + order[0] + " ( " + status + " )")
    check = True
    id = ""
    while check:
        check = True
        # Read and validate order choice
        id = input("Which order you want to update status? (-1 to exit) > ")
        if(id == "-1"):
            return
        for order in customerOrderList:
            if(order[0] == id):
                clear()
                # Change the order status
                if(order[2] == '1'):
                    order[2] = '2'
                    print("Changed to delivered!")

                else:
                    order[2] = '1'
                    print("Changed to paid!")
                check = False
            if(check == True):
                print("Order not found!")

    input("Press any key to continue...")


# ======================================== #
#              Customer Module             #
# ======================================== #
# Functionality included:
# 1. View all food
# 2. New Customer registration
# 3. Login
# 4. View food category, and food items
# 5. Order food from menu
# 6. Payment
# 7. Feedback

def registeredCustomerMenu(adminList, foodList, customerOrderList, customerFoodList, customerPayment, deliveryStaffList, orderAssign, customerList, feedbackList, currentCustomer):
    # show the menu for the registered customer
    choice = 1
    # Print Menu
    while(choice != '5'):
        print()
        print("=====================================")
        print("|  APU ONLINE FOOD SERVICES (AOFS)  |")
        print("=====================================")
        print()
        print("1. View all food")
        print("2. View food category")
        print("3. Order")
        print("4. Give Feedback")
        print("5. Exit")
        choice = input("What you want to do? > ")
        # Perform actions based on choice
        if(choice == '1'):
            clear()
            showFoodItem(foodList)
            input("Press any key to continue...")
        elif (choice == '2'):
            clear()
            showFoodCategory()
            input("Press any key to continue...")
        elif(choice == '3'):
            clear()
            createCustomerOrder(adminList, foodList, customerOrderList, customerFoodList, customerPayment,
                                deliveryStaffList, orderAssign, customerList, feedbackList, currentCustomer)
        elif(choice == '4'):
            clear()
            giveFeedback(feedbackList)
        elif(choice == '5'):
            break
        else:
            # Choice out of range
            print("Error: Please input a valid choice from 1 to 5")
            print()


def customerMenu(adminList, foodList, customerOrderList, customerFoodList, customerPayment, deliveryStaffList, orderAssign, customerList, feedbackList):
    # show the menu for the customer
    choice = 1
    currentCustomer = []
    while (choice != '4'):
        # Print customer menu
        print()
        print("=====================================")
        print("|  APU ONLINE FOOD SERVICES (AOFS)  |")
        print("=====================================")
        print()
        print("1. View all food")
        print("2. Register new account")
        print("3. Login")
        print("4. Exit")
        choice = input("What you want to do? > ")
        # Perform actions based on choice
        if(choice == '1'):
            clear()
            showFoodItem(foodList)
            input("Press any key to continue...")
        elif (choice == '2'):
            clear()
            customerRegister(customerList)
        elif(choice == '3'):
            clear()
            back = customerLogin(customerList)
            if(back):
                return
            else:
                clear()
                registeredCustomerMenu(adminList, foodList, customerOrderList, customerFoodList, customerPayment,
                                       deliveryStaffList, orderAssign, customerList, feedbackList, currentCustomer)
        elif(choice == '4'):
            break
        else:
            # Choice out of range
            print("Error: Please input a valid choice from 1 to 4")
            print()


def customerLogin(customerList):
    customerUsername = input("Please enter your username: ")
    customerPassword = input("Please enter your password: ")
    customerList = open("customerList.txt", "r")
    for line in customerList.readlines():
        us, pw = line.strip().split("|")
        if(customerUsername in us) and (customerPassword in pw):
            print("Login Successful!")
            return
        else:
            print("Invalid username or password!")
            return "-1"


def customerRegister(customerList):
    customerList = []
    while True:
        customerUsername = input("Please enter your username: ")
        customerPassword = input("Please set your password: ")
        myCustomer = [customerUsername, customerPassword]
        customerList.append(myCustomer)
        break
    # open txt file to append customer_list
    with open("customerList.txt", "a") as fh:
        for myCustomer in customerList:
            rec = "|".join(myCustomer)+"\n"
            fh.write(rec)
    print()
    print("Customer Registered.")


def readCustomerList(customerList):
    # Read the customer details from the text file
    # Records: ID, Name, Username, Password
    with open('customerList.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            records = line.split('|')
            customerList.append(records)


def writeCustomerList(customerList):
    # Save the updated customer details to the text file
    # Records: ID, Name, Username, Password
    with open('customerList.txt', 'w') as f:
        for row in customerList:
            for col in row:
                if(col == '\n' or col == ''):
                    break
                f.write(str(col))
                f.write('|')
            f.write('\n')


def giveFeedback(feedbackList):
    # Allow the customer to provide feedback

    feedback = input("Provide your feedback here: (-1 to skip) > ")
    if(feedback == "-1" or feedback == ""):
        return
    else:
        feedbackList.append([feedback])


def readFeedbackList(feedbackList):
    # Read the feedback records from the text file
    with open('feedbackList.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            records = line.split('|')
            feedbackList.append(records)


def writeFeedbackList(feedbackList):
    feedbackList = []
    while True:
        feedback = input("Please enter your comment: ")
        mylist = [feedback]
        feedbackList.append(mylist)
        break
    # open txt file to append feedback_list
    with open("feedbackList.txt", "a") as fh:
        for mylist in feedbackList:
            rec = "|".join(mylist)+"\n"
            fh.write(rec)
    print()
    print("Thank you for your feedback.")


def readFiles(adminList, foodList, customerOrderList, customerFoodList, customerPayment, deliveryStaffList, orderAssign, customerList, feedbackList):
    readAdminList(adminList)
    readFood(foodList)
    readCustomerOrder(customerOrderList)
    readCustomerFoodList(customerFoodList)
    readPayment(customerPayment)
    readDeliveryStaffList(deliveryStaffList)
    readOrderAssign(orderAssign)
    readCustomerList(customerList)
    readFeedbackList(feedbackList)


def writeFiles(adminList, foodList, customerOrderList, customerFoodList, customerPayment, deliveryStaffList, orderAssign, customerList, feedbackList):
    writeAdminList(adminList)
    writeFood(foodList)
    writeCustomerOrder(customerOrderList)
    writeCustomerFoodList(customerFoodList)
    writePayment(customerPayment)
    writeOrderAssign(orderAssign)
    writeCustomerList(customerList)
    writeFeedbackList(feedbackList)


def mainMenu():
    adminList = []
    foodList = []
    customerOrderList = []
    customerFoodList = []
    customerPayment = []
    deliveryStaffList = []
    orderAssign = []
    customerList = []
    feedbackList = []
    currentStaff = []
    # Show the main menu
    readFiles(adminList, foodList, customerOrderList, customerFoodList,
              customerPayment, deliveryStaffList, orderAssign, customerList, feedbackList)
    choice = 1
    while (choice != '4'):
        print("=====================================")
        print("|  APU ONLINE FOOD SERVICES (AOFS)  |")
        print("=====================================")
        print()
        print("1. Admin")
        print("2. Delivery Staff")
        print("3. Customer")
        print("4. Exit")
        choice = input("Who are you? > ")
        # Perform action based on choice
        if(choice == '1'):
            clear()
            adminMenu(adminList, foodList, customerOrderList, customerFoodList,
                      customerPayment, deliveryStaffList, orderAssign, customerList, feedbackList)
        elif (choice == '2'):
            clear()
            deliveryMenu(customerOrderList, customerFoodList,
                         customerPayment, deliveryStaffList, orderAssign, customerList, currentStaff)
        elif(choice == '3'):
            clear()
            customerMenu(adminList, foodList, customerOrderList, customerFoodList,
                         customerPayment, deliveryStaffList, orderAssign, customerList, feedbackList)
        elif(choice == '4'):
            break
        else:
            # Choice out of range
            print("Error: Please input a valid choice from 1 to 4")
            print()
    writeFiles(adminList, foodList, customerOrderList, customerFoodList,
               customerPayment, deliveryStaffList, orderAssign, customerList, feedbackList)


def isfloat(num):
    # check if num is a float or not
    try:
        float(num)
        return True
    except ValueError:
        return False


mainMenu()
