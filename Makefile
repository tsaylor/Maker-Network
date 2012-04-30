all: runuwsgi nginx.conf gaggled.conf
	true

clean:
	rm runuwsgi nginx.conf

configure.json: configure Makefile
	./configure

gaggled.conf: configure.json gaggled.conf.in
	./configure_file gaggled.conf

nginx.conf: configure.json nginx.conf.in
	./configure_file nginx.conf

runuwsgi: configure.json runuwsgi.in
	./configure_file runuwsgi
	chmod +x runuwsgi
