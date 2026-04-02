all: run

run:
	docker run --rm -it -h test-env-py10 -v $$PWD:/app -w /app py310 bash
build:
	docker build -t py310 .

sys-doc:
	 sudo systemctl enable --now docker
