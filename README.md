# Marionette PWA
With the standard Selenium API I'm having a hard time testing the PWA capabilities of my app. Therefore I decided to look into Marionette.

I'm using virtualenv

	virtualenv .
	source bin/activate
	pip install marionette_driver

then, in another shell

	/Applications/Firefox.app/Contents/MacOS/firefox -marionette

Now we can let it walk through its paces:

	python main.py


	

