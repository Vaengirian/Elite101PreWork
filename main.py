import random
#Ian Chung
#Chat program
#Based off lagrassom's chatbot0.1
def generate_response(user_input, randex): #response generator
  monty = "Roughly 20.1 miles per hour"
  answer = ""
  #print("response working")
  if randex != 8: #responds randomly provided randex does not equal 8
    #print("case working")
    responses = [
      "MONT1: How interesting!",
      "MONT1: Very cool!",
      "MONT1: Well said!",
      "MONT1: Exquisite!",
      "MONT1: How sublime!",
    ]
    answer = random.choice(responses)
  else: #responds with a correct / incorrect message (easter egg)
    #print("edge case working")
    if user_input == monty:
      answer = "Mont3: Correct!"
    else:
      answer = "Mont3: Incorrect!"
  return answer
  
def init_chat(): #chat ignition
  quit_character = 'q'
  randex = 0
  questions = [ #list of various questions (+ easter egg)
    "MONT1: What hobbies do you have?\n",
    "MONT1: What's your favorite color?\n",
    "MONT1: Do you have any critters?\n",
    "MONT1: What's your favorite food?\n",
    "MONT1: What's a cause or purpose you deeply believe in?\n",
    "MONT1: Who is your favorite author?\n",
    "MONT1: What is your favorite sport or physical activity?\n",
    "MONT1: How do you like to go crazy and have fun?\n",
    "MONT3: What is the unladen speed of a swallow?\n",
  ]
  user_input = input("MONT1: Hello, how are you?\n") #start of cylce
  print(generate_response(user_input, randex) + "\n")
  
  while user_input != quit_character:
    #Ask the user for more input, then use that in your response
    
    randex = random.randint(0,len(questions)-1)
    #randex = 8
    user_input = input(questions[randex]) #asks randomly generated questions
    print(generate_response(user_input, randex) + "\n") #recieve randomly generated answers

  print("MONT1: Thanks for chatting!")
if __name__ == "__main__":
  print("Behold my first ever chatbot, MONT1, with its large array of questions!")
  print("If you want to end the program, press q.\n")
  init_chat()