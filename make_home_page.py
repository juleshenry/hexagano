

def make_newsfeed(titulares):
    news_template = """
    <hr className={styles.separator} />
    <h2 className={styles.titular}>###</h2>
    """
    html = ""
    for titular in titulares:
        html += news_template.replace("###", titular)
    html += "<hr className={styles.separator} />"
    # properly indent
    final_html = ""
    for l in html.split('\n'):
        final_html += ' '*10 + l + "\n"
    return final_html

def make_home_page(titulares):
    home_template = """
    import Link from "next/link";
    import Head from "next/head";
    import styles from "./index.module.css";
    
    const Home = () => {
    
      return (
        <div>
          <Head>
            <link rel="icon" href="public/favicon.ico" />
          </Head>
          <div className={styles.topBar}></div>
          <div className={styles.pagestyle}>
            <Link className={styles.brandLogo} href="/">
              ONE WORLD GAZETTE
            </Link>
            <div className={styles.newsFeed}>"""
    home_template += make_newsfeed(titulares)
    home_template +="""
            </div>
            <Link className={styles.bigButton} href="/catalog">
              🌐
            </Link>
          </div>
        </div>
      );
    };
    
    export default Home;
    """
    return home_template

if __name__=='__main__':
    titulares = ["t1", "t2", "t3"]
    print(make_home_page(titulares))