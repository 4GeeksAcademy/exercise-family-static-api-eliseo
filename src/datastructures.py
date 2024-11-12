
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            {
                "id": self._generate_id(),
                "first_name": "John",
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jane",
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jimmy",
                "age": 5,
                "lucky_numbers": [1]
            }
        ]
    
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        new_member= {
            "id": member.get("id", self._generate_id()),
            "first_name": member.get("first_name"),
            "age": member.get("age"),
            "lucky_numbers": member.get("lucky_numbers")
        }
        self._members.append(new_member)
        return new_member
        

    def delete_member(self, id):
        for index in range(0, len(self._members)):
            if self._members[index].get("id") == id:
                return self._members.pop(index)
        return None


    def get_member(self, id):
        return next((member for member in self._members if member['id'] == id), None)

  
    def get_all_members(self):
        return self._members
