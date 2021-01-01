import speech_recognition as sr 
import pyttsx3 
import random

# Initialize the recognizer 
r = sr.Recognizer() 

# Function to convert text to 
# speech 
def SpeakText(data): 
	
	# Initialize the engine 
	engine = pyttsx3.init() 
	engine.say(data) 
	engine.runAndWait() 
	
#Private data (Change as per your need)
#keep all data in lowercase as all capitalization is removed from the input (see line [43])
private_data = ['kunal', 'satwik', 'aryan', 'kushal', 'yajan', 'vijay']
# Loop infinitely for user to 
# speak 
while(1):	 
	
	# Exception handling to handle 
	# exceptions at the runtime 
	try: 
		
		# use the microphone as source for input. 
		with sr.Microphone() as source2: 
			
			# wait for a second to let the recognizer 
			# adjust the energy threshold based on 
			# the surrounding noise level 
			r.adjust_for_ambient_noise(source2, duration=0.2) 
			
			#listens for the user's input 
			audio2 = r.listen(source2) 
			
			# Using ggogle to recognize audio 
			voice_data = r.recognize_google(audio2) 
			voice_data = voice_data.lower() 
			break_value = False

			print("User Input: "+voice_data)
			voice_data_as_list = voice_data.split(" ")
			#looping both lists for comparing
			for x in private_data:
				for y in voice_data_as_list:
					if x==y:
						#removing the matching data from string so the new random name and current name are not same
						private_data.remove(x)
						#fetching random integer
						random_int_in_range = random.randint(0, len(private_data)-1)
						#fetching random name from string
						random_name = private_data[random.randint(0, random_int_in_range)]
						index_of_private_data = voice_data_as_list.index(y)
						#converting to list
						voice_data_as_list[index_of_private_data] = random_name
						voice_data = " ".join(voice_data_as_list)
						print("New masked String: "+voice_data)
						break_value = True 
						break
				if break_value==True:
					break
			SpeakText(voice_data) 
			
	except sr.RequestError as e: 
		print("Could not request results; {0}".format(e)) 
		
	except sr.UnknownValueError: 
		print("unknown error occured") 
