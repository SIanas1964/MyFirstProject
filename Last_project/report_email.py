#!/usr/bin/env python3

"""
Generate report and sends email
"""
import os
import reports
import datetime
import email

def data_to_paragraph(path):
    descriptions_list = os.listdir(path)
    description_data = []
    for description_file in descriptions_list :
        with open(path + "/" + description_file, 'r') as description :
            lines = description.readlines()
            description_data.append("name" + lines[0].strip('\n') + "<br/>" + "weight" + lines[1].strip('\n') + "<br/>")
    description_data_paragraph = "<br/>".join(description_data)
    return description_data_paragraph

def main(path):
    filepath = "/tmp/processed.pdf"
    title = "Processed Update on {}".format(datetime.date.today().strftime("%B %d, %Y"))
    paragraph = data_to_paragraph(path)
    reports.generate_report(filepath, title, paragraph)
    message = email.generate_email("automation@example.com","username@example.com", "Upload Completed - Online Fruit Store", "All fruits are uploaded to our website successfully. A detailed list is attached to this email.",filepath)
    email.send_email(message)

if __name__ == "__main__":
    datapath = "supplier-data/descriptions"
    main(datapath)