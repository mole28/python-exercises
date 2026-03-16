import httpx
from pydantic import BaseModel

client = httpx.Client(base_url="https://jsonplaceholder.typicode.com/users/")

class User(BaseModel):
    id: int
    name: str
    username: str

    @classmethod
    def get_user(cls):

        list_of_user=[]

        for i in range(1, 11):
            response = client.get(str(i))
            user_of_dict = response.json()
            user_obj = cls.model_validate(user_of_dict)
            list_of_user.append(user_obj)
        return list_of_user

    
    def save(self):

        filename = "user_" + str(self.id) + ".json"
        with open(filename, "w") as the_open_file:
            the_open_file.write(self.model_dump_json(indent=2))

        print("Saved user " + str(self.id) + " to file: " + filename)


    @classmethod
    def load(cls, user_id):
        filename = "user_" + str(user_id) + ".json"
        with open(filename, "r") as the_open_file:
            user_of_json = the_open_file.read()
            return cls.model_validate_json(user_of_json)
