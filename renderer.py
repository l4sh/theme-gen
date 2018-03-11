'''
    renderer.py
    Render template files
'''
import os

def render_template(tpl_file, content):
    '''
    Render template file
    '''

    try:
        tpl = tpl_file.read()
    except AttributeError:
        f = open(tpl_file)
        tpl = f.read()

    return tpl.format(**content)


def render_all(tpl_dir, output_dir, content):
    '''
    Render all templates in tpl_dir to output_dir
    '''

    if not os.path.isdir(tpl_dir):
        return

    os.makedirs(output_dir, exist_ok=True)

    for tpl_file in os.listdir(tpl_dir):
        if tpl_file.endswith('.tpl'):
            rendered = render_template(
                    os.path.join(tpl_dir, tpl_file),
                    content)

            f = open(os.path.join(output_dir, tpl_file.rstrip('.tpl')), 'w+')
            f.write(rendered)



