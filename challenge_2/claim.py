'''
ClaimId, ClaimType, Description, ClaimAmount, DateOfIncident, DateOfClaim, IsValid

'''

class Claim:

    def __init__(self, claimtype, description, claimamount, dateofincident, dateofclaim, isvalid):
        self.claimtype = claimtype
        self.description = description
        self.claimamount = claimamount
        self.dateofincident = dateofincident
        self.dateofclaim = dateofclaim
        self.isvalid = isvalid 


    def __repr__(self):
        return f"ClaimType: {self.claimtype}, Description: {self.description}, ClaimAmount: {self.claimamount}, DateOfIncident: {self.dateofincident}, DateOfClaim: {self.dateofclaim}, IsValid: {self.isvalid}"