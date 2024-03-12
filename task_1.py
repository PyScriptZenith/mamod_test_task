import re


def to_camel_case(text):
    return re.split('_|-', text)[0].lower() + ''.join(word.title() for word in re.split('_|-', text)[1::])


test_line_1 = 'Hello_worlds_python'  # helloWorldsPython
test_line_2 = "python_.tutorial-camelcase"  # python.TutorialCamelcase


