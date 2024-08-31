html_template = """
<hr className={styles.separator} />
<h2 className={styles.titular}>###</h2>
"""

def make_newsfeed(titulares):
    html = ""
    for titular in titulares:
        html += html_template.replace("###", titular)
    html += "<hr className={styles.separator} />"
    return html
