import json
import uuid


def scrape_index_into_files(category):
    with open('{}/index.json'.format(category)) as f:
        indexData = json.load(f)

    for item in indexData:
        with open("{}/{}.json".format(category, item['slug']), "w") as item_file:
            item['uuid'] = "{}".format(uuid.uuid1())
            json.dump(item, item_file)
        item_file.close()

    f.close()


directories = ["toppings", "base_layers", "mixins", "seasonings", "shells"]
for directory in directories:
    scrape_index_into_files(directory)
