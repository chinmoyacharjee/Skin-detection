import request

def main():
	url = 'http://google.com/favicon.ico'
	r = requests.get(url, allow_redirects=True)
	open('google.ico', 'wb').write(r.content)

if __name__ == "__main__":
    main()

