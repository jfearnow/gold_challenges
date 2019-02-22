from claim import Claim

'''
This module will handle the UI
and CRUD Functionality of the Menus object
'''
#CRUD: Create, Read, Update, Delete

claims = []


def create_claim(claimtype, description, claimamount, dateofincident, dateofclaim, isvalid):
    new_claim = Claim(claimtype, description, claimamount, dateofincident, dateofclaim, isvalid)
    claims.append(new_claim)
   
def get_claims():
    return claims

def remove_first_claim():
    claims.pop(0)


    




