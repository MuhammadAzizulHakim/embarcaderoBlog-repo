from nilearn import datasets

haxby_dataset = datasets.fetch_haxby()
# The different files
print(sorted(list(haxby_dataset.keys())))
# Path to first functional file
print(haxby_dataset.func[0])
# Print the data description
print(haxby_dataset.description)