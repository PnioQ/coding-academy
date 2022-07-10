import requests
import xml.etree.ElementTree as ET

r = requests.get('https://coding-academy.pl/all_customers')
root = ET.fromstring(r.text)

def task1_solution(root):
    file = open('task1_solution.txt', 'w')
    for customer in root:
        file.write(customer.text)
        file.write("\n")
    pass

if __name__ == '__main__':
    task1_solution(root)