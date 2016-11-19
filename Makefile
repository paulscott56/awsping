venv: requirements.txt
	virtualenv $@ -p `which python2.7` --clear
	$@/bin/pip install -r $<

mobaping.zip: venv mobaping.py
	cd $</lib/python2.7/site-packages/ && zip ../../../../$@ -r *
	zip --grow $@ mobaping.py

clean:
	rm -f mobaping.zip

bundle: clean mobaping.zip

.PHONY: bundle clean
