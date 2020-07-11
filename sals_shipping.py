# # create ground shipping function
# # create drone shipping function
# # create premium shipping
# #objective: find out weight and offer cheapest option within shipping classes
#
# BELOW THE INITIAL CODE THAT RETURN IN ERROR ----------------------------------------

# def ground_shipping(weight):
#   if weight <= 2:
#     cost = weight * 1.50 + 20
#   elif (weight > 2) and (weight <= 6):
#     cost = weight * 3.00 + 20
#   elif (weight > 6) and (weight <= 10):
#     cost = weight * 4.00 + 20
#   elif weight > 10:
#     cost = weight * 4.75 + 20
#   else:
#     print("wrong weight")
#   return "$" + str(cost) + " with ground shipping"
#   print("Ground Shipping is the cheapest")
#
#
# def drone_shipping(weight):
#   if weight <= 2:
#     cost = weight * 4.50
#   elif (weight > 2) and (weight <= 6):
#     cost = weight * 9.00
#   elif (weight > 6) and (weight <= 10):
#     cost = weight * 12.00
#   elif weight > 10:
#     cost = weight * 14.25
#   else:
#     print("wrong weight")
#   return "$" + str(cost)
#   print("Drone Shipping is the cheapest")
#
# print(ground_shipping(-40))
# print(drone_shipping(7))

# create ground shipping function
# create drone shipping function
# create premium shipping
#objective: find out weight and offer cheapest option within shipping classes


def ground_shipping(weight):
  if weight <= 2:
    cost = 1.50
  elif (weight > 2) and (weight <= 6):
    cost = 3.00
  elif (weight > 6) and (weight <= 10):
    cost = 4.00
  elif weight > 10:
    cost = 4.75
  return (weight * cost) + 20


def drone_shipping(weight):
  if weight <= 2:
    cost = 4.50
  elif (weight > 2) and (weight <= 6):
    cost = 9.00
  elif (weight > 6) and (weight <= 10):
    cost = 12.00
  elif weight > 10:
    cost = 14.25
  return cost * weight

def all_shipping(weight):
  drone = drone_shipping(weight)
  ground = ground_shipping(weight)
  premium = 125.00
  if ground < drone and ground < premium:
    print("Ground is the cheapest and it will cost you " + str(ground))
  elif drone < premium and drone < ground:
    print("drone is the cheapest and it will cost you " + str(drone))
  elif premium < ground and premium < drone:
    print("Premium is the cheapest and it will cost you " + str(premium))

print(all_shipping(80))


