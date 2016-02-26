import requests
import pudb 

class Model:

	# do I neeed an init ?!

	def movie_info(self):
		movie_info = requests.get("http://www.omdbapi.com/?t=finding+nemo&y=&plot=short&r=json").json()
		return movie_info


