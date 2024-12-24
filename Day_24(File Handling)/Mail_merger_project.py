with open(r"Day_24\Mail Merge Project Start\Input\Names\invited_names.txt", "r") as f2:
    names = f2.readlines()

with open(r"Day_24\Mail Merge Project Start\Input\Letters\starting_letter.txt", "r") as f1:
    content = f1.read()
    for i in names:
        stripped_name = i.strip()
        with open(f"Day_24\Mail Merge Project Start\Output\ReadyToSend\letter_for_{stripped_name}", "w") as r:
            r.write(content.replace("[name]", stripped_name))
