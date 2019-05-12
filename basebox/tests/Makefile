.PHONY: test clean lastfailed

default: test

test:
	py.test

lastfailed:
	py.test --lf

clean:
	find . -name  "__pycache__" | xargs rm -r
	find . -name  ".pytest_cache" | xargs rm -r
