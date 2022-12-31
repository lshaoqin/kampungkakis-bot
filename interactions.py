#Format is {input : {state, reply}}
#The state will determine action taken on the user's next message

default_interactions = {
    "I am a KampungKakis volunteer!" : {'state': 'default', 'reply': "Hello volunteer! What do you need help with?"},
    "I am a KampungKakis beneficiary or senior!" : {'state': 'name', 'reply': "What is your name?"},
    "I am looking for assistance related to groceries." : {'state': 'regular_kaki', 'reply': "Do you already have a regular kaki volunteer?"},
    "I am looking for a medical escort." : {'state': 'regular_kaki', 'reply': "Do you already have a regular kaki volunteer?"},
    "I am looking for assistance related to befriending." : {'state': 'regular_kaki', 'reply': "Do you already have a regular kaki volunteer?"},
    "I am looking for other help." : {'state': 'assistance', 'reply': "Could you share what other assistance you would require? We will do our best to look into it!"},
    "I would like to find out more about upcoming events?" : {'state': 'default', 'reply': "Please refer to the following link (xx link) for our upcoming activities! Feel free to sign up at the respective sign up links."},
    "I would like to take up an ad-hoc volunteer request!" : {'state': 'response', 'reply': "Please share which ad-hoc request is this. A KampungKakis core team member will reach out to share more details about the request with you shortly."},
    "I would like to ask something related to my kaki!" : {'state': 'response', 'reply': "Please share the name of your kaki and the nature of your enquiry. We will get back to you shortly."},
    "I would like to find out more about the volunteer claims process!" : {'state': 'default', 'reply': "Please make your claims via our volunteer claims form - bit.ly/KK_claims2022 \nWe will verify your claim shortly and reimburse by the end of the month."},
    "I would like to connect with someone from KampungKakis!" : {'state': 'response', 'reply': "Please share your question or request. A KampungKakis core team member will reach out and contact you within the next 48 hours."},
    "I would like to sign up as a volunteer." : {'state': 'default', 'reply': "You may sign up as a volunteer via our sign-up form here: volunteer.kampungkakis.org \nWe look forward to connecting with you!"},
    "I would like to sign up as a beneficiary." : {'state': 'default', 'reply': "Are you currently above the age of 50 years old?"},
    "I am not above 50 years old." : {'state': 'response', 'reply': "KampungKakis serves beneficiaries above the age of 50 years old. If you do not fall under this age range, do let us know what kind of support you might require. A KampungKakis core team member will reach out to you within the next 48 hours."},
    "I am above 50 years old." : {'state': 'default', 'reply': "Are you looking for urgent help (within next 48 hours)?"},
    "I am not looking for urgent help." : {'state': 'default', 'reply': "You may sign up as a senior kaki via our sign-up form here: seniorkaki.kampungkakis.org. We look forward to connecting with you!?"},
    "I am looking for urgent help." : {'state': 'default', 'reply': "KampungKakis is unable to help with urgent needs, but here is a list helplines you can call: (gives list)"},
}