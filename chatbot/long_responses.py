import random

WHY_WEAR_MASKS = 'Your claim information is as follows.. claim: '
WHAT_KIND_OF_MASKS = 'you have paid for the '' policy and it is the insurance premium' 
WHAT_IS_COVID = 'to add your house to your policy, please follow the instructions below'
HOW_DOES_IT_SPREAD = 'to remove your house to your policy, please follow the instructions below'
HOW_CAN_PROTECT_MYSELF = 'to add a dependant to your policy, please follow the instructions below'
IF_I_GET_SICK = 'to remove a dependant to your policy, please follow the instructions below'
IF_SOMEONE_GET_SICK = 'to remove a vehicle to your policy, please follow the instructions below'
WHAT_ARE_THE_SYMPTOMS = 'You have  rtgs due off your policy'
EMERGENCY_CARE = 'To check your payment schedule, you login first, here'


def unknown():
    response = ["Could you please re-phrase that? ",
                "Please keep your questions within the insurance domain, l am still learning ",
                "l did not understand that?",
            ][
        random.randrange(3)]
    return response
