PY=python
PELICAN=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py
PUBLISHDIR=$(BASEDIR)/../nikn-pages

DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

help:
	@echo 'Makefile for a pelican Web site                                        '
	@echo '                                                                       '
	@echo 'Usage:                                                                 '
	@echo '   make html                        (re)generate the web site          '
	@echo '   make clean                       remove the generated files         '
	@echo '   make regenerate                  regenerate files upon modification '
	@echo '   make publish                     generate using production settings '
	@echo '   make serve [PORT=8000]           serve site at http://localhost:8000'
	@echo '   make devserver [PORT=8000]       start/restart develop_server.sh    '
	@echo '   make stopserver                  stop local server                  '
	@echo '   make ssh_upload                  upload the web site via SSH        '
	@echo '   make rsync_upload                upload the web site via rsync+ssh  '
	@echo '   make dropbox_upload              upload the web site via Dropbox    '
	@echo '   make ftp_upload                  upload the web site via FTP        '
	@echo '   make s3_upload                   upload the web site via S3         '
	@echo '   make cf_upload                   upload the web site via Cloud Files'
	@echo '   make github                      upload the web site via gh-pages   '
	@echo '                                                                       '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html'
	@echo '                                                                       '

html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean: clean_css clean_publish
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

clean_publish:
	mv $(PUBLISHDIR)/.git $(PUBLISHDIR)/../.git
	mv $(PUBLISHDIR)/.gitignore $(PUBLISHDIR)/../.gitignore
	rm -rf $(PUBLISHDIR)/*
	mv $(PUBLISHDIR)/../.git $(PUBLISHDIR)/.git
	mv $(PUBLISHDIR)/../.gitignore $(PUBLISHDIR)/.gitignore

regenerate:
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

serve:
ifdef PORT
	cd $(OUTPUTDIR) && $(PY) -m pelican.server $(PORT)
else
	cd $(OUTPUTDIR) && $(PY) -m pelican.server
endif

devserver:
ifdef PORT
	$(BASEDIR)/develop_server.sh restart $(PORT)
else
	$(BASEDIR)/develop_server.sh restart
endif

stopserver:
	kill -9 `cat pelican.pid`
	kill -9 `cat srv.pid`
	@echo 'Stopped Pelican and SimpleHTTPServer processes running in background.'

publish: clean css js
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)
	cp -r output/* $(PUBLISHDIR)
	./hashstatic $(PUBLISHDIR)

github: publish
	cd $(PUBLISHDIR); git add -A; git commit -m "site update"; git push origin gh-pages

clean_css:
	rm -rf src/scss/bootstrap/ src/scss/flatly/ src/scss/.sass-cache src/scss/*.css

bootstrap: clean_css
	mkdir -p src/scss/bootstrap/ src/scss/flatly/
	cp ~/src/bootstrap-sass/vendor/assets/stylesheets/bootstrap/* src/scss/bootstrap/
	./less2scss ~/src/bootswatch/flatly/variables.less src/scss/flatly/_variables.scss
	./less2scss ~/src/bootswatch/flatly/bootswatch.less src/scss/flatly/_bootswatch.scss

css: bootstrap
	sed -E -i '' '/family=Lato/s/^/\/\//' src/scss/flatly/_bootswatch.scss
	cd src/scss; sass nikn.scss nikn.css
	java -jar yuicompressor-2.4.8.jar ./src/scss/nikn.css > ./theme/static/css/nikn.min.css

./theme/static/js/packed.js: ./src/js/*.js
	rm -rf src/js/*.min* src/js/packed*
	#cd src/js && rm -rf packed.js && cat *.js > packed.js
	java -jar yuicompressor-2.4.8.jar -o '.js$:.min.js' src/js/*.js
	cp ./src/js/*.js ./theme/static/js/

js: ./theme/static/js/packed.js


clean_js:
	rm -rf ./theme/static/js/packed.js

.PHONY: html help clean regenerate serve devserver publish github css bootstrap clean_css clean_publish js clean_js
