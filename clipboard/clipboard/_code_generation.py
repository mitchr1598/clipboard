import requests
import json
from dataclasses import dataclass
from typing import Union


@dataclass(frozen=True)
class ClipboardClassAttributes:
    attribute_name: str
    att_type: type

    def to_code(self):
        return f'{self.attribute_name}: {self.att_type.__name__ if not self.att_type == dict else name_clean(self.attribute_name)}'


@dataclass(frozen=True)
class ClipboardClass:
    name: str
    attributes: tuple[ClipboardClassAttributes]

    def clipboard_class_names(self):
        return [att.attribute_name for att in self.attributes if att.att_type == dict]

    def to_code(self):
        attribute_code = '\n    '.join([att.to_code() for att in self.attributes]) if len(self.attributes) > 0 else 'pass'
        return f"""@dataclass(frozen=True)
class {name_clean(self.name)}:
    {attribute_code}"""


class APIData:
    def __init__(self, data: Union[list, dict], name):
        self.data = data
        self.classes = set()
        self.parse_list(self.data, name)

    def parse_dict(self, dict_data, name):
        attributes = tuple(ClipboardClassAttributes(key, type(dict_data[key])) for key in dict_data)
        clip_class = ClipboardClass(name, attributes)
        self.classes.add(clip_class)
        for name in clip_class.clipboard_class_names():
            self.parse_dict(dict_data[name], name)

    def parse_list(self, list_data, name):
        for element in list_data:
            if isinstance(element, dict):
                self.parse_dict(element, name)
            else:
                raise UnexpectedType(f"Type {type(element)} of {element} is not expected in the list")

    def to_code(self):
        return '\n\n\n'.join([clip_class.to_code() for clip_class in self.classes])


def name_clean(name):
    return name.replace('_', ' ').title().replace(' ', '').replace('-', '')


class UnexpectedType(Exception):
    pass


def main():
    token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcmdhbmlzYXRpb25JZCI6NDk2LCJqdGkiOiJkYjVhMmU3Zi1mNWY0LTRjZWUtOWU1NS1iY2FhNTk3MmI3MjAiLCJzY29wZSI6ImFwaUFjY2VzcyIsImlhdCI6MTYzNjAwMDU3NSwiZXhwIjoxNjk5MTE1Nzc1LCJpc3MiOiJodHRwczovL2NsaXBib2FyZC5hcHAifQ.QxiELxm6nDob9yP4dsO9tUThnGyIN07Nc2MdEjLYY7Q'

    api_links = [f"https://api.clipboard.app/{section}" for section in ['teams',
                                                                    'incidents',
                                                                    'sessions',
                                                                    'student-teams',
                                                                    'attendance-records',
                                                                    'users']]

    for link in api_links:
        response = requests.get(
            link,
            headers={'Authorization': 'Bearer ' + token}
        )
        module = link.split('/')[-1]
        res = json.loads(response.text)
        data = APIData(res['data'], module)
        code = data.to_code()
        with open(f'{module}.py', 'w') as file:
            file.write('from dataclasses import dataclass')
            file.write('\n'*3)
            file.write(code)
            file.write('\n')


if __name__ == '__main__':
    main()


