Lang = python3
OUTPUT_FILE = test.txt

test:
	$(Lang) tests.py > $(OUTPUT_FILE)

clean:
	rm -f $(OUTPUT_FILE)