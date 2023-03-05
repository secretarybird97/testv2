import argostranslate.package, argostranslate.translate
import translatehtml
import glob

from_code = "en"
to_code = "hi"

available_packages = argostranslate.package.get_available_packages()
available_packages = list(
    filter(
        lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
    )
)[0]

download_path = available_packages.download()
argostranslate.package.install_from_path(download_path)

installed_languages = argostranslate.translate.get_installed_languages()
from_lang = list(filter(lambda x: x.code == from_code, installed_languages))[0]
to_lang = list(filter(lambda x: x.code == to_code, installed_languages))[0]

files = glob.glob("**/*.html", recursive=True)

for file in files:
    print(file)

    html_doc = open(file, "r")
    translation = from_lang.get_translation(to_lang)

    translated_soup = translatehtml.translate_html(translation, html_doc)

    # overwrite the file
    with open(file, "w") as f:
        f.write(str(translated_soup))

    html_doc.close()

print("Done translating html files! :)")

# Path: translatehtml.py
