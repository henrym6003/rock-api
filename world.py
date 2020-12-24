import uuid


class World:
    def __init__(self):
        self.state = {}
        self.col_cnt = 0
        self.row_cnt = 0
        self.uuid = str(uuid.uuid4())

    def add_rocks(self, data):
        input_str = bytes.decode(data)
        rows = input_str.split("\n")
        rows.reverse()
        for row_idx, r in enumerate(rows):
            for col_idx, value in enumerate(r):
                if value == " ":
                    continue
                if value not in [".", ":", "T"]:
                    raise InvalidCharacterError(value)
                rock_column = self.state.get(col_idx, [])
                obj = {"type": value, "row": row_idx}
                rock_column.append(obj)
                self.state[col_idx] = rock_column

    def apply_gravity(self):
        for k, v in self.state.items():
            new_rock_column = []
            for idx, obj in enumerate(v):
                if obj["row"] == 0 or obj["type"] == "T":
                    new_rock_column.append(obj)
                    continue
                if idx == 0:
                    obj["row"] = 0
                    new_rock_column.append(obj)
                    continue
                else:
                    previous = new_rock_column[-1]
                    if previous["type"] == "." and obj["type"] == ".":
                        previous["type"] = ":"
                        new_rock_column[-1] = previous
                        continue
                    if previous["type"] == ":" and obj["type"] == ".":
                        obj["row"] = previous["row"] + 1
                        new_rock_column.append(obj)
                        continue
                    if previous["type"] == "." and obj["type"] == ":":
                        previous["type"] = ":"
                        new_rock_column[-1] = previous
                        obj["row"] = previous["row"] + 1
                        obj["type"] = "."
                        new_rock_column.append(obj)
                        continue
                    if previous["type"] == "T":
                        obj["row"] = previous["row"] + 1
                        new_rock_column.append(obj)
            self.state[k] = new_rock_column
            max_row = max(obj["row"] for obj in new_rock_column) + 1
            if max_row > self.row_cnt:
                self.row_cnt = max_row

        self.col_cnt = max(k for k in self.state.keys()) + 1

    def get_graphical_world(self):
        final_rows = {}
        for col_idx in range(self.col_cnt):
            c = self.state.get(col_idx)
            for row_idx in range(self.row_cnt):
                char_array = final_rows.get(row_idx, [])
                if c is None:
                    char_array.append(" ")
                else:
                    filtered = list(filter(lambda x: x["row"] == row_idx, c))
                    if len(filtered) > 0:
                        char_array.append(filtered[0]["type"])
                    else:
                        char_array.append(" ")
                final_rows[row_idx] = char_array
        print_ordered = list(final_rows.values())
        print_ordered.reverse()
        final = []
        for chars in print_ordered:
            final.append("".join(chars))

        return str.encode("\n".join(final))


class InvalidCharacterError(Exception):
    def __init__(self, value):
        super().__init__("Invalid character '{0}' supplied in request".format(value))














