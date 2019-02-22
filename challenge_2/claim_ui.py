import claim_repo   

'''
Komodo Claims Department:
30 after claim is no longer valid.
ClaimType: Car, Home, Theft
Choose a menu option:
1. See All Claims
2. Take care of next claim
3. Enter a new claim
'''
def print_next_claim(claim_list):
    x = claim_list[0]
    print(x)

def handle_claim():
    temp = claim_repo.get_claims()
    print('Next claim: ')
    print_next_claim(temp)
    user_choice = input('Do you want to handle this claim: Y or N').lower()
    if user_choice == "y":
        claim_repo.remove_first_claim()
        print('Claim Handled')
        
def build_new_claim():
    claim_type = input('Enter the type of Claim: \t')
    description = input('Enter the description of claim: \t')
    claim_amount = input('Amount of Claim: \t')
    date_of_incident = input('Date of the Incident: \t')
    date_of_claim = input('Date of the Claim: \t')
    is_valid = input('Is the claim valid: \t')
    claim_repo.create_claim(claim_type, description, claim_amount, date_of_incident, date_of_claim, is_valid)
    
def see_all_claims():
    claim_list = claim_repo.get_claims()
    for i in claim_list:
        print(i)


while True:
    print('Komodo Claims Department')
    choice = input("Choose a menu option: \n" +
                   "1. See All Claims: \n" +
                   "2. Take Care of next claim: \n" +
                   "3. Enter a new claim: \n" +
                   "4. Exit\n")
    if choice == '1':
        see_all_claims()
    elif choice == '2':
        handle_claim()
    elif choice == '3':
        build_new_claim()
    elif choice == '4':
        exit()
    else:
        print('Input is not valid')

