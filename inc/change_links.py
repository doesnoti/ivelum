# Replaces the style, script and image paths of the original website to ensure correct display

def change_links(page, URL):
    # replace the link in the logo
    header = page.find('tr')
    if header:
        logo_link = header.find('a')
        if logo_link and logo_link['href'] + '/' == URL:
            logo_link['href'] = '/'

    # replace the styles and favicon paths
    link_tags = page.find_all('link')

    for single in link_tags:
        if single['rel'][0] == 'stylesheet' or single['rel'][0] == 'shortcut':
            single['href'] = URL + single['href']

    # replace the script path
    scripts = page.find_all('script')

    for single in scripts:
        single['src'] = URL + single['src']

    # change the img path
    imgs = page.find_all('img')

    for single in imgs:
        single['src'] = URL + single['src']

    return page
