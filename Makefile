PYTHON=python3
PROGRAM=penny

SRC_DIR=src
BUILD_DIR=build

all:
	mkdir -p $(BUILD_DIR)
	$(PYTHON) -m zipapp $(SRC_DIR) -p /usr/bin/$(PYTHON) \
		-o $(BUILD_DIR)/$(PROGRAM).pyz

clean:
	rm -rf $(BUILD_DIR)
