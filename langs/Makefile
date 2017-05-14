gen:
	pybabel extract -F ../src/babel.cfg -o pot/messages.pot ../src
	pybabel init -i pot/messages.pot -d translations -l en

edit:
	poedit translations/en/LC_MESSAGES/messages.po

update:
	pybabel extract -F ../src/babel.cfg -o pot/messages.pot ../src
	pybabel update -i pot/messages.pot -d translations -l en

compile:
	pybabel compile -d translations

rm:
	rm -rf translations/*
	rm -rf pot/*