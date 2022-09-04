import json

class modules:
    def __init__(self):
        print("modules up")

    def get_note_list(self):
        f = open("notes.json", "r")
        data = json.load(f)
        note_name_list = []
        for a in data:
            note_name_list.append(a)
        return note_name_list

    def add_note(self, note_name):
        if note_name == "":
            return
        f = open("notes.json", "r")
        data = json.load(f)
        data[note_name] = ""
        data = json.dumps(data)
        self.save(data)

    def delete_note(self, name):
        f = open("notes.json", "r")
        data = json.load(f)
        f.close()
        f = open("notes.json", "w")
        data.pop(name)
        data = json.dumps(data)
        self.save(data)

    def open(self, note_name):
        f = open("notes.json", "r")
        data = json.load(f)
        try:
            note_content = data[note_name]
        except:
            return "No such note"
        return note_content

    def save_note(self, note_name, note_content):
        f = open("notes.json", "r")
        data = json.load(f)
        f.close()
        data[note_name] = note_content
        data = json.dumps(data)
        self.save(data)

    def save(self, dict):
        f = open("notes.json", "w")
        f.write(dict)
        f.close()
        return

    def load_settings(self):
        f = open("settings.json", "r")
        data = json.load(f)
        return data

    def save_settings(self, bg, bt, fg):
        f = open("settings.json", "w")
        data = {}
        data["bg"] = bg
        data["bt"] = bt
        data["fg"] = fg
        data = json.dumps(data)
        f.write(data)
        return


