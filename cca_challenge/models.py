from django.db import models

# Section model contains course info, as well as methods which change the registered number if a student adds or drops a class. 
class Section (models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    section_title = models.CharField(max_length = 50)
    section_id = models.CharField(max_length = 50)
    instructor = models.CharField(max_length = 50)
    department = models.CharField(max_length = 50)
    room = models.CharField(max_length = 50)
    capacity = models.PositiveIntegerField()
    registered = models.PositiveIntegerField()


    def register(self):
        self.registered += 1
        return self.registered

    def drop(self):
        self.registered -= 1
        return self.registered

    def to_json(self):
        return dict(
            id = self.id,
            section_title = self.section_title,
            section_id = self.section_id,
            instructor = self.instructor,
            department = self.department,
            room = self.room,
            capacity = self.capacity,         
            registered = self.registered   
        )  