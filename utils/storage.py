def save_chat(history):
	try:
		with open("history.txt","w") as file:

			for speaker,message in history:
				safe_message=message.replace("\n","\\n")
				file.write(f"{speaker}|{safe_message}\n")

			return True

	except Exception:
		return False

def load_chat():

	try:
		history=[]

		with open("history.txt",'r') as file:

			for line in file:
				speaker,message=line.strip().split('|',1)
				message=message.replace("\\n",'\n')
				history.append((speaker,message))

		return history

	except Exception as e:
		print(e)
		return None
