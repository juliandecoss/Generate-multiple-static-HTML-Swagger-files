install:
	@[ ! -d .venv ] && python3 -m venv --copies .venv ||:;
	@( \
		source .venv/bin/activate; \
		pip install -qU pip; \
		pip install -r requirements.txt; \
	)

swagger-static:
	@.venv/bin/python ./scripts/html_generator.py ./docs/openapi

swagger-validation:
	@.venv/bin/python ./scripts/specs_openapi.py ./docs/openapi