import uuid


class FileWorker:

    def __init__(self, file_path, file_name):
        self._file_path = file_path
        self._file_name = file_name
        self._file_location = None

        self._default_output_extension = '.txt'

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, name):
        self._file_name = name

    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, path):
        self._file_path = path

    @property
    def file_location(self):
        return str(self.file_path + '/' + self.file_name)

    def end_lines_with_comma(self):
        """Read a file as lines, add a comma to the end of each line, save it to a new file.
        Returns:
            new .txt file with a uuid4 name
        """
        new_file_name = str(uuid.uuid4()) + self._default_output_extension
        with open(self.file_name) as src_file:
            with open(new_file_name, 'w') as dest_file:
                for line in src_file:
                    dest_file.write(str(line.strip('\n') + ',' + '\n'))

    def replace_a_word_in_each_line(self, old_word: str, new_word: str):
        """ Read a file as lines, Search and replace a specific word in the whole file, save as new file.
        Args:
            old_word (str): The word you want to look up and replace
            new_word (str): the word that will replace the old word
        Returns:
            new .txt file with a uuid4 name
        """
        new_file_name = str(uuid.uuid4()) + self._default_output_extension
        with open(self.file_location) as src_file:
            with open(new_file_name, 'w') as dest_file:
                for line in src_file:
                    dest_file.write(str(line.replace(old_word, new_word)))
