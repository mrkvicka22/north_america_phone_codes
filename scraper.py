from bs4 import BeautifulSoup
import re


def get_phone_code_dict() -> dict:
    with open("website.html", "r") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    codes = soup.find("div", {"id": "codes_2"}).parent.findAll("a")
    phone_codes = {}
    for code in codes:
        string = code.getText().replace("\n", "")
        code = string[:string.index("-")].replace("\t", "").strip()
        name = re.sub(r"\t+", " ", string=string[string.index("-") + 1:]).strip().replace(", ", ",").replace(",", " ")
        phone_codes[code] = name
    return phone_codes

if __name__ == '__main__':
    print(get_phone_code_dict())