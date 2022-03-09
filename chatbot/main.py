import re
import long_responses as long


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi','hie','help', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how', 'are','you'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
    response('Im the COVID Chat assistant', ['is','your','name', ], single_response=True)


    # Longer responses
    response(long.WHY_WEAR_MASKS, ['why',' should','people', ' wear', ' mask'], required_words=['wear', 'mask','people'])
    response(long.WHAT_KIND_OF_MASKS, ['what','kind','of ', 'of', 'mask',' should', 'the','public',' wear'], required_words=['mask', 'public','wear'])
    response(long.WHAT_IS_COVID, ['what','is','covid','covid-19','corona','sarscov'], required_words=['what', 'is'])
    response(long.HOW_DOES_IT_SPREAD, ['how','does','the','virus','spread'], required_words=['how','virus','spread'])
    response(long.HOW_CAN_PROTECT_MYSELF, ['how','do','can','I','protect','myself'], required_words=['protect','myself'])
    response(long.IF_I_GET_SICK, ['what','to','do','if','l','get','sick'], required_words=['I','get','sick'])
    response(long.IF_SOMEONE_GET_SICK, ['what','to','do','if','someone','gets','sick'], required_words=['someone','sick'])
    response(long.WHAT_ARE_THE_SYMPTOMS, ['what','are','the','sympthoms'], required_words=['sympthoms'])
    response(long.EMERGENCY_CARE, ['when','seek','emergency','treatment','help',], required_words=['emergency','treatment'])


    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match

# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system
while True:
    print('Bot: ' + get_response(str(input('You: ')).lower()))
