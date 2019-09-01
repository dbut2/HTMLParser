string = '<html><head><link rel="stylesheet" type="text/css" href="style.css" /><title>Job Vacancy Posting System</title></head><body><div class="container"><h1>Job Vacancy Posting System</h1><hr /><h2>Home</h2><p>Name: Dylan Butler</p><p>Student ID: 101109539</p><p>Email: <a href="mailto:101109539@student.swin.edu.au">10110959@student.swin.edu.au</a></p><p>I declate the this assignment is my individual work. I have not worked collaboratively nor have I copied from any other student\'s work or from any other source.</p><hr /><p><a href="postjobform.php">Post a job vacancy</a></p><p><a href="searchjobform.php">Search job vacancies</a></p><p><a href="about.php">About</a></p></div></body></html>'


def parse_html(html):
    parsed = parse_tag(html, 0)
    return parsed


def parse_tag(html, i):
    if i == len(html):
        return False
    tag = {'name':'','attributes':{},'children':[]}
    type = 0
    value = ''
    mode = 0
    att_name = ''
    while True:
        if html[i] == '<':
            pass
        elif html[i] == '>':
            if mode == 0:
                tag['name'] = value
            elif mode == 1:
                tag['attributes'][att_name] = ''
            elif mode == 2:
                tag['attributes'][att_name] = value
            break
        elif html[i] == ' ':
            if mode == 0:
                tag['name'] = value
            elif mode == 1:
                tag['attributes'][att_name] = ''
            elif mode == 2:
                tag['attributes'][att_name] = value
            value = ''
            att_name = ''
            mode = 1
        elif html[i] == '=':
            att_name = value
            value = ''
            mode = 2
        elif html[i] == "\"":
            pass
        elif html[i] == "/":
            if html[i-1] == '<':
                type = 2
            else:
                type = 1
        else:
            value += html[i]
        i += 1
    i += 1
    if type == 0:
        while True:
            next_tag = parse_tag(html, i)
            # print({'This': {'tag': tag, 'i': i, 'type': type}, 'Next': next_tag})
            if not next_tag:
                break
            elif next_tag['type'] == 0 or next_tag['type'] == 1:
                tag['children'].append(next_tag['tag'])
                i = next_tag['i']
            elif next_tag['type'] == 2:
                i = next_tag['i']
                break
    return {'tag': tag, 'i': i, 'type': type}


def get_children(html, i):
    if html[i] == '<':
        pass
    if html[i] == '>':
        pass
    return True


print(parse_html(string))
