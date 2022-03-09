import random

WHY_WEAR_MASKS = 'Face coverings limit the volume and travel distance of expiratory droplets dispersed when talking, breathing, and coughing. A face covering without vents or holes will also filter out particles containing the virus from inhaled and exhaled air, reducing the chances of infection.'
WHAT_KIND_OF_MASKS = 'N95 respirators offer a higher level of filtration than cloth, surgical or procedural masks. However, they are not necessary to protect people from the virus under normal circumstances. In order to be optimally effective, respirators must be fit-tested and worn properly, tightly fitted against the person\'s face.' 
WHAT_IS_COVID = 'Coronavirus disease 2019 is a contagious disease caused by severe acute respiratory syndrome coronavirus 2. The first known case was identified in Wuhan, China, in December 2019. The disease has since spread worldwide, leading to an ongoing pandemic.'
HOW_DOES_IT_SPREAD = 'COVID-19 transmits when people breathe in air contaminated by droplets and small airborne particles containing the virus. The risk of breathing these in is highest when people are in close proximity, but they can be inhaled over longer distances, particularly indoors. Transmission can also occur if splashed or sprayed with contaminated fluids in the eyes, nose or mouth, and, rarely, via contaminated surfaces.'
HOW_CAN_PROTECT_MYSELF = 'Preventive measures include physical or social distancing, quarantining, ventilation of indoor spaces, covering coughs and sneezes, hand washing, and keeping unwashed hands away from the face. The use of face masks or coverings has been recommended in public settings to minimise the risk of transmissions.'
IF_I_GET_SICK = 'Most people with COVID-19 have mild illness and can recover at home without medical care. Do not leave your home, except to get medical care. Do not visit public areas and do not go to places where you are unable to wear a mask. Take care of yourself.'
IF_SOMEONE_GET_SICK = 'The CDC also states that people who have been around someone with confirmed or suspected COVID-19 should stay home for 10 to 14 days after that exposure unless they are fully vaccinated or had COVID themselves in the last 90 days.'
WHAT_ARE_THE_SYMPTOMS = 'Three common clusters of symptoms have been identified: one respiratory symptom cluster with cough, sputum, shortness of breath, and fever; a musculoskeletal symptom cluster with muscle and joint pain, headache, and fatigue; a cluster of digestive symptoms with abdominal pain, vomiting, and diarrhea.'
EMERGENCY_CARE = 'Stay home. Most people with COVID-19 have mild illness and can recover at home without medical care. Do not leave your home, except to get medical care.'


def unknown():
    response = ["Could you please re-phrase that? ",
                "Please keep your questions within the COVID Pandemic domain, l am still learning ",
                "l did not understand that?",
            ][
        random.randrange(3)]
    return response
