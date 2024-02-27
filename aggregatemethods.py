 ## aggregate method that counts the number of course a Student is a part of. For this methood all we need to do is look at the count  of all the entollments in the student object.

 def course_count(self):
 	return len(self._enrollments)

## aggregate methid that counts the number of courses a Student is a part of. For this method all we  neeed to do is look at the count of all the enrollments in the Student objecy.
def course_count(sekf):
	return len(self,_enrollments)

	##aggregate mthod to  the Enrollment class to figure out how many enrollments were done for any day students were enrolled. Class method.
	@classmethod
	def aggregate_enrollments_per_day(cls):
		enrollllment_count ={}
		for enrollment in cls.all:
			date = enrollment.get_enrollment_date().date()
			enrollment_count[date] = enrollment_count.get(date, 0) + 1
			return enrollment_count

			#in this method we iterate through all the enrollments and create a Dictionary where the key is the date and the value is the count of enrollments on that date. We increment the count every time we see an enrollment on the same date.

			#Now let's assume the Student has a grades attribute. This attribute can be a dictionary where the key is the enrollment and the value is the grade. Let's wwrite a method that would give us the average grade a student across al the courses they are enrolled in.

	 def aggregate_average_grade(self):
				# lets assume the grades are stored in a procted attribute called _grades.
				total_grades = sum(self._grades._grades.values())
				num_courses = len(self._grades)
				average_grade = total_grades / num_courses

			return average_grade


	#In this illustration we don't care about the course and only the grades  lets get the values from the grades dictionary using self._grades.values(). We can now sum the grades and divide it by the number of the courses we have which will end up being the average of the students grades across all the enrollments.

	#Conclusion

