import json

with open("wikipedia-JSCoverage.json") as f1:
	json_obj = json.loads(f1.read())
	# print(json_obj)
	with open("raw.txt", "w") as f2:
		for junk in json_obj["junk"]:
			for junklist in junk["junk_list"]:
				f2.write(junklist + "\n");

	# print(json_obj["junk"])


with open("raw.txt") as rawf, \
	 open("input.txt", "w") as inf, \
	 open("output.txt", "w") as outf:
	prev_line = ''
	for curr_line in rawf:
		curr_line = curr_line.strip()
		if len(prev_line) > 0 and len(curr_line) > 0:
			inf.write(prev_line)
			outf.write(curr_line)
		prev_line = curr_line

