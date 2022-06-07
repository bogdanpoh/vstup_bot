import os.path

class FileManager(object):

    @staticmethod
    def get_specialities() -> dict:
        path_to_file = os.path.join(os.getcwd(), "documents/specialities.txt")
        specialities = {}

        if os.path.isfile(path_to_file):
            with open(path_to_file, "r") as file:
                array_specialities = file.readlines()

                for speciality_item in array_specialities:
                    index = array_specialities.index(speciality_item)
                    speciality = speciality_item.replace("\n", "")

                    specialities[str(index)] = speciality

        return specialities

    @staticmethod
    def get_speciality_by_index(index) -> str:
        speciality = FileManager.get_specialities().get(index, "-")
        return speciality
