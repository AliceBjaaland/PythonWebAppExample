import requests
def send_simple_message():
	return requests.post(
		"https://api.mailgun.net/v3/sandbox73bb17da616e4cf8a08021d9bf25974c.mailgun.org/messages",
		auth=("api", "7bf22546ca9f2b917b87f5f91ba1ba2b-acb0b40c-2c080521"),
		data={"from": "Excited User <mailgun@sandbox73bb17da616e4cf8a08021d9bf25974c.mailgun.org>",
			"to": ["awengrhys@gmail.com"],
			"subject": "Hello",
			"text": "Testing some Mailgun awesomness!"})

send_simple_message()
