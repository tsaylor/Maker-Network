all: runuwsgi nginx.conf
	true

clean:
	rm runuwsgi nginx.conf

configure.json: configure Makefile
	./configure

nginx.conf: configure.json nginx.conf.in
	./configure_file nginx.conf

runuwsgi: configure.json runuwsgi.in
	./configure_file runuwsgi
	chmod +x runuwsgi
