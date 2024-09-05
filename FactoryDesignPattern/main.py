from factory import PersonFactory

# The Client
athlete = PersonFactory.create_person("athlete")
doctor = PersonFactory.create_person("doctor")
teacher = PersonFactory.create_person("teacher")
unknown = PersonFactory.create_person("unknown")
print(athlete.get_info())
print(doctor.get_info())
print(teacher.get_info())
