from ollama import chat

def get_response(user_input):

	response=chat(
		model='gemma3:1b',
		messages=[
			{
				'role':'user',
				'content':user_input
			}
		]
	)

	return response.message.content
