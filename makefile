build_base:
	docker build --rm --force-rm --no-cache -f base.dockerfile -t on_track_base_image:latest .

build_on_track:
	docker build --rm --force-rm --no-cache -f on_track.dockerfile -t on_track:latest .

run_on_track:
	docker run --env-file .env --rm --name on_track_api -p 8086:8086 -it on_track:latest uvicorn main:app --host 0.0.0.0 --port 8086

run_dev_on_track:
	make build_on_track && make run_on_track