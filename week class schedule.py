
calc_location = "Bldg: 117"
wght_location = "Bldg: 225"
labs_location = "Bldg: 24A"
biolgy_location = "Bldg: 24B"
soci_location = "Bldg: 334"
psych_location = "Bldg: 335"
tutor_location = "Bldg: 100"



def monday_f(monday_class, monday_times, class_location):
      monday_schedule = []
      
      index = 0      
      while index < len(monday_class):
      
        scheduled_class = monday_class[index] + ": " + monday_times[index] + ", " + class_location[index]
        
        monday_schedule.append(scheduled_class)
        
        index += 1
    
      return monday_schedule

monday_class = ["Calculus 1", "Weight Lifting", "Labs", "Biology"]
monday_times = ["0800", "0900", "1300", "1400"]
m_class_loc = [calc_location, wght_location, labs_location, biolgy_location]

monday_schedule = monday_f(monday_class, monday_times, m_class_loc)
 
def tuesday_f(tuesday_class, tuesday_times, class_location):
      tuesday_schedule = []
      
      index = 0
      while index < len(tuesday_class):
      
      
        scheduled_class = tuesday_class[index] + ": " + tuesday_times[index] + ", " + class_location[index]
        tuesday_schedule.append(scheduled_class)
        
        index += 1
    
      return tuesday_schedule
    
    
tuesday_class = ["Sociology 101", "psycology 1", "Calculus 1"]
tuesday_times = ["0830", "1000", "1300"]
t_class_location = [soci_location, psych_location, calc_location]

tuesday_schedule = tuesday_f(tuesday_class, tuesday_times, t_class_location)

def wednesday_f(wednesday_class, wednesday_times, class_location):
      wednesday_schedule = []
      
      index = 0
      while index < len(wednesday_class):
          
        scheduled_class = wednesday_class[index] + ": " + wednesday_times[index] + ", " + class_location[index]
        wednesday_schedule.append(scheduled_class)
        
        index += 1
    
      return wednesday_schedule
    
wednesday_class = ["Tutoring", "Calculus 1", "Biology"]
wednesday_times = ["1000", "1300", "1400"]
w_class_location = [tutor_location, calc_location, biolgy_location]

wednesday_schedule = wednesday_f(wednesday_class, wednesday_times, w_class_location)

def thursday_f(thursday_class, thursday_times, class_location):
      thursday_schedule = []
      
      index = 0
      while index < len(thursday_class):
        
        scheduled_class = thursday_class[index] + ": " + thursday_times[index] + ", " + class_location[index]
        thursday_schedule.append(scheduled_class)
        
        index += 1
    
      return thursday_schedule
   
thursday_class = ["Sociology 101", "Weight Lifting", "Calculus 1"]
thursday_times = ["0830", "1000", "1300"]
th_class_location = [soci_location, wght_location, calc_location]
thursday_schedule = thursday_f(thursday_class, thursday_times, th_class_location)
  
def friday_f(friday_class, friday_times, class_location):
      friday_schedule = []
      
      index = 0
      while index < len(friday_class):
      
        scheduled_class = friday_class[index] +": " + friday_times[index] + ", " + class_location[index]
        friday_schedule.append(scheduled_class)
        
        index += 1
    
      return friday_schedule
    
    
friday_class = ["Labs", "Biology", "Calculus 1"]
friday_times = ["0800", "0900", "1300"]
f_class_location = [labs_location, biolgy_location, calc_location]

friday_schedule = friday_f(friday_class, friday_times, f_class_location)

#This is a tuple, you can store any data in a tuple, each ( ) is an index, can be used as a list with [ ]. 
full_schedule = [("Monday:", monday_schedule), ("Tuesday:", tuesday_schedule), ("Wednesday:", wednesday_schedule), ("Thursday:", thursday_schedule), ("Friday:", friday_schedule)]

#I used False in a while loop to ensure that the input is displayed after an output. 
loop = False

while loop == False:
  
  user_input = input("What class schedule do you want to view? ->")    
  print("-----‐-------------------------------------------------------------------------------------------------------")

  if user_input == "monday" or user_input == "Monday":
       print("Your schedule for MONDAY is: ")
       print("__________________________________________________________________ ")
       for i in monday_schedule:       
         print(i)
         print("__________________________________________________________________ ")
         
  elif user_input == "tuesday" or user_input == "Tuesday":
      print("Your schedule for TUESDAY is: ")
      print("__________________________________________________________________ ")
      for i in tuesday_schedule:
        print (i)
        print("__________________________________________________________________ ")
      
  elif user_input == "wednesday" or user_input == "Wednesday":
      print("Your schedule for WEDNESDAY is: ")
      print("__________________________________________________________________ ")
      for i in wednesday_schedule:
        print(i)
        print("__________________________________________________________________ ")
      
  elif user_input == "thursday" or user_input == "Thursday":
      print("Your schedule for THURSDAY is: ")
      print("__________________________________________________________________ ")
      for i in thursday_schedule:
        print(i)
        print("__________________________________________________________________ ")
      
  elif user_input == "friday" or user_input =="Friday":
      print("Your schedule for FRIDAY is: ")
      print("__________________________________________________________________ ")
      for i in friday_schedule:
        print(i)
        print("__________________________________________________________________ ")
      
  elif user_input == "all" or user_input == "All":        
      print("Your full week schedule is: ")
      print("_________________________________________________________________________________________")    
      #This for loop outputs the tuple from up above to list the schedule on top of each other.
      for i in full_schedule:
           print(i)
           print("_________________________________________________________________________________________")
       
  elif user_input == "help" or user_input == "Help":
      print("Type either Monday, Tuesday, Wednesday, Thursday, or Friday to view your schedule for those days. Type All to view your full week schedule.")
      print("__________________________________________________________________ ") 
      
  else:
      print("Invalid response, please try again.")
      print("Type 'Help' for a list..")
      print("__________________________________________________________________ ")
      
#This loop is false to ensure that the loop recycles after every output.
loop = False

