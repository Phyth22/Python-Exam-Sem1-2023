
#

# Get user input for age
#user_age = int(input("Enter your age: "))

# Check eligibility based on age
#if user_age >= 18:
    #print("You are eligible.")
#else:
    #print("You are not eligible.")


#(ii)

def grade_students(mark):
    try:
        mark = float(mark)
    except ValueError:
     print('Invalid input' )

    if mark >= 90:
        grade = 'A'
        message = 'Excellent'
       
        
    elif 80 <= mark < 90:
        grade = 'B'
        message = 'Excellent'
        
        
    elif 70 <= mark < 80:
        grade = 'C'
        message = 'Good'
        
        
    elif 60 <= mark < 70:
        grade = 'D'
        message = 'Satisfactory'
        
        
    else:
        grade = 'F'
        message = 'Needs improvement'
        grade_students(mark)
       # print (grade, message)
       

    

# Testing with a valid mark
valid_mark = 85
valid_result = grade_students(valid_mark)
print(f"Grade: {valid_result[0]}, Message: {valid_result[1]}")

# Testing with an invalid input
invalid_mark = 'abc'
invalid_result = grade_students(invalid_mark)
#print(result_invalid)

 




   
   
  

   
   
         
   
   #GIT COMMANDS FOR PUSHING WRK
   
   # git init
   #git add .
   #git commit -m "helo"
   #git remote add origin "url"
# git remote -v
#git push -u -f origin master
   
   