import json
import uuid

directories = ["toppings", "base_layers", "mixins", "seasonings", "shells"]

for directory in directories:
    updatedIndexData = []

    with open('{}/index.json'.format(directory)) as readable_file:
        # print(readable_file)
        indexData = json.load(readable_file)

        for item in indexData:
            with open("{}/{}.json".format(directory, item['slug']), "w") as item_file:
                item['uuid'] = "{}".format(uuid.uuid1())
                json.dump(item, item_file)
                updatedIndexData.append(item)
            item_file.close()

        readable_file.close()

    with open('{}/index.json'.format(directory), "w") as writeable_file:
        json.dump(updatedIndexData, writeable_file)
        writeable_file.close()
