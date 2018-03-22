import pathlib

path = pathlib.Path(".")
directoryList = [i for i in path.iterdir()]
for i in directoryList:
		print(i)
for i in path.glob(".+\.txt"):
	print(i)
path = path / "dir"
if not path.exists():
	path.mkdir()
if path.is_dir():
	path /= "a.txt"
with path.open("w+") as file:
	file.write("W.")
