#
# file : makefile
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

# Definitions
# -----------

EXEC_NAME = babble

# Build type : 'release' or 'debug'
BUILD_TYPE = debug

SRC_ROOT = $(abspath .)
TGT_ROOT ?= $(SRC_ROOT)/build

EXEC ?= $(TGT_ROOT)/$(EXEC_NAME)
TGT_DIRS += $(dir $(EXEC))

DATA_DIR = $(SRC_ROOT)/data

# Libraries
# ---------

# GMP
INC_DIRS += gmp
LINK_LIBS += gmp

# C Flags
# ---------

INC_DIRS += $(SRC_ROOT)/include
CPP_FLAGS += $(addprefix -I, $(INC_DIRS))

CPP_FLAGS += -std=c++14 -Wall -Wextra
ifeq ($(BUILD_TYPE), release)
	CPP_FLAGS += -O3
else ifeq ($(BUILD_TYPE), debug)
	CPP_FLAGS += -g -fsanitize=address
	CPP_FLAGS += -DDEBUG_BUILD
endif

# Link Flags
# ----------

LINK_FLAGS += $(addprefix -l, $(LINK_LIBS))
LINK_FLAGS += -pedantic -lpthread -lm

# Tools
# -----

TOOL_PREFIX ?=

CC  = $(TOOL_PREFIX)gcc
CPP = $(TOOL_PREFIX)g++
LD  = $(TOOL_PREFIX)g++
AR  = $(TOOL_PREFIX)ar

TOOL_DIR ?= $(abspath $(dir $(shell which $(CC))))

# Source files
# ------------

SRC_RFILES += $(shell ls $(SRC_ROOT)/src/*.{s,S,c,cpp} 2> /dev/null)

SRC_FILES = $(abspath $(SRC_RFILES))

OBJ_FILES += $(subst $(SRC_ROOT), $(TGT_ROOT), $(addsuffix .o, $(SRC_FILES)))
DEP_FILES += $(subst $(SRC_ROOT), $(TGT_ROOT), $(addsuffix .d, $(SRC_FILES)))

TGT_DIRS += $(dir $(OBJ_FILES) $(DEP_FILES))

# Rules
# -----

.PHONY : all clean

all : tree $(EXEC)

rebuild : clean all

run : all
	@echo "[`date "+%H:%M:%S"`] Running '$(EXEC)'..."
	@$(EXEC)

tree :
	@mkdir -p $(TGT_DIRS)

clean :
	@rm -r -f $(EXEC) $(OBJ_FILES) $(DEP_FILES) $(TGT_DIRS)

$(EXEC) : $(OBJ_FILES)
	@echo "[`date "+%H:%M:%S"`] Linking '$@'..."
	@$(TOOL_DIR)/$(LD) $(CPP_FLAGS) -o $@ $(OBJ_FILES) $(LINK_FLAGS)
	@echo "[`date "+%H:%M:%S"`] Linked '$@'."

-include $(DEP_FILES)

# Compile .cpp files
$(TGT_ROOT)/%.cpp.o : $(SRC_ROOT)/%.cpp
	@echo "[`date "+%H:%M:%S"`] Compiling '$<'..."
	@$(TOOL_DIR)/$(CPP) -MMD -c -o $@ $< $(CPP_FLAGS)
	@echo "[`date "+%H:%M:%S"`] Compiled '$@'."
