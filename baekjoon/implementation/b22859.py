# HTML 파싱
import re

html = input()
result = []

start_index = html.find('<div')

while start_index != -1:
    div_title_start = html.find('<div', start_index) + 12
    div_title_end = html.find('"', div_title_start)
    div_title = html[div_title_start:div_title_end]
    result.append("title : " + div_title)

    div_tag_end = html.find('</div>', div_title_end)

    start_index = div_title_end

    while start_index < div_tag_end:
        p_start = html.find('<p>', start_index, div_tag_end)

        if p_start == -1:
            break

        p_end = html.find('</p>', p_start)

        content = html[p_start + 3:p_end].strip()
        content = re.sub('<[^>]*>', '', content)
        content = re.sub('\s{2,}', ' ', content)
        result.append(content.strip())

        start_index = p_end

    start_index = html.find('<div', start_index)

print(*result, sep='\n')
