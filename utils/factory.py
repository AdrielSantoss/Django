from faker import Faker

fake = Faker()

def generate_new(): 
        return {
            "title": fake.sentence(),
            "text": fake.text()
        }
        