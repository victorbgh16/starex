with open('../rspec/jupiter_zoom_text.dat', 'r') as f:
    data = f.readlines()

for i in range(len(data)):
    data[i] = data[i].replace('\t', ';')
    data[i] = data[i].replace('\n', ';\n')

print(data)

with open('../rspec/jupiter_zoom_text.dat', 'w') as f:
    for line in data:
        f.write(line)