def save_chat(history):
	try:
		with open("history.txt","w") as file:

			for speaker,message in history:

				file.write(f"{speaker}|{message}\n")

			return True

	except Exception:
		return False

def load_chat():

	try:
		history=[]

		with open("history.txt",'r') as file:

			for line in file:
				speaker,message=line.strip().split('|')
				history.append((speaker,message))

		return history

	except Exception:
		return None
