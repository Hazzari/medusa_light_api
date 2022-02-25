ifeq ("$(shell test -e config/.env && echo exist)","exist")
include config/.env
else
$(info Coping "config/.env.example" to "config/.env".)
dummy := $(shell cp config/.env.example config/.env)
include config/.env
export $(shell sed 's/=.*//' config/.env)
endif

export PYTHONPATH=$PYTHONPATH:.

CHECK_CMD=sh -c "pre-commit run isort -a && \
			pre-commit run autopep8 -a && \
			pre-commit run flake8 -a && \
			pre-commit run mypy -a && \
			pre-commit run bandit -a && \
			pre-commit run xenon -a && \
			pre-commit run bandit && \
			pre-commit run yamllint -a"


check:
	$(CHECK_CMD)

run:
	cd backend && gunicorn config.wsgi --bind 0.0.0.0:8000

pip_upgrade:
	pip install --upgrade pip setuptools pip-tools

pip-install: requirements.txt
	pip-sync requirements.txt

install: pip-install
	pre-commit install

docker-build:
	docker-compose build web

docker-run:
	docker-compose up web

docker-clean:
	docker-compose down --remove-orphans

clean: pip_upgrade docker-clean
	pip uninstall -y -r <(pip freeze)
	rm $(PROJECT_HOME)/requirements.txt
