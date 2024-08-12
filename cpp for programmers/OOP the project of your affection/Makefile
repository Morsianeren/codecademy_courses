# This makefile is made to be used in windows

CC = g++
CFLAGS = -Wall -g
SRC_DIR = src
BUILD_DIR = build

SRC = $(wildcard $(SRC_DIR)/*.cpp)
OBJ = $(patsubst $(SRC_DIR)/%.cpp,$(BUILD_DIR)/%.o,$(SRC))
TARGET = $(BUILD_DIR)/my_program

# Rule to build the final executable
$(TARGET): $(OBJ)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJ)

# Rule to build the test executable
$(TEST_TARGET): $(TEST_OBJ)
	$(CC) $(CFLAGS) -o $(TEST_TARGET) $(TEST_OBJ)

# Rule to compile .cpp files from src/ into .o files in build/
$(BUILD_DIR)/%.o: $(SRC_DIR)/%.cpp
	@mkdir -p $(BUILD_DIR)
	$(CC) $(CFLAGS) -c $< -o $@

# Rule to clean up build files
clean:
	@echo "Cleaning up..."
	del /Q $(BUILD_DIR)\*

.PHONY: clean