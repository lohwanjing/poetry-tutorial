
# business logic aka spring services, convert to db format, save to db


def create_person(data):
    print("Creating person: {}".format(data))


def update_person(person_id, data):
    print("Updating person with id: {}, data: {}".format(person_id, data))


def delete_person(person_id):
    print("Deleting person with id: {}".format(person_id))


def create_image(data):
    print("Creating image: {}".format(data))


def update_image(image_id, data):
    print("Updating image with id: {}, data: {}".format(image_id, data))


def delete_image(image_id):
    print("Deleting image with id: {}".format(image_id))
