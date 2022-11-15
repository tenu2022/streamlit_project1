import toml

output_file = ".streamlit/secrets.toml"

with open("private/raspberry1-47370-firebase-adminsdk-9eb4u-92da494d53.json") as json_file:
    json_text = json_file.read()

config = {"textkey": json_text}
toml_config = toml.dumps(config)

with open(output_file, "w") as target:
    target.write(toml_config)