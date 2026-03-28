all:
	docker run --rm -it -v "$(pwd)":/app -w /app piscine-project:py310

sys-doc:
	 sudo systemctl enable --now docker

