def save_chat(history):
	try:
		with open("history.txt","w") as file:

			for speaker,message in history:

				file.write(f"{speaker}|{message}\n")

			return True

	except Exception:
		return False
