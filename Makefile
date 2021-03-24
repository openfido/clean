README.md: src/clean.py Makefile
	@echo '# OpenFIDO `clean` Pipeline' >$@
	@echo '' >>$@
	@echo '```' >>$@
	@python3 src/clean.py --help >>$@
	@echo '```' >>$@
	@echo '' >>$@
	@echo 'See [Online Documentation](https://docs.gridlabd.us/index.html?owner=openfido&project=clean&branch=main&folder=&doc=/README.md) for details.' >>$@